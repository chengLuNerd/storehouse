## 20201011

[TOC]

### 警报管理

即如何从监控数据中生成警告







Prometheus安装方式

**k8s**

[kayrus/*prometheus*-*kubernetes*](https://github.com/kayrus/prometheus-kubernetes)

[camilb/*prometheus*-*kubernetes*](https://github.com/camilb/prometheus-kubernetes)

**docker-compose**

[vegasbrianc/*prometheus*](https://github.com/vegasbrianc/prometheus)



这个先记录下，可以关注下，星星挺多的

[prometheus-operator/kube-*prometheus*](https://github.com/prometheus-operator/kube-prometheus)

Use *Prometheus* to *monitor* Kubernetes and applications running on Kubernetes



### Thanos概述

http://dockone.io/article/6019

Thanos项目的最初目标之一是无缝集成任意现有的Prometheus实例。第二个目标是操作应该尽量简单，并且应该尽可能降低准入门槛。



### Thanos架构

1. #### 全局视图

![img](pics/prometheus_20201011/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_16028404752750.png)

为了能够在现有的Prometheus集群之上收获一个全局视图，我们需要将中央查询层和所有服务器互联。

Thanos [Sidecar](https://kubernetes.io/blog/2015/06/the-distributed-system-toolkit-patterns#example-1-sidecar-containers)组件即是担任这样的角色，它会被部署到每一台正在运行的Prometheus服务端一侧。它充当的是一个代理服务器，通过Thanos规范化的基于gRPC的Store API提供Prometheus的本地数据，它也允许通过标签和时间段来选择时间序列数据。

2. #### 不受限的保留数据

![img](pics/prometheus_20201011/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_16028406063501.png)

