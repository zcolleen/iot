import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import ssl

def on_connect(client, userdata, flags, rc):
  print("Connected:" + str(rc))
#  client.subscribe("$devices/are18v6krffaq7o1mldk/commands", qos=1)

def on_message(client, userdata, message):
  print(message.topic + " " + str(message.payload))

def on_publish(client, userdata, mid):
  print("Message published")

register = mqtt.Client(client_id="aresgcakub7pk92mbhej")
register.on_connect = on_connect
register.on_message = on_message
register.on_publish = on_publish
register.tls_set(ca_certs="../crt/rootCA.crt", certfile="../keys_certs/cert_1.pem", keyfile="../keys_certs/key_1.pem", cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2)

#register.loop_forever()
register.connect("mqtt.cloud.yandex.net", port=8883)
register.publish("$devices/are18v6krffaq7o1mldk/commands", payload="sending message from code", qos=1)
#publish.single("$devices/are18v6krffaq7o1mldk/commands", payload="sending text from module",
#hostname="mqtt.cloud.yandex.net", port=8883, client_id="are18v6krffaq7o1mldk", tls={'ca_certs':"../crt/rootCA.crt", 'certfile':"../keys_certs/cert_1.pem", 'keyfile':"../keys_certs/key_1.pem"})

#register.disconnect()
register.loop_forever()
