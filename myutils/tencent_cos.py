
# appid 已在配置中移除,请在参数 Bucket 中带上 appid。Bucket 由 BucketName-APPID 组成
# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region
# -*- coding=utf-8
import os
import sys
import csv
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'AKIDZkleguZzmCNXS9D39tTO5XG6hCSW4mCY'  # 替换为用户的 secretId
secret_key = 'LtJwQTKwKYkjZAhz2vZVDfDWlA2hKqBJ'  # 替换为用户的 secretKey
secret_string = '-1257726623'
region = 'ap-shanghai'                  # 替换为用户的 Region
token = None                            # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'                        # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

bucket_name = 'seatable-file'
real_bname = bucket_name+secret_string   # 真实的bucket名称需要加上secret_string
config_cos = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config_cos)               # 获取客户端对象


def get_contained_file_list():              # 获得存储桶下的所有文件夹
    response = client.list_objects(
        Bucket=real_bname,
        Delimiter='/'
    )
    res = response['CommonPrefixes']
    res = [i['Prefix'].rstrip('/') for i in res]
    return res

def get_prefix_file_list(prefix):
    if prefix =='':
        Prefix=''
    else:
        Prefix='%s/'%prefix
    response = client.list_objects(
        Bucket=real_bname,
        Prefix=Prefix
    )

    res = response['Contents']
    for x in res:
        # x.remove('Owner')
        # x.remove('StorageClass')
        x['name'] = x['Key'].replace('%s/'%prefix, '')
        x.pop('Owner', None)
        x.pop('StorageClass', None)
        x.pop('Key', None)
        x['size'] = round(int(x['Size'])/1024**2,1)
        x['url'] = 'https://{0}.cos.ap-shanghai.myqcloud.com/{1}/{2}'.format(real_bname,prefix,x['name'])
    return res


def delete_bucket_file(file_name):                  # bucket_list 需要分析的bucket_列表
    response = client.delete_object(
        Bucket=real_bname,
        Key=file_name
    )
    # print(config.real_bname,'======',  file_name, '======has been deleted')

# def download_bucket_file(file_name):
#     response = client.get_object(
#         Bucket=real_bname,
#         Key=file_name,
#     )
#     response['Body'].get_stream_to_file(file_name)

def upload_bucket_file(local_f_path, cos_f_path):
    with open(local_f_path, 'rb') as fp:
        response = client.put_object(
            Bucket=real_bname,  # 存储桶的名称
            Body=fp,
            Key=cos_f_path,  # 文件名
            # Key=file_path,                # 出现在存储桶中的是个文件夹
            StorageClass='STANDARD',
            EnableMD5=False
        )

if __name__=='__main__':
    res = get_prefix_file_list('')
    print(res)

    delete_bucket_file('论语全译.txt')




    