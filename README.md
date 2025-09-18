#### celery 启动
```shell
celery -A app.mycelery worker --loglevel=info -P gevent
```