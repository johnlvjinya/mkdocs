
import os
import config
import pandas as pd
import myutils.tencent_cos as mtc
import myutils.seatable as msa

mt = msa.MyseaTable(config.st_api_token)

def refresh_seatable_md():  # 新建cos文档的md文件
    rows = mt.base.list_rows('cos')
    df = pd.DataFrame(rows).sort_values('名称').reset_index(drop=True)
    if df.shape==0:
        return
    last_t = 'start111'
    appear_list = []
    with open('mkdocs/docs/index.md', 'w', encoding='utf-8') as fp:
        for i,r in df.iterrows():
            if r['名称']==last_t: # 不用增加标题
                pass  
            else:       # 增加标题
                tree_i_list = r['名称'].split('-')

                for index_j,t_j in enumerate(tree_i_list):
                    if t_j not in appear_list:
                        fp.write('##'+'#'*index_j+' '+t_j)
                        fp.write('\n')
                        appear_list.append(t_j)
            ########## 插入链接
            fp.write('[%s](%s)'%(r['name'], r['url']))
            fp.write('\n\n')
            last_t = r['名称']



    df.to_excel('temp/last_files.xlsx', index=False)


    pass


if __name__=='__main__':
    refresh_seatable_md()