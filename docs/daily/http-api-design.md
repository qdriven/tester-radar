# 0.HTTP API Design

关于HTTP API Design的翻译，
参考[http-api-design](https://github.com/interagent/http-api-design.git)

## 1. HTTP API 设计基础

- 分解关注点
- 安全请求:
  * https
  * 不鼓励Redirect
- 版本放在HTTP Header里面
```sh 
Accept: application/vnd.heroku+json; version=3

```
- etags作为缓存支持
- 提供request id用来追踪请求信息
- 根据请求范围分解超大的响应 - Range Header

## 2. 请求

- 请求包体使用JSON格式
```sh 
$ curl -X POST https://service.com/apps \
    -H "Content-Type: application/json" \
    -d '{"name": "demoapp"}'

{
  "id": "01234567-89ab-cdef-0123-456789abcdef",
  "name": "demoapp",
  "owner": {
    "email": "username@example.com",
    "id": "01234567-89ab-cdef-0123-456789abcdef"
  },
  ...
}
```
- 资源名称
- 对资源的动作或者操作
```shell
/resources/:resource/actions/:action
/runs/{run_id}/actions/stop
/actions/:action/resources
/actions/restart/servers
```
- 提供一致性是的路径格式
- 资源路径都是小写
```shell
service-api.com/users
```
- 最小化路径嵌套
```sh 
/orgs/{org_id}/apps/{app_id}/dynos/{dyno_id}
```

to:

```sh 
/orgs/{org_id}
/orgs/{org_id}/apps
/apps/{app_id}
/apps/{app_id}/dynos
/dynos/{dyno_id}
```

- 支持non-id

```shell
$ curl https://service.com/apps/{app_id_or_name}
$ curl https://service.com/apps/97addcf0-c182
$ curl https://service.com/apps/www-prod
```

## 3. Response

- 合适的status code
  * 200: GET, POST, DELETE, or PATCH 
  * 201: POST/PUT创建一个资源成功,同步
  * 202: 异步
  * 206： GET，部分返回
  * 401: Unauthorized, 用户没有被授权
  * 403: 用户没有权限
  * 429: 请求数量太多
  * 500: 服务端报错
- 时间问题格式:UTC times formatted in ISO8601
- 获取结果错误
- 保持JSON最小化

## 产出物

- 提供机器可读的JSON文件
- 提供人类可读的文档
- 提供可执行的例子
- 接口稳定的描述，向后兼容
