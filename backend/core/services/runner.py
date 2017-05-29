#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import docker
from requests.exceptions import ReadTimeout

from backend.core.settings import ContainerConfig
from backend.core.utils.uuid import create_uuid

# 保存待执行的源码文件:
class CodeWriter(ContainerConfig):
    def __init__(self, content, file_type, java_class_name=None):
        self.file_name = create_uuid()    # 随机生成
        self.file_type = file_type
        self.java_class_name = java_class_name

        # 保存代码文件
        self.save_code(content)
        # 保存命令
        self.cmd = self.save_cmd()

    @property
    def file_path(self):
        """文件名称+后缀拼接
        
        :return: 
        """
        lang = self.language_support.get(self.file_type)

        if self.java_class_name:
            fp = "{}_{}.{}".format(self.file_name, self.java_class_name, lang)
        else:
            fp = "{}.{}".format(self.file_name, lang)

        return fp

    def save_code(self, content):
        """保存代码文件  
        :param content: 代码内容
        :return: 
        """
        # 文件保存的绝对路径:
        file_path = os.path.join(self.volume_path, self.file_path)

        with open(file_path, mode="w", encoding="utf8") as f:
            f.write(content)

    def save_cmd(self):
        """保存代码执行的 shell 命令
        :return: 
        """
        # 容器中执行文件的绝对路径:
        file_path = os.path.join(self.volume_bind_path, self.file_path)

        cmd = "/bin/bash {0}/{1} {2} {3}/{4} {5} {5}".format(
            self.volume_bind_path,
            self.shell_01,
            self.timeout,
            self.volume_bind_path,
            self.shell_02,
            file_path
        )
        return cmd


# 启动容器:
class ContainerWorker(ContainerConfig):
    """
    源码中关于 volume 的配置参数设置:

        container_id = cli.create_container(
            'busybox', 'ls', volumes=['/mnt/vol1', '/mnt/vol2'],
            host_config=cli.create_host_config(binds={
                '/home/user1/': {
                    'bind': '/mnt/vol2',
                    'mode': 'rw',
                },
                '/var/www': {
                    'bind': '/mnt/vol1',
                    'mode': 'ro',
                }
            })
        )


    """
    def __init__(self, cmd):
        self.client = docker.APIClient()
        # 容器待执行指令:
        self.cmd = cmd

    def create(self):
        #self.cmd = "ls /code-runner"

        # 容器共享 volume 配置参数设置:
        container = self.client.create_container(
            image=self.image_name,
            command=self.cmd,
            volumes=[self.volume_path],    # 只定义了共享目录, 下一个配置中设置目录映射
            host_config=self.client.create_host_config(binds={
                self.volume_path: {
                    'bind': self.volume_bind_path,  # 映射到容器中的路径
                    'mode': self.volume_mode,
                },
            })
        )
        return container

    def run(self):
        ctr = self.create()

        self.client.start(container=ctr.get("Id"))  # 启动容器
        try:
            self.client.wait(container=ctr, timeout=self.timeout)  # 等待执行, 超时判断
        except ReadTimeout as e:
            print("too slow, killed!")
            self.client.kill(container=ctr)  # 超时, kill 掉

        ctr_logs = self.client.logs(container=ctr.get("Id"))
        print(ctr_logs)

        self.client.stop(ctr)  # 退出容器
        self.client.remove_container(ctr, v=True, force=True)  # 清理容器


# 代码执行服务:
class CodeRunner(object):
    def __init__(self, content, file_type, java_class_name=None):
        self.cw = CodeWriter(content, file_type, java_class_name)
        self.cmd = self.cw.cmd
        self.runner = ContainerWorker(self.cmd)

    def run(self):
        return self.runner.run()



if __name__ == '__main__':
    image_name = "daocloud.io/library/gcc:4.9.2"
    code = """

import datetime
import os
print(os.getcwd())
print(datetime.datetime.now())


    """

    code_timeout = """
    
import time
time.sleep(4)
print("can you see me?")

    """

    a = CodeWriter(code, "python")


    runner = CodeRunner(code, "python")
    runner.run()

    # 超时判断:
    runner2 = CodeRunner(code_timeout, "python")
    runner2.run()
