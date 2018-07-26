## BTC 加密货币
1. BTC 白皮书，2018.06.30 看完。 很highlevel的介绍，需要结合code理解。对攻击者成功概率的计算公式理解不透彻，以后有机会再仔细研究。[白皮书](https://github.com/daleiyang/btc-cryptocurrency-consensus/blob/master/BitcoinAndCryptocurrencyTechnologies/bitcoin.pdf)
2. Mastering Bitcoin: Programming the Open Blockchain

    |章节|完成时间|
    |:----------|:----------|
    |Chapter 1. Introduction|2018-07-03|
    |Chapter 2. How Bitcoin Works|2018-07-03|
    |Chapter 3. Bitcoin Core: The Reference Implementation|2018-07-09|
    |Chapter 4. Keys, Addresses|2018-07-11|
    |Chapter 5. Wallets|2018-07-12|
    |Chapter 6. Transactions|2018-07-16|
    |Chapter 7. Advanced Transactions and Scripting|2018-07-17|
    |Chapter 8. The Bitcoin Network|2018-07-19|
    |Chapter 9. The Blockchain|2018-07-20|
    |Chapter 10. Mining and Consensus|2018-07-26|
    |Chapter 11. Bitcoin Security|进行中|
    
   Notes：
   * 用Azure ubuntu VM, 外加256G的SSD搭建了环境，同步区块链速度还可以。
   * 通过python-bitcoinlib库和full node交互很方便。
   * V神的pybitcointools，要从git上下载，用setup.py安装；和 python-bitcoinlib冲突，需要先删除python-bitcoinlib。
   * 第5章是的钱包制作指南。重点是HD钱包生成公钥私钥的原理，有很多的细节，有实际需要采用得着。
   * 第10章是精华所在，体会如下：
     1. 之所以搞出10分钟搞出一个区块，目的就是简化在所有机器中同步状态的难度。
     2. BTC的激励机制、根据全网算力动态调整猜谜难度的设计很牛，解决了如何在去中心化的环境中，维护整体网络可靠可用的问题。
     对比了BTC的“去中心化”一致 和 Paxos 的 "可以自由选主的中心化" 一致，有些想法，记录如下：
     1. BTC让所有的矿工一起猜迷题，谁先猜出来谁说了算；对应到Paxos， 只有 "主" 节点说了算：对于BTC来说，谁猜中了，他的结果（区块）大家都认可；在这一轮中，他就是“主"；下一轮，不一定谁是”主“；Paxos 谁是 ”主“ 谁说了算，除非重新选”主“，否则就一直是这个节点说了算。
     2. BTC有多个矿工同时猜出来，都广播自己的结论，出现不一致；对应到Paxos，就是多 "主" 并存，需要重新选 "主"。对于BTC，在一轮中，如果有多个矿工同时猜出来，都广播自己的结论，这就是多个节点都认为自己是”主“，BTC中出现了不一致。依靠10分钟猜一次、谁投入的算力多，就认可谁的结果 这种设计，能够最终在全网解决不一致的问题。对Paxos来说，也会出现多个节点都认为自己是”主“的情况，导致不一致出现，但也有一套协议最终能够达到全网一致。
     3. 效率上来说，肯定是Paxos完胜，绝不会需要10分钟的delay，代价就是协议复杂度高。

## 分布式系统一致性
1. Paxos 算法 
   * 目前进展：截至2017年3月15号，我正在细读Miguel Castro的论文并理解Liskov的代码，尽快完成原型开发，完成后我会详细讲讲解决拜占庭将军问题的Paxos算法到底是个什么东东，是如何实现的。如有兴趣请保持关注:)
   * 背景：在2015年11月到2016年2月期间，我隶属的XX公司XX组有一套基于微软云服务的内容管理平台，它是XX公司XX组对外各种网站的基础架构，XX公司XX组大部分对外网站均构建于其上。这个平台的数据存贮依赖于微软云的存储服务，同时也依赖于存储服务所提供的数据复制功能将主节点的数据同步到全球的其他多个云服务数据中心。但是这个同步服务的能力没有能够达到用户的希望。我利用业余时间系统阅读了相关主题的论文，最后发现参考MSR的Miguel Castro的论文[Practical Byzantine Fault Tolerance](https://github.com/daleiyang/btc-cryptocurrency-consensus/blob/master/Paxos/Thesis/castro-thesis.pdf)、MIT的 Liskov提供的[Practical Byzantine Fault Tolerance](http://www.pmg.csail.mit.edu/bft) 示例程序、再结合Google的[Paxos Made Live - An Engineering Perspective](https://research.google.com/archive/paxos_made_live.pdf)的实现方法是一条可行之路。遗憾的是实际项目由于需要较多资源投入的原因没能够启动。下面列出系统设计文档，其中包括我仔细阅读过的14篇论文和其他文献、项目资源估算报告。
   * 相关资料存储处：[https://github.com/daleiyang/btc-cryptocurrency-consensus/tree/master/Paxos/Thesis](https://github.com/daleiyang/btc-cryptocurrency-consensus/tree/master/Paxos/Thesis)
   * 系统设计文档：[Highly-Available Distributed In-Memory Cache with Byzantine Paxos](https://github.com/daleiyang/btc-cryptocurrency-consensus/blob/master/Paxos/Highly-Available%20Distributed%20In-Memory%20Cache%20with%20Byzantine%20Paxos.doc)
   * 实现时间和人力估算：[Replication with Byzantine Paxos Current Status and Estimation](https://github.com/daleiyang/btc-cryptocurrency-consensus/blob/master/Paxos/Replication%20with%20Byzantine%20Paxos%20Current%20Status%20and%20Estimation.doc)
