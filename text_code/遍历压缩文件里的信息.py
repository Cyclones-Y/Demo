import zipfile
import chardet

zipfile_path = '/mnt/e/投标测试文件.zip'

# 打开压缩文件
with zipfile.ZipFile(zipfile_path, 'r') as zip_file:
    for file in zip_file.infolist():
        encode_file = file.filename.encode('cp437')
        print(encode_file)
        encode_file_1 = chardet.detect(encode_file)['encoding']
        print(encode_file.decode(encode_file_1))