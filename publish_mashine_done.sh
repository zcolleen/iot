
yc iot mqtt publish \
--debug \
--cert keys_certs/cert_register.pem \
--key keys_certs/key_register.pem \
--topic '$devices/are6c1grj2ojp532jr3u/commands' \
--message 'processing_mode0' \
--qos 1
