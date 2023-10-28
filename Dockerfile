FROM python:3-buster

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txtc
COPY ./uwsgi.ini /app/uwsgi.ini
COPY ./app /app

WORKDIR /app
EXPOSE 443

RUN apt-get update && apt-get install -y \
		# openssl(暗号化や認証などのセキュリティ関係機能)の開発に必要らしい
		libssl-dev \
		# データのシリアライズに必要らしい
		libxml2-dev \
		libxslt1-dev \
		# この辺はPillow(画像処理)に必要らしい
		libjpeg-dev \
		# データの圧縮に必要らしい
		zlib1g-dev \
		# フォントに必要らしい
		libfreetype6-dev \
		liblcms2-dev \
		libopenjp2-7-dev \
		libtiff5-dev \
		# Tkinterを使うために必要らしい
		tk-dev \
		tcl-dev \
		libmariadb-dev-compat \
		mariadb-client \
		&& rm -rf /var/lib/apt/lists/* \
		&& apt-get clean \
		&& pip3 install -U pip \
		&& pip3 install -r requirements.txt

RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*