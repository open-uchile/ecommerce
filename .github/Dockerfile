FROM ubuntu:16.04

# Install system requirements
RUN apt update && \
    apt install -y --no-install-recommends python2.7 python-dev python-pip python-setuptools nodejs npm nodejs-legacy libmysqlclient-dev mysql-client git make build-essential gcc locales \
    # webpay
    libssl-dev libxml2-dev libxmlsec1-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip

# Setup system locales, this is used to fix accent in code
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ADD . /openedx/ecommerce
WORKDIR /openedx/ecommerce

RUN make production-requirements && pip install xmlsec==1.3.3

EXPOSE 8000
CMD gunicorn --name ecommerce --bind=0.0.0.0:8000 --max-requests=1000 --workers ${WORKER_COUNT:-1} ecommerce.wsgi:application
