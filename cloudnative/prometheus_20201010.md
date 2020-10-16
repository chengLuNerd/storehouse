## 20201010

[TOC]

### PromQL

Prometheus provides a functional query language called PromQL (Prometheus Query Language) that lets the user select and aggregate time series data in real time. 





### 服务发现

当前的问题是对于指定的每个目标，我们在抓取配置中手动列出他们的IP地址和端口，这种方法在主机较少的时候还可以，但不适用于使用容器和基于云的实例的动态集群，这些实例经常会出现变化、创建或销毁。

prometheus通过服务发现，自动化的机制来检测、分类和识别新的和变更的目标。有如下几种服务发现方案：

1. 基于文件的方式
2. 基于云的方式
3. 基于DNS的方式

**基于文件的服务发现**

``` yaml
- job_name: node
  file_sd_configs:
    - files:
      - targets/nodes/*.json
      refresh_interval: 5m

# 使用file_sd_configs替换prometheus.yml文件中的static_configs
# 每隔 refresh_interval时间检测文件是否有变更。

```

node.json文件

``` json
[{
 "targets": [
     ":9100",
     ":9100",
     ":9100"
 ]   
}]
```

数据来源通常来自于CMDB。有一些工具从CMDB中获取对应的目标转换成服务发现文件。

**基于API的服务发现**

这里我们只关心kubernetes，后面监控kubernetes时会详细介绍。其它的平台有Consul、Azure、AmazonEC2、Google Compute Cloud等。

**基于DNS的服务发现**

``` yaml
- job_name: webapp
  dns_sd_configs:
    - names: ['']
# 我们指定了一个dns_sd_configs块。其中指定的names参数包含要查询的DNS条目列表
```

关于DNS有些术语还不太清楚

依赖于A、AAAA或SRV DNS记录查询？？

