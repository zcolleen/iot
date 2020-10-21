yc iot mqtt publish \
--debug \
--cert keys_certs/cert_storage.pem \
--key keys_certs/key_storage.pem \
--topic '$devices/are18v6krffaq7o1mldk/events' \
--message 'ready' \
--qos 1
