## BTC 加密货币
1. BTC 白皮书，2018.06.30 看完。 很highlevel的介绍，需要结合code理解。对攻击者成功概率的计算公式理解不透彻，以后有机会再仔细研究。[白皮书](https://github.com/daleiyang/btc-cryptocurrency-consensus/blob/master/BitcoinAndCryptocurrencyTechnologies/bitcoin.pdf)
2. Mastering Bitcoin: Programming the Open Blockchain

    |章节|完成时间|
    |:----------|:----------|
    |全书通读|2018-07-03 到 2018-07-31|
    
    [读书笔记](https://github.com/daleiyang/btc-cryptocurrency-consensus/tree/master/BitcoinAndCryptocurrencyTechnologies/MasteringBitcoin2thEdition)

3. BTC v0.3.22 源代码阅读

    [阅读笔记](https://github.com/daleiyang/btc-cryptocurrency-consensus/tree/master/BitcoinAndCryptocurrencyTechnologies/Satoshi'sOriginalBitcoinClient)	

## 分布式系统一致性
1. Paxos 算法 
   * 目前进展：截至2017年3月15号，我正在细读Miguel Castro的论文并理解Liskov的代码，尽快完成原型开发，完成后我会详细讲讲解决拜占庭将军问题的Paxos算法到底是个什么东东，是如何实现的。如有兴趣请保持关注:)
   * 背景：在2015年11月到2016年2月期间，我隶属的XX公司XX组有一套基于微软云服务的内容管理平台，它是XX公司XX组对外各种网站的基础架构，XX公司XX组大部分对外网站均构建于其上。这个平台的数据存贮依赖于微软云的存储服务，同时也依赖于存储服务所提供的数据复制功能将主节点的数据同步到全球的其他多个云服务数据中心。但是这个同步服务的能力没有能够达到用户的希望。我利用业余时间系统阅读了相关主题的论文，最后发现参考MSR的Miguel Castro的论文[Practical Byzantine Fault Tolerance](https://github.com/daleiyang/btc-cryptocurrency-consensus/blob/master/Paxos/Thesis/castro-thesis.pdf)、MIT的 Liskov提供的[Practical Byzantine Fault Tolerance](http://www.pmg.csail.mit.edu/bft) 示例程序、再结合Google的[Paxos Made Live - An Engineering Perspective](https://research.google.com/archive/paxos_made_live.pdf)的实现方法是一条可行之路。遗憾的是实际项目由于需要较多资源投入的原因没能够启动。下面列出系统设计文档，其中包括我仔细阅读过的14篇论文和其他文献、项目资源估算报告。
   * 相关资料存储处：[https://github.com/daleiyang/btc-cryptocurrency-consensus/tree/master/Paxos/Thesis](https://github.com/daleiyang/btc-cryptocurrency-consensus/tree/master/Paxos/Thesis)
   * 系统设计文档：[Highly-Available Distributed In-Memory Cache with Byzantine Paxos](https://github.com/daleiyang/btc-cryptocurrency-consensus/blob/master/Paxos/Highly-Available%20Distributed%20In-Memory%20Cache%20with%20Byzantine%20Paxos.doc)
   * 实现时间和人力估算：[Replication with Byzantine Paxos Current Status and Estimation](https://github.com/daleiyang/btc-cryptocurrency-consensus/blob/master/Paxos/Replication%20with%20Byzantine%20Paxos%20Current%20Status%20and%20Estimation.doc)
