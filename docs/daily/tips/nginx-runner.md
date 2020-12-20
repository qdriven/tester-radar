---
layout: posts
title: 测试日志2020-5 前端部署 NGINX Conf文件自动配置
date: 2020-07-30 12:12:00
categories: [python,eat-dog-food,test-ops]
tags: [python,eat-dog-food,test-ops]
---

## 前端部署 NGINX Conf文件自动配置

新部署了一个服务，测试环境NGINX帮忙配置一下；这周老鸟被这些事情忙的不亦乐乎，一会nginx加一个环境配置，
一会部署一个测试环境前端,一会重启一些nginx,一周很快就过去了，老鸟感觉一周测试的事情做的很少，倒是做了很多nginx运维的事情.
按照现在流行的说法叫test-ops，不知道哪个天才创造了这个职位名称，但是很遗憾，老鸟不能再招人了，公司HC已经冻结了，但是如果一直这样也不是个事情呀. 怎么解决？老鸟除了这些破事，还有其他项目要搞，会要开，还想着早点回家和小孩做做几何题，怎么办？

问题怎么解决？ 老鸟一般问题会遵照下面几个步骤进行:
1. 问题是什么？想要解决什么问题
2. 有没有现成的解决方案？解决的思路是什么
3. 不求完美解决，但求80%以上解决问题
<!-- more -->
## 1. 问题是什么

问题其实很清楚，目前通过手工的方式修改NGXIN conf文件， 然后手工重启(reload)nginx进行配置更新,严重影响了工作产出了,如果不能够解决这些重要又紧急的事情，产出就不够了，年纪大了可能就被人嫌弃了, 那么怎么解决呢？

无论如何先从实际情况出发，ngxin 配置到底配置的是什么? 这个NGINX前端的配置其实说来很简单,就是在NGINX CONF文件里面给每个新的项目(project2)添加URL路径,以及router的配置:

- 1. nginx Location 配置
```sh 
location /project2 {
    try_files $uri $uri/ @router;
    index index.html;
}
```
- 2. project2 router的配置添加: 把project2的index.html加到router里面

```sh	
location @router {
    rewrite ^.*$ /index.html last;
    rewrite ^.*$ /mng/index.html last;
    rewrite ^.*$ /client/index.html last;
    rewrite ^.*$ /engineer/index.html last;
    rewrite ^.*$ /project2/index.html last;
}
```

把这些手动的事情自动化了，同时不加新的沟通，还沿用原来的使用方式,用户使用方面不需要又任何变化. 

为什么修改一个东西，我觉得大体分两种情况
1. 原来用户的使用习惯不需要变化，默默把他需要的事情给做了
2. 如果要改变用户的使用方式，一定要大大提高用户的效率，否者用户有隐性成本

某种程度上Do't make me think的产品设计未必任何情况下都是对的， 也有一种可能就是扇用户两巴掌，说你有点傻，换个方式可以让你提高很多效率。

## 1.1 解决思路

在开始考虑解决思路的时候，先考虑两个问题，当前的约束条件(一些现状)和最终要达成的目标.

- 约束条件
公司没有什么高大上的服务发现，K8S集群，就只有一个NGINX服务给测试环境用,同时部署是通过JENKINS来发布的. 所以解决的办法不能超过这个范畴.

- 最终要达成的效果

1. QA触发项目的新建的前端Jenkins任务
2. QA开始测试新的前端项目

- 完成目标分解的任务

整件事情其实简单讲就是：
1. 输入： projectName
2. 输出:  对应的nginx conf就生成好，同时nginx生效(也就是需要reload)

那么接下来的问题是从哪里输入这个projectName，目前看如果要融入到流程里面就已有一个地方，那就是Jenkins 部署的脚本里面.
