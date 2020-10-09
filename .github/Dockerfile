FROM ubuntu:16.04

# Install system requirements
RUN apt update && \
    apt install -y --no-install-recommends python3.5 python3-dev python3-pip python3-setuptools libmysqlclient-dev mysql-client git make build-essential gcc locales \
    # webpay
    libssl-dev libxml2-dev libxmlsec1-dev \
    && rm -rf /var/lib/apt/lists/* \
    && ln -s /usr/bin/pip3 /usr/bin/pip \
    && ln -s /usr/bin/python3.5 /usr/bin/python \
    && pip install --upgrade pip

# Setup system locales, this is used to fix accent in code
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ADD . /openedx/ecommerce
ADD ./assets.py /openedx/ecommerce/ecommerce/settings/assets.py
ADD ./eol.py /openedx/ecommerce/ecommerce/settings/eol.py
WORKDIR /openedx/ecommerce

# Get nodejs
RUN pip install nodeenv
RUN nodeenv /openedx/nodeenv --node=12.13.0 --prebuilt
ENV PATH /openedx/nodeenv/bin:${PATH}

RUN make production-requirements && pip install xmlsec==1.3.3 python-json-logger==0.1.11 && DJANGO_SETTINGS_MODULE=ecommerce.settings.assets make static

EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE=ecommerce.settings.eol
CMD gunicorn --name ecommerce --bind=0.0.0.0:8000 --max-requests=1000 --workers ${WORKER_COUNT:-1} ecommerce.wsgi:application
