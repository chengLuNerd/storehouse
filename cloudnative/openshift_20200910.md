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

 

换了一台服务器：

``` shell
root@ks-allinone:~/test# minishift start --vm-driver virtualbox --skip-startup-checks
-- Starting profile 'minishift'
-- Starting the OpenShift cluster using 'virtualbox' hypervisor ...
-- Minishift VM will be configured with ...
   Memory:    4 GB
   vCPUs :    2
   Disk size: 20 GB
-- Starting Minishift VM .......................... OK
-- Writing current configuration for static assignment of IP address ... OK
   Importing 'openshift/origin-control-plane:v3.11.0' . CACHE MISS
   Importing 'openshift/origin-docker-registry:v3.11.0'  CACHE MISS
   Importing 'openshift/origin-haproxy-router:v3.11.0'  CACHE MISS
-- OpenShift cluster will be configured with ...
   Version: v3.11.0
-- Pulling the OpenShift Container Image .Error pulling the OpenShift container image: ssh command error:
command : docker pull openshift/origin-control-plane:v3.11.0
err     : exit status 1
output  : Trying to pull repository docker.io/openshift/origin-control-plane ... 
Get https://registry-1.docker.io/v2/: x509: certificate signed by unknown authority

```



Error response from daemon: Get https://registry-1.docker.io/v2/: x509: certificate signed by unknown authority

应该是证书的问题。

``` shell
echo -n | openssl s_client -showcerts -connect registry-1.docker.io:443 2>/dev/null  | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > /usr/local/share/ca-certificates/dockerio.crt

    update-ca-certificates
```



/etc/ssl/certs/ca-certificates.crt

```
echo -n | openssl s_client -showcerts -connect registry-1.docker.io:443 2>/dev/null  | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' >> /etc/ssl/certs/ca-certificates.crt

root@ks-allinone:/usr/local/share/ca-certificates# docker pull openshift/origin-control-plane:v3.11.0
Error response from daemon: error unmarshalling content: invalid character '<' looking for beginning of value

```

https://www.cnblogs.com/sting2me/p/5596222.html



晕，还是上不了网的问题，公司网络有代理，登录上网权限就ok了。

``` shell
root@ks-allinone:/etc/systemd/system/docker.service.d# minishift start --vm-driver virtualbox --skip-startup-checks
-- Starting profile 'minishift'
The 'minishift' VM is already running.

minishift stop

Login to server ...
Creating initial project "myproject" ...
Server Information ...
OpenShift server started.

The server is accessible via web console at:
     

You are logged in as:
    User:     developer
    Password: <any value>

To login as administrator:
    oc login -u system:admin


```



### 容器启动openshift

```shell
docker run -d --name "origin" \
        --privileged --pid=host --net=host \
        -v /:/rootfs:ro -v /var/run:/var/run:rw -v /sys:/sys -v /var/lib/docker:/var/lib/docker:rw \
        -v /var/lib/origin/openshift.local.volumes:/var/lib/origin/openshift.local.volumes \
        openshift/origin start
```



仍然有报错：

failed to run Kubelet: failed to create kubelet: misconfiguration: kubelet cgroup driver: "systemd" is different from docker cgroup driver



https://my.oschina.net/u/1777269/blog/2243827

``` shell
[root@UVM41 node_exporter-1.0.1.linux-amd64]# docker info
Client:
 Debug Mode: false

Server:
 Containers: 26
  Running: 21
  Paused: 0
  Stopped: 5
 Images: 68
 Server Version: 19.03.4
 Storage Driver: overlay2
  Backing Filesystem: xfs
  Supports d_type: true
  Native Overlay Diff: true
 Logging Driver: json-file
 **Cgroup Driver: systemd**
```



晕，还是访问不了，web访问的时候报503的错误。

