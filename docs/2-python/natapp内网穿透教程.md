

## 远程桌面



#### 机器A（被控制) 端环境准备

##### natapp启动服务

参考https://blog.csdn.net/youtui/article/details/102647661

```
## 注册使用natapp，采用TCP隧道协议，本地端口选择（一般是3389）
## 下载并，启动服务
natapp -authtoken=442e65c3ff7e8a3e		# 注意换成自己的token
```

##### 允许远程访问

```
“计算机”---“属性”---“远程设置”				# 配置好，允许远程访问
```



#### 机器B（控制端）

```
## win+R输入命令打开远程连接
mstsc 										# 机器B（控制端） windows远程桌面
## 打开natapp机器A查看映射地址，如果账号做了域名映射也可以用映射的地址，本次为
lvjinya.natapp1.cc:41652					# 输入这个地址，就是远程桌面的地址
```

##### 被控制端密码为空的处理

参考：https://jingyan.baidu.com/article/adc815134ce595f723bf7302.html

```
gpedit.msc
【Windows 设置】-【安全设置】-【本地策略】-【安全选项】
点击【安全选项】后，在右侧的窗口里找到【帐户：使用空白密码的本地帐户只允许进行控制台登录】一行，右击，选择【属性】
在弹出属性设置窗口中，选择【已禁用】
然后点击【应用】-【确定】，再关闭组策略。
```



## web服务端口映射

##### 运行

下载natapp.exe，参考主页https://natapp.cn/

```
/natapp.exe
/run.bat
```

进入目录下运行，

```
natapp -authtoken=8d340a67a12dddc9
```



##### 后台运行

新建run.bat

```
if "%1"=="hide" goto CmdBegin
start mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit
:CmdBegin

cd C:\Users\lvjinya\Desktop\p_env_tools_natapp-win64-remote-control
natapp -authtoken=8d340a67a12dddc9
```



##### 开机启动设置

```
复制启动bat文件到
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
```

