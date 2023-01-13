FROM python:3.10-slim

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

ENV APP_HOME=/opt/kitchen

WORKDIR $APP_HOME
ENV PATH $PATH:$APP_HOME
ENV TZ="Asia/Shanghai"

COPY ./src/requirements.txt $APP_HOME/requirements.txt
COPY ./src/docker-entrypoint.sh $APP_HOME/docker-entrypoint.sh

RUN /usr/local/bin/python -m pip install --upgrade pip &&\
    cd $APP_HOME &&\
    pip install -r requirements.txt &&\
    pip install uwsgi &&\
    sed -i 's/\r//' docker-entrypoint.sh && \
    chmod +x docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]

