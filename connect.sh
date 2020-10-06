#subscribe for topic for exact device
yc iot mqtt subscribe \
--debug \
--cert cert.pem \
--key key.pem \
--topic '$devices/are18v6krffaq7o1mldk/commands' \
--qos 1

#publish command for device
yc iot mqtt publish \
--debug \
--cert cert_1.pem \
--key key_1.pem \
--topic '$devices/are18v6krffaq7o1mldk/commands' \
--message 'Test next' \
--qos 1


yc iot mqtt publish \
--cert cert.pem \
--key key.pem \
--topic '$devices/are18v6krffaq7o1mldk/events' \
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
--key key.pem \
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
