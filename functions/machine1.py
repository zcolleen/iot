import paho.mqtt.client as mqtt
import ssl
from time import sleep


class Machine1:

	def __init__(self, save):
		self.publisher = save

	@staticmethod
	def on_connect(client, userdata, flags, rc):
		print("Connected: " + str(rc))
		client.subscribe("$devices/are2p8db0r2mne8jbm4d/commands", qos=1)
		print("Subscribed")

	def on_message(self, client, userdata, message):
		print(message.topic + ' ' + str(message.payload))
		if str(message.payload) == "b'state'":
			self.publisher.publish("$devices/are2p8db0r2mne8jbm4d/events", payload="ready", qos=1)
		elif str(message.payload) == "b'process'":
			print("Machine1 processing command")
			sleep(15)
			self.publisher.publish("$devices/are2p8db0r2mne8jbm4d/events/done", payload="ready", qos=1)


	@staticmethod
	def on_publish(client, userdata, mid):
		print("Message published")


def handler():

	ma1 = mqtt.Client(client_id="are2p8db0r2mne8jbm4d")
	my_ma1 = Machine1(ma1)

	ma1.on_connect = Machine1.on_connect
	ma1.on_message = my_ma1.on_message
	ma1.on_publish = Machine1.on_publish

	ma1.tls_set(ca_certs="../crt/rootCA.crt", certfile="../keys_certs/cert_machine1.pem",
					 keyfile="../keys_certs/key_machine1.pem", cert_reqs=ssl.CERT_REQUIRED,
					 tls_version=ssl.PROTOCOL_TLSv1_2)
	ma1.connect("mqtt.cloud.yandex.net", port=8883)

	ma1.loop_forever()


if __name__ == "__main__":
	handler()
