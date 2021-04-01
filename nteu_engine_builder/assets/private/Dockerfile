FROM ubuntu:18.04

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
RUN export DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get install -y gcc
RUN apt-get install -y make
RUN apt-get install -y git
RUN apt-get install wget

##########################
### PYTHON 3.7
##########################

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3.7
RUN apt-get -y install python3-pip
RUN python3.7 -m pip install --upgrade pip

##########################
### Pragmatic segmenter
##########################

# Ruby
RUN apt-get install -y ruby-full

# Pragmatic segmenter dependencies
RUN gem install bundler
RUN gem install pragmatic_segmenter_server

# Pragmatic segmenter launcher
COPY private/config.ru /config.ru

##################
### Supervisord
##################

# install supervisord
RUN apt-get install -y supervisor

##################
### GATEWAY
##################

RUN python3.7 -m pip install nteu-gateway==1.0.1
COPY private/openapi.yaml openapi.yaml
COPY gateway_launcher.py gateway_launcher.py

##################
### GATEWAY UI
##################

RUN wget -O - https://github.com/Pangeamt/nteu-gateway-client/archive/refs/tags/0.0.1.tar.gz | tar -xz --strip=1 "nteu-gateway-client-0.0.1/dist"
RUN mv dist static

##################
### GATEWAY TRANSLATE FUNCTION
##################

COPY translate.py translate.py

##################
### TRANSLATIION ENGINE
##################

{% for item in config['translationEngine']['dockerCmds'] %}
{{ item }}
{% endfor %}

##################
### START SUPERVISORD
##################

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]
