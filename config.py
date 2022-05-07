
import os

file_list = '00_upload,temp'.split(',')
for f in file_list:
    if os.path.exists(f) is False:
        os.mkdir(f)


###### seatable表格token
st_api_token = '0bfd623fc845592c776d8c35e2f24ae69cf3eb53'
server_url='https://cloud.seatable.cn'