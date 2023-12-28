## Flask App

### demo01-flask

```shell
docker-compose up -d

docker-compose ps

docker-compose down

docker-compose up -d --build
```

> http://localhost:5000

### demo02-flask-redis

```shell
docker-compose up -d
```

> http://localhost:5000

### demo03-flask-scale

正常启动一个

```shell
docker-compose up -d
```

扩展3个web服务，并且用nginx代理

```shell
docker-compose up -d --build --scale web=3
```

测试

```shell
for i in {1..30}; do curl http://localhost:1080; done
```
