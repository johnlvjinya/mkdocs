
import os
import config
import shutil
import requests
import numpy as np
import pandas as pd
import myutils.tencent_cos as mtc
import myutils.seatable as msa

mt = msa.MyseaTable(config.st_api_token)

def get_file_by_url(f_url, save_path = 'temp/temp.png'):
    mt.base.download_file(f_url, save_path=save_path)

def refresh_seatable_md():  # 新建cos文档的md文件
    rows = mt.base.list_rows('cos')
    df = pd.DataFrame(rows).sort_values('名称').reset_index(drop=True)
    df.fillna(0,inplace=True)#替换为0
    if df.shape==0:
        return
    last_t = 'start111'
    appear_list = []
    try:shutil.rmtree('mkdocs\\docs')
    except:pass
    os.makedirs('mkdocs\\docs')

    with open('mkdocs/docs/index.md', 'w', encoding='utf-8') as fp:
        
        for i,r in df.iterrows():
            if r['名称']==last_t: # 不用增加标题
                pass  
            else:       # 增加标题
                try:
                    tree_i_list = str(r['名称']).split('-')
                except:
                    print(r['名称'])

                for index_j,t_j in enumerate(tree_i_list):
                    if t_j not in appear_list:
                        fp.write('##'+'#'*index_j+' '+t_j)
                        fp.write('\n')
                        appear_list.append(t_j)
            ########## 插入链接
            fp.write('[%s](%s)'%(r['name'], r['url']))
            fp.write('\n\n')
            last_t = r['名称']

            ############ 保存md文件
            save_path = os.path.join('mkdocs\\docs', str(r['名称']).split('-')[0])

            file_type = r['name'].split('.')[-1]
            if file_type=='md':
                if os.path.exists(save_path) is False:
                    os.makedirs(save_path)

                file_path = os.path.join(save_path, r['name'])
                rsp = requests.get(r['url']) # 发送请求
                with open (file_path, 'wb') as f:
                    f.write(rsp.content)

            ################ 下载seatable的文件
            if r['note_file']!=0:  ############## 存在备注文件
                print('yess', r['note_file'])
                for st_f in r['note_file']:
                    st_f_type = st_f['name'].split('.')[-1]
                    if st_f_type=='md':
                        file_path = os.path.join(save_path, st_f['name']) 
                        if os.path.exists(save_path) is False:
                            os.makedirs(save_path)

                        get_file_by_url(f_url=st_f['url'], save_path = file_path)

    df.to_excel('temp/last_files.xlsx', index=False)


if __name__=='__main__':
    refresh_seatable_md()