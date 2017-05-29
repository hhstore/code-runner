# code-runner
基于 Flask, Docker 实现的在线编程网站.

## 依赖:





## 本地运行:

### 1. 拉取依赖的 docker 容器:

- [daocloud - gcc:4.9.2 镜像](https://hub.daocloud.io/repos/9bd717cf-7e5b-4943-843a-1c9104cb596f)
- [配置 Docker 加速器](https://www.daocloud.io/mirror#accelerator-doc)


```bash 

docker pull daocloud.io/library/gcc:4.9.2


```


## 项目架构:


- 前端:
    - bootstrap
    - codemirror
    - vue.js

- 后端:
    - flask
    - docker


## 前端初始化:

```bash

#   vue-cli · Generated "frontend".
#   To get started:
   
cd frontend
npm install
npm run dev



```

## 参考:

- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/)

- [about docker run ](https://github.com/docker/docker-py/issues/933)






