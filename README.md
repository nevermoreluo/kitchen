# kitchen

默认配置，使用docker compose up 即可启动  
 


### 目的
由于python的web项目不可避免的需要wsgi系列的协议作为部署启动，因此搞了一个all in one的compose，一方面确保更新启动流程固定化，一方面做备忘  


初始化的数据库通过src/.env.template的变量`MYSQL_DATABASE`启动mysql容器时自动创建  
编码集通过my.cnf设定为utf8 

可能需要修改的文件，不用修改文件就能启动，只是配置中有些绑定kitchen这个项目了 其他项目需要修改kitchen的project name
```
# docker compose
docker-compose.yml

# 暴露的端口，以及django的静态文件配置, 我的机器80还有其他用所以配的监听9000了
docker/nginx/nginx.conf

# uwsgi配置，里面定义了kitchen project,通过module=%(project).wsgi:application启动
docker/uwsgi/uwsgi.ini

# 数据库配置， 需要和django.setting的db配置一致
src/.env.template

```


