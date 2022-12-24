## 动机

![image-20220913205850999](49_%E4%BD%BF%E7%94%A8%E6%B3%A8%E6%84%8F%E5%8A%9B%E6%9C%BA%E5%88%B6%E7%9A%84seq2seq.assets/image-20220913205850999.png)

## 加入注意力

![image-20220913205953867](49_%E4%BD%BF%E7%94%A8%E6%B3%A8%E6%84%8F%E5%8A%9B%E6%9C%BA%E5%88%B6%E7%9A%84seq2seq.assets/image-20220913205953867.png)

![image-20220913210630093](49_%E4%BD%BF%E7%94%A8%E6%B3%A8%E6%84%8F%E5%8A%9B%E6%9C%BA%E5%88%B6%E7%9A%84seq2seq.assets/image-20220913210630093.png)

- Attention模块，将编码器对应每个词的输出作为key和value，二者其实是一个东西，假设英语句子长为3，那么就会有3个key-value-pair，也就是每一个词的对应的RNN的输出，所以之前的Seq2Seq相当于只用了最后一个keyvalue，但是现在将每个时刻的keyvalue都放到Attention模块中。 

- query是解码器RNN对上一个词的输出，比如上一次的输出是hello的话，现在开始翻一下一个词时，就把它放到Attention里，然后把它附近的一些东西圈出来，当然因为现在还没得到hello预测的结果world，所以是无法拿到World的Embedding的。我们可以假设RNN的输出都是在同一个语义空间里的，所以我们要用输出，而不能用Embedding的输入，因为keyvalue也是RNN的输出，所以key和query做匹配的时候，最好也是用同样一个RNN的输出，差不多在一个语义空间里，这样  比较好。然后match到一个输出后，再将这个输出当做query进行预测下一个，也就相当于替换掉了原始seq2seq中的context_variable

## 总结

![image-20220913214513586](49_%E4%BD%BF%E7%94%A8%E6%B3%A8%E6%84%8F%E5%8A%9B%E6%9C%BA%E5%88%B6%E7%9A%84seq2seq.assets/image-20220913214513586.png)