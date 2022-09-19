![image-20220916164619114](ResNeXt.assets/image-20220916164619114.png)

![image-20220916164836107](ResNeXt.assets/image-20220916164836107.png)

![image-20220916164927039](ResNeXt.assets/image-20220916164927039.png)  

![image-20220916165708095](ResNeXt.assets/image-20220916165708095.png)

![image-20220916171852193](ResNeXt.assets/image-20220916171852193.png)

![image-20220916171910502](ResNeXt.assets/image-20220916171910502.png)

![image-20220916171920802](ResNeXt.assets/image-20220916171920802.png)

上面两个图，一个不通过group，一个group为2，但是他们得到的的feature map是一样的

![image-20220916201909397](ResNeXt.assets/image-20220916201909397.png)

![image-20220916202625868](ResNeXt.assets/image-20220916202625868.png)

- 32*4d表示的是每个group中的channel数，C=32表示group数，越往后的stage发现C并没有变化，所以此时每个group的数量就会翻倍

![image-20220916205407327](ResNeXt.assets/image-20220916205407327.png)

- 作者实验发现32*4d的效果最好

![image-20220916210443195](ResNeXt.assets/image-20220916210443195.png)

当Block中的层数<3时虽然左右两种的计算上是等价的，但是作用不大