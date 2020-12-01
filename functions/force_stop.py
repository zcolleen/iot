import paho.mqtt.client as mqtt
import ssl


class Register:

	def __init__(self, save):
		self.publisher = save

	@staticmethod
	def on_connect(client, userdata, flags, rc):
		print("Connected: " + str(rc))

	@staticmethod
	def on_message(client, userdata, message):
		print(message.topic + ' ' + str(message.payload))

	@staticmethod
	def on_publish(client, userdata, mid):
		print("Message published")

	def polling_devices(self, register):
		self.publisher.publish("$devices/are18v6krffaq7o1mldk/commands", payload="stop", qos=1)
		self.publisher.publish("$devices/are6c1grj2ojp532jr3u/commands", payload="stop", qos=1)
		self.publisher.publish("$devices/are2p8db0r2mne8jbm4d/commands", payload="stop", qos=1)


def handler(event, context):

	register = mqtt.Client(client_id="aresgcakub7pk92mbhej")
	my_register = Register(register)

	register.on_connect = Register.on_connect
	register.on_message = Register.on_message
	register.on_publish = Register.on_publish

	register.tls_set(ca_certs="../crt/rootCA.crt", certfile="../keys_certs/cert_register.pem",
					 keyfile="../keys_certs/key_register.pem", cert_reqs=ssl.CERT_REQUIRED,
					 tls_version=ssl.PROTOCOL_TLSv1_2)
	register.connect("mqtt.cloud.yandex.net", port=8883)
	register.loop_start()

	my_register.polling_devices(register)

	register.loop_stop()


handler(10, 10)
