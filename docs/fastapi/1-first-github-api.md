# 第一个Github API


## 三行代码的一个API

```shell script
from fastapi import FastAPI

app = FastAPI()


@app.get("/github/{repo_name}")
def get_github_repo_status(repo_name):
    return {"repo_name": repo_name}

```

## 运行api

```shell script
uvicorn main:app --reload
```

## 使用swagger或者redoc 调用api

访问:
http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/doc

就可以从页面上调用API

## 完成想要的获取github信息的接口

- 使用pygithub
- 获取需要的github信息返回json或者yml格式


## 使用api router 重构API

- 为什么使用API router
- 如何重构

