
import os
import shutil
import config
import myutils.tencent_cos as mtc
import myutils.seatable as msa

mt = msa.MyseaTable(config.st_api_token)


def q_name_from_cos(q_name):
    sql = ''' select name from cos where name='%s' '''%q_name
    res = mt.base.query(sql)
    return res


def upload_from_file(src_file='00_upload'):
    file_list = os.listdir(src_file)
    for f in file_list:
        f_path = os.path.join(src_file, f)
        if os.path.isfile(f_path):
            # print(f)
            mtc.upload_bucket_file(f_path, f)
            os.remove(f_path)
            res = q_name_from_cos(f)
            if not res:  # 如果不存在
                print('uploading.........',f)
                row_data = {
                    'name':f,
                    'url':'https://seatable-file-1257726623.cos.ap-shanghai.myqcloud.com/%s'%f,
                    'cos_delete':'false'
                }
                mt.base.append_row(table_name='cos', row_data=row_data)
            else:
                print('存在,不用插入')


        else:
            shutil.rmtree(f_path)




if __name__=='__main__':
    upload_from_file()








