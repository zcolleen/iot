FROM ubuntu

#RUN apt-get install bash
RUN apt-get update ; apt-get install -y curl
#apt-get install -y mosquitto 
#RUN apt-get install mosquitto mosquitto-clients
#RUN apt-get install openssl
#RUN apt-get install -y vim
RUN curl https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
RUN apt-get install -y vim


COPY ./crt/rootCA.crt .
COPY ./crt/rootCA.crt:Zone.Identifier .
COPY ./keys_certs/key.pem .
COPY ./keys_certs/cert.pem .
COPY ./keys_certs/key_1.pem .
COPY ./keys_certs/cert_1.pem .
COPY ./sender.sh .
COPY ./reciever.sh .

EXPOSE 8883

CMD ["bash"]
#CMD [ "sh", "start.sh" ]