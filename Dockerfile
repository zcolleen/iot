FROM ubuntu

#RUN apt-get install bash
RUN apt-get update ; apt-get install -y curl
RUN curl https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash

CMD [ "bash" ]