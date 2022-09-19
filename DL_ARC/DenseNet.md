## 介绍

![image-20220916110244045](DenseNet.assets/image-20220916110244045.png)

![image-20220916112216844](DenseNet.assets/image-20220916112216844.png)

## 设计理念

![image-20220916100838161](DenseNet.assets/image-20220916100838161.png)

![image-20220916101411855](DenseNet.assets/image-20220916101411855.png)

![image-20220916110851906](DenseNet.assets/image-20220916110851906.png)

## 网络结构

### Dense Block

![img](https://pic4.zhimg.com/v2-0b28a49f274da9bd8dec2dccddf1ec53_b.jpg)

![image-20220916111226726](DenseNet.assets/image-20220916111226726.png)

![image-20220916111749369](DenseNet.assets/image-20220916111749369.png)

- 上图计算细节：在每个DenseBlock中，每个层的计算结果，也就是经过$H(.)$的结果的channel都是k，然后再加上之前cat n-1层的结果

#### DenseBlock+bottleneck -> DenseNet-B

![image-20220916111909517](DenseNet.assets/image-20220916111909517.png)

- 通常1*1卷积输出的通道数通常是GrowthRate(K)的4倍 

### Transition

#### Transition + compression rate -> DenseNet-C

![image-20220916112135482](DenseNet.assets/image-20220916112135482.png)

![image-20220916151451685](DenseNet.assets/image-20220916151451685.png)

## 性能对比

### pre-activation

![image-20220916113448674](DenseNet.assets/image-20220916113448674.png)

![image-20220916153937761](DenseNet.assets/image-20220916153937761.png)

![image-20220916154104440](DenseNet.assets/image-20220916154104440.png)

## DenseNet的优势

### 1.更强的梯度流动

![image-20220916154316357](DenseNet.assets/image-20220916154316357.png)

### 2.减少了参数量

DenseNet的DenseBlock中越往后的层虽然参数越多，但是大部分都可以直接来自前面，所以参数量更少

![image-20220916154849317](DenseNet.assets/image-20220916154849317.png)

### 3.保存了低维度的特征

![image-20220916155208017](DenseNet.assets/image-20220916155208017.png)

## DenseNet的不足

DenseNet由于需要进行多次Concatnate操作，数据需要被多次复制，显存容易增加的很快，需要一定的显存优化技术，另外DeseNet是一种更为特殊的网络，ResNet则相对一般化一些，所以ResNet的应用范围更广

一种高效的DenseNet的实现：论文如下：[Memory-Efficient Implementation of DenseNets](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/1707.06990)

不过可以使用PyTorch框架自动实现这种优化

![image-20220916155957157](DenseNet.assets/image-20220916155957157.png)

