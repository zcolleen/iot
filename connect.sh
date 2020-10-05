yc iot mqtt subscribe \
--username arean1frk3n1vjugbnoq \
--password Semen21.02.2000 \
--topic '$device/arean1frk3n1vjugbnoq/commands' \
--qos 1

yc iot mqtt publish \
-u arean1frk3n1vjugbnoq \
-p Semen21.02.2000 \
--topic '$devices/arean1frk3n1vjugbnoq/events' \
--message 'Test data' \
--qos 1

mosquitto_sub -d -h mqtt.cloud.yandex.net \
-p 8883 \
--cafile rootCA.crt \
--cert cert.pem \
--key key.pem \
-t '$devices/arean1frk3n1vjugbnoq/commands' \
-q 1

mosquitto_pub -d -h mqtt.cloud.yandex.net \
-p 8883 \
--cafile rootCA.crt \
--cert cert.pem \
--key key.pem \
-t '$devices/aregq0ha5729atv7cv9n/events' \
-m 'test' \
-q 1

mosquitto_pub -d -t '$devices/arean1frk3n1vjugbnoq/events' -m "Hello from Terminal window 2!"