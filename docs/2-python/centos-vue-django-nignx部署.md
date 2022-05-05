### centos登陆

##### 1.1 工具准备

```
1.PuTTY
https://www.chiark.greenend.org.uk/~sgtatham/putty/
2.Xftp
链接：https://pan.baidu.com/s/1UHT9FIiqZYu5cE4k9xqMYA 提取码：76ym
```

##### 1.2 登陆

```
1.Putty登录
host name: 175.24.90.248, port:22, SSH
超时设置：https://blog.csdn.net/qq_38461388/article/details/107281199

2.Xftp登陆
主机:175.24.90.248, 用户名root,协议SFTP,端口:22
```

##### 1.3 putty常见命令

```
cd /home		进入'/home'目录'
cd ..			返回上一级目录
cd ../..		返回上两级目录
pwd				显示工作目录
ls				显示当前目录的所有子文件
mkdir dir1		创建一个叫做'dir1'的目录'
mkdir -p/tmp/dir1/dir2				创建一个目录树
rm-rf dir1							删除一个叫做'dir1'的目录并同时删除其内容
ls -lh								显示权限
python –V   python3 –V				检查python版本

```

### 新系统的准备

##### 2.1 组织文件

对于一个新系统，在root文件夹下新建一些文件用于组织文件

```
---/root
------lvjinya
---------mydownload
---------myinstall
---------myfiles
```

##### 2.2 库环境准备

yum install gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel  gcc-c++ intltool -y



### 安装mwget

mwget对比wget为多线程下载

参考： https://www.jianshu.com/p/e420439f86fe 

```
1. 安装
mkdir -p /root/lvjinya/mydownload			# 创建下载目录
cd /root/lvjinya/mydownload					# 进入下载目录
wget http://jaist.dl.sourceforge.net/project/kmphpfm/mwget/0.1/mwget_0.1.0.orig.tar.bz2
tar -xjvf mwget_0.1.0.orig.tar.bz2			# 解压
cd mwget_0.1.0.orig							# 进入解压目录
mkdir -p /root/lvjinya/myinstall/mwget						# 创建安装目录
./configure -prefix=/root/lvjinya/myinstall/mwget		# 安装到指定目录
make && make install 			 			# 如有异常参考页面，如无异常执行编译

2. 添加环境变量（对所有系统用户生效，永久生效）
## 参考：https://blog.csdn.net/f110300641/article/details/82663132
## 修改 /etc/profile 文件，在文件末尾加上如下两行代码 
PATH=$PATH:/root/lvjinya/myinstall/mwget/bin 
export PATH
## 最后执行命令 
source /etc/profile		# 刷新配置

mwget -v				# 查看是否安装成功

```



### 安装python3

参考： https://www.cnblogs.com/adidasshe/p/11904720.html 

```

1. 安装
cd /root/lvjinya/mydownload						# 进入下载目录
mwget https://www.python.org/ftp/python/3.7.7/Python-3.7.7.tgz		# 多线程下载
tar zxvf Python-3.7.7.tgz						# 解压文件
cd Python-3.7.7									# 进入解压文件
mkdir -p /root/lvjinya/myinstall/python3		# 创建安装目录
./configure --prefix=/root/lvjinya/myinstall/python3				# 安装到指定位置
make && make install							# 安装

2. 添加环境变量
## 修改 /etc/profile 文件，在文件末尾加上如下两行代码 
PATH=$PATH:/root/lvjinya/myinstall/python3/bin 		
export PATH				
## 最后执行命令 
source /etc/profile		# 刷新配置
python3 -V				# 查看是否成功

```



### git的安装和使用

##### git安装

```
cd /root/lvjinya/mydownload								# 进入下载目录
mwget https://www.kernel.org/pub/software/scm/git/git-2.19.2.tar.gz		# 多线程下载
tar -xzvf git-2.19.2.tar.gz								# 解压文件
ls														# 查看解压文件名称
cd git-2.19.2											# 进入解压文件
mkdir -p /root/lvjinya/myinstall/git					# 创建安装目录
./configure --prefix=/root/lvjinya/myinstall/git		# 安装到指定位置
make && make install									# 安装

2. 添加环境变量
## 修改 /etc/profile 文件，在文件末尾加上如下两行代码 
PATH=$PATH:/root/lvjinya/myinstall/git/bin 		
export PATH				
## 最后执行命令
source /etc/profile		# 刷新配置
git --version			# 查看是否成功
```



##### 代码克隆

```
cd /root/lvjinya/myfiles			# 进入本人文件目录
git clone https://github.com/johnlvjinya/vue-django-template-table.git		# 克隆项目
```

##### 服务器更新代码

##服务器通过以下命令可以把仓库的代码copy过来，覆盖本地修改

```
git fetch --all
git reset --hard origin/master
git pull
```



### django项目部署

##### 安装sqlite3

如果项目依赖sqlite3，却没有安装，参考以下

注意去 https://www.sqlite.org/download.html  下载最新版本的sqlite, 复制链接地址

```
# 安装最新版本
cd /root/lvjinya/mydownload										# 进入下载目录
mwget https://www.sqlite.org/2020/sqlite-autoconf-3320300.tar.gz		# 注意版本
tar xvzf sqlite-autoconf-3320300.tar.gz							# 解压文件
cd sqlite-autoconf-3320300										# 进入解压文件
./configure --prefix=/usr/local
make && make install

# 替换系统低版本 sqlite3
mv /usr/bin/sqlite3  /usr/bin/sqlite3_old
ln -s /usr/local/bin/sqlite3   /usr/bin/sqlite3
echo "/usr/local/lib" > /etc/ld.so.conf.d/sqlite3.conf
ldconfig
sqlite3 -version

```



##### 项目的运行环境

如果虚拟环境和依赖包没有准备好，参考以下

注意: 豆瓣源安装，**注意是pip3**

```
1. 虚拟环境
pip3 install -i https://pypi.douban.com/simple virtualenv   # 安装虚拟环境
cd /root/lvjinya/myfiles									# 本文文件目录
virtualenv djangoenv										# 创建虚拟环境
source /root/lvjinya/myfiles/djangoenv/bin/activate					# 激活环境

2. 依赖包(根据需要)
pip3 install -i https://pypi.douban.com/simple django
pip3 install -i https://pypi.douban.com/simple django-cors-headers
pip3 install -i https://pypi.douban.com/simple djangorestframework
```



##### 启动后端

保证：1. 运行环境OK, 2. 保证项目克隆后。启动后端，参考如下

```
1. 启动代码
cd /root/lvjinya/myfiles/vue-django-template-table/mybackend  # manage.py所在的目录
python3 manage.py runserver								## 正常模式， 挂机就没了
nohup python3 manage.py runserver 0.0.0.0:8000 &		## nohup模式
lsof -i:8000											## 检查8000端口是否启动
http://175.24.90.248:8000/app01/getsuperuser			## 发送get请求，看是否成功（参考）


2. 问题备注：
### 端口占用的问题，查询解除8000端口占用
lsof -i:8000， kill -9 24194(PID)
参考：https://cloud.tencent.com/developer/article/1452924

### 8000端口启动失败的问题
python3 manage.py runserver		# 使用正常模式启动查看
```

##### 



### 安装nginx

安装参考  https://my.oschina.net/yueshengwujie/blog/3099219 

##### 库环境依赖

```
yum install gcc-c++ pcre pcre-devel zlib zlib-devel openssl openssl-devel -y
```



##### 安装nginx



```
1. 安装
cd /root/lvjinya/mydownload					# 进入下载目录
mwget https://nginx.org/download/nginx-1.18.0.tar.gz
tar -zxvf nginx-1.18.0.tar.gz				# 解压
### 如果解压报错，可能是下载的文件有问题，需要删除文件再重新下载，如果速度太慢就用windows下载
### windows下载地址 https://github.com/nginx/nginx/releases/tag/release-1.18.0 注意版本
cd nginx-1.18.0							# 进入解压目录
mkdir -p /root/lvjinya/myinstall/nginx					# 创建安装目录
./configure --prefix=/root/lvjinya/myinstall/nginx		# 安装到指定目录
make && make install 			 			# 如有异常参考页面，如无异常执行编译

2. 添加环境变量（对所有系统用户生效，永久生效）
## 修改 /etc/profile 文件，在文件末尾加上
export PATH=$PATH:/root/lvjinya/myinstall/nginx/sbin 
## 最后执行命令 
source /etc/profile		# 刷新配置


#启动、停止nginx
cd /root/lvjinya/myinstall/nginx/sbin/
./nginx     #启动
./nginx -s stop  #停止，直接查找nginx进程id再使用kill命令强制杀掉进程
./nginx -s quit  #退出停止，等待nginx进程处理完任务再进行停止
./nginx -s reload  #重新加载配置文件，修改nginx.conf后使用该命令，新配置即可生效

#重启nginx，建议先停止，再启动
./nginx -s stop
./nginx

#查看nginx进程，如下返回，即为成功
[root@VM_0_12_centos ~]# ps aux|grep nginx
root      5984  0.0  0.0 112708   976 pts/1    R+   14:41   0:00 grep --color=auto nginx
root     18198  0.0  0.0  20552   612 ?        Ss   11:28   0:00 nginx: master process ./nginx
nobody   18199  0.0  0.0  23088  1632 ?        S    11:28   0:00 nginx: worker process
```



##### nginx的原理

参考： https://blog.csdn.net/wangbiao007/article/details/82910709 





### 安装nodejs

参考：  https://www.cnblogs.com/zhi-leaf/p/10979629.html 

```
1. 安装
cd /root/lvjinya/mydownload						# 进入下载目录
mwget https://nodejs.org/dist/v12.18.3/node-v12.18.3-linux-x64.tar.xz
## 注意如果网速不好就用windows下载然后放到mydownload目录下
tar -xvf node-v12.18.3-linux-x64.tar.xz			# 解压文件			
cd node-v12.18.3-linux-x64						# 进入解压文件
mkdir -p /root/lvjinya/myinstall/nodejs 		# 创建安装目录
cd /root/lvjinya/myinstall/nodejs				# 进入安装的目录
mv /root/lvjinya/mydownload/node-v12.18.3-linux-x64 .  # 后面的.表示移动到当前目录


2. 添加环境变量
## 修改 /etc/profile 文件，在文件末尾加上如下代码 
export PATH=$PATH:/root/lvjinya/myinstall/nodejs/node-v12.18.3-linux-x64/bin
## 最后执行命令 
source /etc/profile		# 刷新配置
node -v
npm -v					# 查看是否成功

```



### vue项目环境安装

##### 安装依赖包

```
cd /root/lvjinya/myfiles/vue-django-template-table/myfrontend	# 进入前端目录
npm config set registry https://registry.npm.taobao.org    		# 设置淘宝源
npm install   			# 安装
```

##### 生成dist文件夹

```
npm run build:prod  # 这条命令会生成一个dist文件夹
```



##### 修改nginx配置文件

```
参考： https://www.cnblogs.com/mengxiaoleng/p/12952371.html 
## 配置地址
/root/lvjinya/myinstall/nginx/conf 
```

参考：

```

user root;			# 查看用户名
worker_processes  1;
events {
    worker_connections  1024;
}
http {
        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;
        access_log /root/lvjinya/myfiles/vue-django-template-table/myfrontend/access.log;
        error_log /root/lvjinya/myfiles/vue-django-template-table/myfrontend/error.log;
        gzip on;
        server {
                listen 8088;                          #1.你想让你的这个项目跑在哪个端口
                server_name 175.24.90.248;            #2.当前服务器ip
                location / {
                    root   /root/lvjinya/myfiles/vue-django-template-table/myfrontend/dist/;     #3.dist文件的位置
                    try_files $uri $uri/index.html;     #4.重定向,内部文件的指向(照写)
                    }
      
            }
            
		# 参考 https://blog.csdn.net/m0_37904728/article/details/78745243
		include /root/lvjinya/myinstall/nginx/conf/mime.types;		# 根据mime.types保证css文件解析
		default_type application/octet-stream;
}
```



##### 启动服务

```
# 重启nginx，建议先停止，再启动
nginx -s stop			# 结束进程
ps aux|grep nginx		# 查看是否成功
/root/lvjinya/myinstall/nginx/sbin/nginx -c /root/lvjinya/myinstall/nginx/conf/nginx.conf
```



##### 查看vue首页

 http://175.24.90.248:8088/ 



### 调试的注意点

打开浏览器network, disabled cache

检查network相关的文件没有加载

检查console

##### css文件加载成功但样式不对

浏览器console出现警告， 说明css文件没有被正常解析

```
 Resource interpreted as Stylesheet but transferred with MIME type text/plain
```

nginx配置后重启

```
# 参考 https://blog.csdn.net/m0_37904728/article/details/78745243
include /root/lvjinya/myinstall/nginx/conf/mime.types;    # 根据mime.types保证css文件解析
default_type application/octet-stream;
```

后端api数据

```
检查数据库，检查api等等
```





