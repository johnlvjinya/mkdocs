import config
import pandas as pd
import myutils.seatable as msa
from seatable_api.constants import ColumnTypes
import myutils.tencent_cos as mtc

mt = msa.MyseaTable(config.st_api_token)

#################################################################### 新建表格
add_dict = {
    'name': [ColumnTypes.TEXT, 300],  # 列属性和宽度
    'note_file': [ColumnTypes.FILE, 100],
    'url': [ColumnTypes.URL, 20],
    'cos_delete': [ColumnTypes.SINGLE_SELECT, 60],
    # 'class_tree':[ColumnTypes.SINGLE_SELECT,150],
}

exists_tb_list = mt.get_sub_tb_list()
create_tb_list = 'cos'.split(',')  ###### seatable需要创建的表格

for f in create_tb_list:
    if f not in exists_tb_list:
        mt.base.add_table(f, lang='zh-cn')

    cols_list = [x.get('name') for x in mt.base.list_columns(f)]
    for k, v in add_dict.items():
        if k not in cols_list:
            mt.base.insert_column(table_name=f,
                                  column_name=k,
                                  column_type=v[0],
                                  column_key=None,
                                  column_data=None)
        mt.base.resize_column(table_name=f,
                              column_key=k,
                              new_column_width=v[1])
        if k == 'cos_delete':
            mt.base.add_column_options(f, k, [
                {
                    "name": "true",
                    "color": "#EE30A7",
                    "textColor": "#000000"
                },
                {
                    "name": "false",
                    "color": "#C1FFC1",
                    "textColor": "#000000"
                },
            ])

#################################################################### 删除数据

rows = mt.base.list_rows('cos',
                         view_name=None,
                         order_by=None,
                         desc=False,
                         start=None,
                         limit=None)
df = pd.DataFrame(rows)
# df.to_excel('test.xlsx', index=False)
df = df[df['cos_delete'] == 'true'].reset_index(drop=True)
for i, r in df.iterrows():
    # print(r['name'])
    try:
        mt.base.delete_row('cos', r['_id'])
        mtc.delete_bucket_file(r['name'])
    except Exception as e:
        print(e)
