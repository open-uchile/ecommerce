FROM ubuntu:16.04

# Install system requirements
RUN apt update && \
    apt install -y --no-install-recommends libpython3.5-minimal python3-dev  python3-pip python3-setuptools nodejs npm nodejs-legacy libmysqlclient-dev mysql-client git make build-essential gcc locales \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install --upgrade pip \
    && rm /usr/bin/python \
    && ln -s /usr/bin/python3 /usr/bin/python

# Setup system locales, this is used to fix accent in code
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ADD . /openedx/ecommerce
WORKDIR /openedx/ecommerce

RUN make production-requirements && pip3 install fluent-logger==0.9.3 xmlsec==1.3.3

EXPOSE 8000
CMD gunicorn --name ecommerce --bind=0.0.0.0:8000 --max-requests=1000 --workers ${WORKER_COUNT:-1} ecommerce.wsgi:application
