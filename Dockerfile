FROM python:3.10-slim

ARG APP_HOME

RUN sed -i 's#http://deb.debian.org#https://mirrors.ustc.edu.cn#g' /etc/apt/sources.list.d/debian.sources &&\
    sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list.d/debian.sources


RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		default-mysql-client \
        libmariadb-dev-compat \
        libpq-dev \
        postgresql-client \
        net-tools \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

MAINTAINER Nevermore

# 设置 python 环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR $APP_HOME
ENV PATH $PATH:$APP_HOME
ENV TZ="Asia/Shanghai"

COPY ./src/requirements.txt $APP_HOME/requirements.txt
COPY ./docker/docker-entrypoint.sh /opt/docker-entrypoint.sh

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ &&\
    pip config set install.trusted-host mirrors.aliyun.com &&\
    /usr/local/bin/python -m pip install --upgrade pip &&\
    cd $APP_HOME &&\
    pip install -r requirements.txt &&\
    pip install uwsgi &&\
    sed -i 's/\r//' /opt/docker-entrypoint.sh && \
    chmod +x /opt/docker-entrypoint.sh

ENTRYPOINT ["/opt/docker-entrypoint.sh"]

