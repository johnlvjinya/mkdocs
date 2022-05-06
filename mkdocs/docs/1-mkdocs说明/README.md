## 安装运行

根据md文件生成文档管理页面，参考

```
https://www.mkdocs.org/getting-started/
```

##### 依赖安装

```
pip install -i https://pypi.douban.com/simple mkdocs
```

##### 创建一个项目

```
mkdocs new my-project
cd my-project
```

##### 项目结构

```
/mmkdocs.yml
配置文件
/docs
所有markdown文件
```

##### 运行

```
mkdocs serve
```

##### 配置主题

/mkdocs.yml

```
site_name: Mydoc
theme:
    name: mkdocs
    nav_style: dark
```



## mkdocs-material主题

##### 安装mkdocs-material

```
pip install -i https://pypi.douban.com/simple mkdocs-material
```

##### 配置主题

/mkdocs.yml

```
site_name: Mydoc
theme:
    name: material

markdown_extensions:
  - admonition
  - codehilite:
      guess_lang: false
      linenums: false
  - toc:
      permalink: true
  - footnotes
  - meta
  - def_list
  - pymdownx.arithmatex
  - pymdownx.betterem:
      smart_enable: all
  - pymdownx.caret
  - pymdownx.critic
  - pymdownx.details
  - pymdownx.emoji:
      emoji_generator: !!python/name:pymdownx.emoji.to_png
  - pymdownx.inlinehilite
  - pymdownx.magiclink
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.superfences
  - pymdownx.tasklist
  - pymdownx.tilde
      
extra_javascript:
    - 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-MML-AM_CHTML'
```

##### 数学公式

然后在mkdocs.yml里添加如下内容，用于导入js

```
extra_javascript:
    - 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-MML-AM_CHTML'
```

##### reference

```
https://cyent.github.io/markdown-with-mkdocs-material/syntax/main/
```

