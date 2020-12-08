import paho.mqtt.client as mqtt
import ssl
import base64

class Register:

	@staticmethod
	def on_connect(client, userdata, flags, rc):
		print("Connected: " + str(rc))
		print("Subscribed")

	@staticmethod
	def on_message(client, userdata, message):
		print(message.topic + ' ' + str(message.payload))

	@staticmethod
	def on_publish(client, userdata, mid):
		print("Message published")


def handler(event, context):

	register = mqtt.Client(client_id="aresgcakub7pk92mbhej")

	register.on_connect = Register.on_connect
	register.on_message = Register.on_message
	register.on_publish = Register.on_publish

	register.tls_set(ca_certs="clf2/crt/rootCA.crt", certfile="clf2/keys_certs/cert_register.pem",
					keyfile="clf2/keys_certs/key_register.pem", cert_reqs=ssl.CERT_REQUIRED,
					tls_version=ssl.PROTOCOL_TLSv1_2)

	register.connect("mqtt.cloud.yandex.net", port=8883)
	register.loop_start()
	d = base64.b64decode(event['messages'][0]['details']['payload'])
#	print(d)
	s2 = d.decode("UTF-8")
#	print(s2)
	register.publish("$devices/are18v6krffaq7o1mldk/commands", payload=s2, qos=1)
	register.loop_stop()
