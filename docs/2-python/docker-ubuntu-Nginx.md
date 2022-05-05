##### docker

```
Build, Ship and Run
Buildonce，Runanywhere

Docker技术的三大核心概念，分别是：
镜像（Image）容器（Container）仓库（Repository）
镜像---它除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（例如环境变量）。镜像不包含任何动态数据，其内容在构建之后也不会被改变。
仓库---最常使用的Registry公开服务，是官方的Docker Hub，这也是默认的 Registry，并拥有大量的高质量的官方镜像
```

##### K8S

```
将Docker应用于具体的业务实现，是存在困难的——编排、管理和调度等各个方面，都不容易。于是，人们迫切需要一套管理系统，对Docker及容器进行更高级更灵活的管理

一个K8S系统，通常称为一个K8S集群（Cluster）
集群主要包括两个部分：一个Master节点（主节点）一群Node节点（计算节点）
Master节点---主要还是负责管理和控制。
Node节点---是工作负载节点，里面是具体的容器。

Master节点包括API Server、Scheduler、Controller manager、etcd。
API Server是整个系统的对外接口，供客户端和其它组件调用，相当于“营业厅”。
Scheduler负责对集群内部的资源进行调度，相当于“调度室”。
Controller manager负责管理控制器，相当于“大总管”。

Node节点包括Docker、kubelet、kube-proxy、Fluentd、kube-dns（可选），还有就是Pod。
Pod是Kubernetes最基本的操作单元。一个Pod代表着集群中运行的一个进程，它内部封装了一个或多个紧密相关的容器。除了Pod之外，K8S还有一个Service的概念，一个Service可以看作一组提供相同服务的Pod的对外访问接口。这段不太好理解，跳过吧。
Docker，不用说了，创建容器的。
Kubelet，主要负责监视指派到它所在Node上的Pod，包括创建、修改、监控、删除等。
Kube-proxy，主要负责为Pod对象提供代理。
Fluentd，主要负责日志收集、存储与查询。


```

查看ubuntu版本

```
cat /proc/version
```



##### 1.安装docker

https://www.cnblogs.com/kingsonfu/p/11576797.html

参考其中的离线安装模式

```
-下载
wget https://download.docker.com/linux/static/stable/x86_64/docker-18.06.3-ce.tgz

-解压
tar -zxvf docker-18.06.3-ce.tgz

-复制
cp docker/* /usr/bin/
```

##### 2注册service服务

在/etc/systemd/system/目录下新增docker.service文件**，内容如下，这样可以将docker注册为service服务

```
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target firewalld.service
Wants=network-online.target
  
[Service]
Type=notify
# the default is not to use systemd for cgroups because the delegate issues still
# exists and systemd currently does not support the cgroup feature set required
# for containers run by docker
ExecStart=/usr/bin/dockerd --selinux-enabled=false --insecure-registry=127.0.0.1
ExecReload=/bin/kill -s HUP $MAINPID
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
# Uncomment TasksMax if your systemd version supports it.
# Only systemd 226 and above support this version.
#TasksMax=infinity
TimeoutStartSec=0
# set delegate yes so that systemd does not reset the cgroups of docker containers
Delegate=yes
# kill only the docker process, not all processes in the cgroup
KillMode=process
# restart the docker process if it exits prematurely
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s
  
[Install]
WantedBy=multi-user.target
```

此处的--insecure-registry=127.0.0.1（此处改成你私服ip）设置是针对有搭建了自己私服Harbor时允许docker进行不安全的访问，否则访问将会被拒绝。

**3 启动docker**

给docker.service文件添加执行权限

```
chmod +x /etc/systemd/system/docker.service 
```

重新加载配置文件（每次有修改docker.service文件时都要重新加载下）

```
systemctl daemon-reload                
```

启动

```
systemctl start docker
```

设置开机启动

```
systemctl enable docker.service
```

查看docker服务状态

```
systemctl status docker
netstat -anp |grep 80
```



##### 获取Nginx镜像

```
获取Nginx镜像：docker pull nginx
查看Nginx镜像是否获取成功: docker images

```



##### docker配置和部署项目Nginx

```

在本机8081端口运行Nginx服务器(默认配置)
docker run \
-d \
-p 4200:80 \
--rm \
--name mynginx \
--volume "/lvf/gantt-demo/scheduling.dist":/usr/share/nginx/html \
nginx

注意：4200:80表示开放4200端口，替代默认的80端口，/lvf/gantt-demo/scheduling.dist为项目的路径
运行命令后会生成一个容器ID，本次为：efe5de985fbb5c2f5057cb6da9342fbcb20f7a6650a7558c458b381fd4638f51
查看docker:  docker ps

问题1：如果容器名称被占用了，怎么修改
docker rm -f mynginx
docker network disconnect --force
docker network inspect
```



其他命令：

```
查看docker:  docker ps
进入容器： docker exec -it react1 /bin/bash （react1为容器的名称NAMES字段）
退出容器：exit
结束容器：docker stop a1b0b9f49b99   
删除容器：docker rm 容器id（可以通过 docker ps查看， 本次为：docker rm a1b0b9f49b99 ）

彻底删除容器,xx为容器ID: docker rm -f xxx (本次为 docker rm -f a1b0b9f49b99  )
docker network disconnect --force
docker network inspect 
```

