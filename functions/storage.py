import paho.mqtt.client as mqtt
import ssl
from time import sleep


class Storage:

	def __init__(self, save):
		self.publisher = save

	@staticmethod
	def on_connect(client, userdata, flags, rc):
		print("Connected: " + str(rc))
		client.subscribe("$devices/are18v6krffaq7o1mldk/commands", qos=1)
		print("Subscribed")

	def on_message(self, client, userdata, message):
	#	print(message.topic + ' ' + str(message.payload))
		if str(message.payload) == "b'stop'":
			print("Forced stop of storage")
			exit(1)
		elif str(message.payload) == "b'state'":
			self.publisher.publish("$devices/are18v6krffaq7o1mldk/events", payload="ready", qos=1)
			print("Storage is ready")
		elif str(message.payload) == "b'put'":
			print("Storage processing command")
			sleep(10)
			self.publisher.publish("$devices/are18v6krffaq7o1mldk/events/done", payload="ready", qos=1)

	@staticmethod
	def on_publish(client, userdata, mid):
		print("Message published")


def handler():
	stor = mqtt.Client(client_id="are6c1grj2ojp532jr3u")
	my_stor = Storage(stor)

	stor.on_connect = Storage.on_connect
	stor.on_message = my_stor.on_message
	stor.on_publish = Storage.on_publish

	stor.tls_set(ca_certs="../crt/rootCA.crt", certfile="../keys_certs/cert_storage.pem",
				 keyfile="../keys_certs/key_storage.pem", cert_reqs=ssl.CERT_REQUIRED,
				 tls_version=ssl.PROTOCOL_TLSv1_2)
	stor.connect("mqtt.cloud.yandex.net", port=8883)

	stor.loop_forever()


if __name__ == "__main__":
	handler()
