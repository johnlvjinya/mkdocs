### python 安装

##### 安装

进入安装包，点击安装，注意**真实的安装路径**

```
安装包下载
链接：https://pan.baidu.com/s/1X20bcqsvmNygpOQEoU58Sg 
提取码：unan
```

##### 环境变量

```
# 安装完成后，添加环境变量（注意根据变化改变，本次安装路径为D:\python\python3.7.7）
D:\python\python3.7.7
D:\python\python3.7.7\Scripts
```

##### 环境变量

```
# 升级Pip
python -m pip install --upgrade pip

# 安装pandas，其他包类似
pip3 install -i https://pypi.douban.com/simple pandas
pip3 install -i https://pypi.douban.com/simple xlrd
pip3 install -i https://pypi.douban.com/simple matplotlib
```



### Sublime Text3 安装配置

##### 安装

进入安装包，点击安装

##### 激活

Help--Enter License--输入激活码

```
----- BEGIN LICENSE -----
Member J2TeaM
Single User License
EA7E-1011316
D7DA350E 1B8B0760 972F8B60 F3E64036
B9B4E234 F356F38F 0AD1E3B7 0E9C5FAD
FA0A2ABE 25F65BD8 D51458E5 3923CE80
87428428 79079A01 AA69F319 A1AF29A4
A684C2DC 0B1583D4 19CBD290 217618CD
5653E0A0 BACE3948 BB2EE45E 422D2C87
DD9AF44B 99C49590 D2DBDEE1 75860FD2
8C8BB2AD B2ECE5A4 EFC08AF2 25A9B864
------ END LICENSE ------
```

注意一段时间后，这个激活码可能失效，请使用新的激活码，如搜不到考虑使用激活软件。

##### 设置不更新

Preferences--Settings

 在花括弧中添加:"update_check":false ，如下所示

```
{
	"expand_tabs_on_save": true,
	"font_size": 13,
	"ignored_packages":
	[
		"Vintage"
	],
	"tab_size": 4,
	"translate_tabs_to_spaces": true,
	"update_check": false
}

```

##### 安装SublimeREPL

```
# 按住进入
Shift+Ctrl+P
# 查找安装，可能延时
Package Control: Install Packaage 
# 搜索SublimeREPL，点击安装
SublimeREPL
# 查看是否安装成功
Preferences--Package Settings--出现SublimeREPL选项
```

##### F5运行

Preferences -- Key Bindings --修改为如下代码

```
[
    {
        "keys": ["f5"],
        "caption": "SublimeREPL: Python - RUN current file",
        "command": "run_existing_window_command",
        "args": {
            "id": "repl_python_run",
            "file": "config/Python/Main.sublime-menu",
        }
    },

    {
        "keys": ["ctrl+f5"],
        "caption": "SublimeREPL: Python - PDB current file",
        "command": "run_existing_window_command",
        "args": {
            "id": "repl_python_pdb",
            "file": "config/Python/Main.sublime-menu"
        }
    },
]
```





