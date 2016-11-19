FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENV NODEJS_VERSION=6.9.1 \
    PATH=$PATH:/opt/node/bin

# Node and npm
RUN curl -sL https://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz | tar xz --strip-components=1

# Clear cache
RUN apt-get autoclean && apt-get clean
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/