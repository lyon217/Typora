![image-20220915170813342](YOLO_v3SPP.assets/image-20220915170813342.png)

## Mosaic图像增强

![image-20220915170835990](YOLO_v3SPP.assets/image-20220915170835990.png)

默认使用4张图像进行拼接训练

- 在使用Misaic的基础上再加上BN其实是变相增大了batchsize，因为BN就是在求均值方差，如果数据集越大，那么越接近整体数据集的均值方差，效果就会越好，所以这种变相增大batchsize的方式还是有一定效果的

## SPP模块

SPP模块和SPPnet中的SPP结构不一样，只能说是借鉴

![image-20220915171343820](YOLO_v3SPP.assets/image-20220915171343820.png)

- 三个maxpool的stride都是1，然后根据padding可以保证whc都是不变的，从而实现了不同尺度的特征的融合 

- 当然，为什么要在第一个预测特征层前上SPP，而不是在每一个预测特征层前都加上或者说在最后一个预测特征层前加上？

    ![image-20220915172500949](YOLO_v3SPP.assets/image-20220915172500949.png)

![image-20220915171705392](YOLO_v3SPP.assets/image-20220915171705392.png)

## CIoU Loss

### IoU Loss

![image-20220915172551240](YOLO_v3SPP.assets/image-20220915172551240.png)

![image-20220915173058671](YOLO_v3SPP.assets/image-20220915173058671.png)

- 通过上图可以发现的是即使在l2 Loss的值一致的情况下，IOU也是可能不一致的，这也说明了l2 loss不能很好的反应两个目标边界框重合的程度，所以引入了IoU Loss = $-lnIoU$,还有一个比较常见的IoULoss的计算公式就是1-IoU，IoUloss相对于l2loss的好处就是1.能够更好的反应重合程度，2.具有尺度不变性，就是无论重叠的两个矩形框是大还是小，它的重合程度与矩形框的尺度是无关的
- 缺点是当bb与gt的IoU为0时，loss为inf，无法训练，因此IoULoss在回归任务中表现不好

### GIoU Loss

![image-20220915175153463](YOLO_v3SPP.assets/image-20220915175153463.png)

- 绿色是gt，红色是bb，蓝色是$A^c$，u是并集，当bb和gt完全重合的时候，ac就等于u，IoU等于1，此时GIoU=1，当bb和gt完全无关的时候，GIoU=IoU-1+u/ac,此时iou=0,u/ac=0,此时GIoU=-1，所以$L_{GIoU}=1-GIoU(0<=L_{GIoU}<=2)$ 

![image-20220915194301757](YOLO_v3SPP.assets/image-20220915194301757.png)

- GIoU在bb和gt在同一水平或者高度的时候，就退化为IoU

### DIoU Loss-Distance IoU

![image-20220915212710975](YOLO_v3SPP.assets/image-20220915212710975.png)

Liou和LGiou都有的问题是收敛慢，并且回归的不够准确

![image-20220915212743997](YOLO_v3SPP.assets/image-20220915212743997.png)

- $\rho$代表的是欧氏距离，
- b是预测边界框的中心坐标，b^gt是真实框的中心坐标，
- c是两个框的最小外接矩形的对角线的长度
- 两个框重合的时候，d是等于0的，那么DIoU=IoU-0
- 当两个框相距无穷远的时候，d^2/c^2->1，所以此时DIoU=IoU-1=0-1 -> -1
- DIoU损失能够直接最小化两个boxes之间的距离，因此收敛速度更快

### CIoU Loss-Complete IoU

![image-20220915213850494](YOLO_v3SPP.assets/image-20220915213850494.png)

- AP75就是IOU的阈值为0.75
- $L_{CIoU}(D)$是将公式中的IOU替换为DIOU

![image-20220915214025142](YOLO_v3SPP.assets/image-20220915214025142.png)

## Focal Loss

![image-20220915214146375](YOLO_v3SPP.assets/image-20220915214146375.png)

![image-20220915214528462](YOLO_v3SPP.assets/image-20220915214528462.png)

#### 引入$\alpha$

![image-20220916091738549](YOLO_v3SPP.assets/image-20220916091738549.png)

- 使用的策略是\alpha 对于正样本，负样本则使用 1-\alpha

- $\alpha$只是一个超参数，来调整正负样本的权重，并不是正负样本的比例，

![image-20220916092126184](YOLO_v3SPP.assets/image-20220916092126184.png)

- $(1-p_t)^y$能够降低易分样本的损失贡献，易分样本就是右边表格中，的well-classified examples，这些都是$p_t$的值非常大的样本
- 易分样本是指无论正负并且预测得到的正确率很高的样本

![image-20220916092548139](YOLO_v3SPP.assets/image-20220916092548139.png)

- 将$\alpha$和两个部分结合起来发现当\alpha=0.25，\gmma=2.0时是最好的

![image-20220916093212702](YOLO_v3SPP.assets/image-20220916093212702.png)

- 通过表格可以看到 Focal Loss的核心就是可以更加专注于训练比较难学习的样本

使用Focal Loss要注意的是训练集中尽量不好有错误的样本，否则会使劲学习错误样本