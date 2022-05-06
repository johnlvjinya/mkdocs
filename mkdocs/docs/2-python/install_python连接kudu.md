





**impala依赖**

```
six
bit_array
thrift
thrift_sasl
pandas(不装应该也可以) 
sqlalchemy 
pytest（不装应该也可以）
```



##### 安装次序

```
pip install -i https://pypi.douban.com/simple impala
pip install -i https://pypi.douban.com/simple impyla

安装impyla报错
提示vc 14++报错：安装visual studio
再提示报错：用whl装bit_array
```



##### 测试代码

```

from impala.dbapi import connect


def get_data():
    result_data = []

    conn = connect(host='101.132.107.216', port=21050)
    cur = conn.cursor()

    cur.execute('use kudu_pro;')
    query_sql = "select at_filepath  from attachment where at_subtype = '207003' and at_identifier is not null limit 100"
    cur.execute(query_sql)
    data_list = cur.fetchall()
    for data in data_list:
        result_data.append(str(data).replace("('", '').replace("',)", '').replace('/upload/', '/data/oms_upload/'))
    conn.close()

    return result_data
print(get_data() )


```

