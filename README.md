# code-runner
基于 Flask, Docker 实现的在线编程网站.



## 项目依赖:

- 前端:
    - vue.js
    - [CodeMirror](http://codemirror.net/demo/theme.html)
    - [vue-codemirror](https://github.com/surmon-china/vue-codemirror)
        - [vue-codemirror: 文档](https://surmon-china.github.io/vue-codemirror/)
- 后端:
    - [docker-py](https://github.com/docker/docker-py)
        - [文档](https://docker-py.readthedocs.io/en/stable/)
    - [Pika](https://github.com/pika/pika)
    - [celery](https://github.com/celery/celery)
    - flask
    - docker

## 开发环境搭建:



### 1. 前端环境初始化:

```bash

#   vue-cli · Generated "frontend".
#   To get started:
   
cd frontend
npm install
npm run dev


```

### 2. 拉取 docker 容器:

- [daocloud - gcc:4.9.2 镜像](https://hub.daocloud.io/repos/9bd717cf-7e5b-4943-843a-1c9104cb596f)
- [配置 Docker 加速器](https://www.daocloud.io/mirror#accelerator-doc)


```bash 

docker pull daocloud.io/library/gcc:4.9.2


```

### 3. 运行项目后台服务:

```bash 
# server:

python 

```



## 参考:

- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/)
- [about docker run ](https://github.com/docker/docker-py/issues/933)






