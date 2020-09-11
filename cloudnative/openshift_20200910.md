## 20200910

[TOC]

### 安装minishift

1. 安装virtualBox

https://www.virtualbox.org/wiki/Linux_Downloads

报错：

``` shell
[root@UVM41 test]# rpm -ivh VirtualBox-6.1-6.1.14_140239_el7-1.x86_64.rpm 
警告：VirtualBox-6.1-6.1.14_140239_el7-1.x86_64.rpm: 头V4 DSA/SHA1 Signature, 密钥 ID 98ab5139: NOKEY
错误：依赖检测失败：
	libSDL-1.2.so.0()(64bit) 被 VirtualBox-6.1-6.1.14_140239_el7-1.x86_64 需要
	libopus.so.0()(64bit) 被 VirtualBox-6.1-6.1.14_140239_el7-1.x86_64 需要
```

解决方法：

``` shell
yum install SDL -y
yum install opus -y
```

2. 下载minishift 

[v1.34.2](https://github.com/minishift/minishift/releases/tag/v1.34.2)

解压执行如下命令：

``` shell
./minishift start --vm-driver virtualbox
```

因为网络问题，也可以通过--skip-startup-checks参数跳过检查；

自己下载oc文件[v3.11.0](https://github.com/openshift/origin/releases/tag/v3.11.0)，放置到/root/.minishift/cache/oc/v3.11.0/linux/目录下面；

自己下载文件minishift-centos7.iso文件[v1.16.0](https://github.com/minishift/minishift-centos-iso/releases/tag/v1.16.0)，放置到/root/.minishift/cache/iso/centos/v1.16.0/目录下面；



还是报错呀,是因为虚拟机的原因吧。

``` shell
-- Starting Minishift VM ...... FAIL E0910 14:57:06.395523   18268 start.go:494] Error starting the VM: Error creating the VM. Error with pre-create check: "This computer doesn't have VT-X/AMD-v enabled. Enabling it in the BIOS is mandatory". Retrying.
Error starting the VM: Error creating the VM. Error with pre-create check: "This computer doesn't have VT-X/AMD-v enabled. Enabling it in the BIOS is mandatory"
```

 