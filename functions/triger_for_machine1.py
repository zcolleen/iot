
import paho.mqtt.client as mqtt
import ssl
#from time import sleep


class Register:

	def __init__(self, register):
		self.register = register

	@staticmethod
	def on_connect(client, userdata, flags, rc):
		print("Connected: " + str(rc))
		client.subscribe("$devices/are6c1grj2ojp532jr3u/events/done", qos=1)
#		client.subscribe("$devices/are2p8db0r2mne8jbm4d/events", qos=1)
		print("Subscribed")

	def on_message(self, client, userdata, message):
		print(message.topic + ' ' + str(message.payload))
#		if str(message.payload) == "b'ready'" and str(message.topic) == "$devices/are2p8db0r2mne8jbm4d/events":
#			self.register.publish("$devices/are2p8db0r2mne8jbm4d/commands", payload="process", qos=1)

	@staticmethod
	def on_publish(client, userdata, mid):
		print("Message published")


def handler(event, context):

	register = mqtt.Client(client_id="aresgcakub7pk92mbhej")
	my_register = Register(register)

	register.on_connect = Register.on_connect
	register.on_message = my_register.on_message
	register.on_publish = Register.on_publish

	register.tls_set(ca_certs="clf2/crt/rootCA.crt", certfile="clf2/keys_certs/cert_register.pem",
					keyfile="clf2/keys_certs/key_register.pem", cert_reqs=ssl.CERT_REQUIRED,
					tls_version=ssl.PROTOCOL_TLSv1_2)

	register.connect("mqtt.cloud.yandex.net", port=8883)
	register.loop_start()

	if event['messages'][0]['details']['payload'] == "cmVhZHk=":
		register.publish("$devices/are2p8db0r2mne8jbm4d/commands", payload="process", qos=1)
#		sleep(5)
	register.loop_stop()
