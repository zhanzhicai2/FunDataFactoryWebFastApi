# encoding: utf-8
# @File  : create_key.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/09/10

import paramiko
from config import FilePath


def generate_ssh_key():
    key = paramiko.RSAKey.generate(4096)
    # 私钥生成
    key.write_private_key_file(FilePath.RSA_PRI_KEY)
    # 公钥生成
    rsa_pub_key = f"{key.get_name()} {key.get_base64()} FunDataFactory"
    with open(FilePath.RSA_PUB_KEY, 'w') as f:
        f.write(rsa_pub_key)


if __name__ == '__main__':
    generate_ssh_key()
