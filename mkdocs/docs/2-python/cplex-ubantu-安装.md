



##### 下载cplex-bin文件复制到指定目录下

```
文件路径： /lvf/cplex_install_bin_file
文件名： cplex_studio1210.linux-x86-64.bin
```



##### 安装bin文件

```
# putty cd进入文件路径后获得权限
udo chmod u+x cplex_studio1210.linux-x86-64.bin
# 安装
sudo ./cplex_studio1210.linux-x86-64.bin
# 选择英文，以及其他要求
# 选择安装路径
本次选择：/lvf/cplex_install_bin_file/install_path
```

##### 添加环境变量

添加环境变量，本次oplrun命令在如下路径下/lvf/cplex_install_bin_file/install_path/opl/bin/x86-64_linux

```
# Xftp进入/etc用sublimetext打开profile文件

# 在最后添加
export PATH=/lvf/cplex_install_bin_file/install_path/opl/bin/x86-64_linux:$PATH

# putty cmd进入etc文件路径下
source profile

# 测试oplrun,运行测试，复制MODEL.mod文件和Data.dat文件，oplrun运行测试
```



