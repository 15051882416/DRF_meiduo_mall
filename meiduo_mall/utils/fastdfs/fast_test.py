from fdfs_client.client import Fdfs_client

# 创建FastDFS客户端
client = Fdfs_client("./client.conf")

# 使用FastDFS客户端上传文件（图片）
ret = client.upload_by_filename("/home/python/Desktop/upload_Images/kk02.jpeg")
print(ret)

"""
ret = {'Group name': 'group1', 
'Remote file_id': 'group1/M00/00/00/wKhvl1zuV_OAB1wqAAEXU5wmjPs10.jpeg',
 'Status': 'Upload successed.', 
 'Local file name': '/home/python/Desktop/upload_Images/kk02.jpeg', 
 'Uploaded size': '69.00KB', 
 'Storage IP': '192.168.111.151'}


ret = {
'Group name': 'Storage组名',
'Remote file_id': '文件索引，可用于下载',
'Status': '文件上传结果反馈',
'Local file name': '上传文件全路径',
'Uploaded size': '文件大小',
'Storage IP': 'Storage地址'
 }
 
"""
