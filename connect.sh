yc iot mqtt subscribe \
--debug \
--username arean1frk3n1vjugbnoq \
--password Semen21.02.2000 \
--topic '$device/arean1frk3n1vjugbnoq/commands' \
--qos 1

yc iot mqtt publish \
--debug \
--username arean1frk3n1vjugbnoq \
--password Semen21.02.2000 \
--topic '$devices/arean1frk3n1vjugbnoq/events' \
--message 'Test data' \
--qos 1

#sending command to device
mosquitto_pub -d -h mqtt.cloud.yandex.net \
-p 8883 \
--cafile rootCA.crt \
--cert cert_3.pem \
--key key_3.pem \
-t '$devices/arean1frk3n1vjugbnoq/commands' \
-m 'test command' \
-q 1

#sending data to register from device
mosquitto_pub -d -h mqtt.cloud.yandex.net \
-p 8883 \
--cafile rootCA.crt \
--cert cert.pem \
--key ke.pem \
-t '$devices/aregq0ha5729atv7cv9n/events' \
-m 'test' \
-q 1

#subscribing for commands from device
mosquitto_sub -d -h mqtt.cloud.yandex.net \
-p 8883 \
--cafile rootCA.crt \
--cert cert.pem \
--key key.pem \
-t '$devices/arean1frk3n1vjugbnoq/commands' \
-q 1


openssl req -x509 \
-newkey rsa:4096 \
-keyout key_3.pem \
-out cert_3.pem \
-nodes \
-days 365 \
-subj '/CN=localhost'
