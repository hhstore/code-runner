#!/usr/bin/env python
# -*- coding: utf-8 -*-


# docker 容器 默认配置项:
class ContainerConfig(object):
    # 容器镜像名:
    image_name = "daocloud.io/library/gcc:4.9.2"

    # 宿主机共享目录:
    volume_path = "/iDockerShare/codebox" #"/code-runner"
    # 映射到容器中的路径:
    volume_bind_path = "/code-runner"  # /code-runner
    volume_mode = "rw"

    shell_01 = "run.sh"
    shell_02 = "run_code.sh"

    # 支持的编程语言:
    language_support = {
        "python": "py",
        "ruby": "rb",
        "c": "c",
        "c++": "cpp",
        "java": "java",
        "go": "go",
        "perl": "pl",
    }

    # 程序执行超时时间:
    timeout = 3
