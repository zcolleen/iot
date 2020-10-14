import paho.mqtt.client as mqtt
import ssl

def on_connect(client, userdata, flags, rc):
  print("Connected:" + str(rc))
  client.subscribe("$devices/are18v6krffaq7o1mldk/commands", qos=1)

def on_message(client, userdata, message):
  print(message.topic + " " + str(message.payload))

client = mqtt.Client(client_id="are18v6krffaq7o1mldk")
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(ca_certs="../crt/rootCA.crt", certfile="../keys_certs/cert.pem", keyfile="../keys_certs/key.pem", cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2)

client.connect("mqtt.cloud.yandex.net", port=8883)
client.loop_forever()
