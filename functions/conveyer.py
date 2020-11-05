import paho.mqtt.client as mqtt
import ssl
import time


class Conveyer:

	def __init__(self, save):
		self.publisher = save

	@staticmethod
	def on_connect(client, userdata, flags, rc):
		print("Connected: " + str(rc))
		client.subscribe("$devices/are6c1grj2ojp532jr3u/commands", qos=1)
		print("Subscribed")

	def on_message(self, client, userdata, message):
		print(message.topic + ' ' + str(message.payload))
		if str(message.payload) == "b'state'":
			print("we won")
			self.publisher.publish("$devices/are6c1grj2ojp532jr3u/events", payload="ready", qos=1)
		#elif str(message.payload) == "b'process'":
			#your code func

	@staticmethod
	def on_publish(client, userdata, mid):
		print("Message published")


def handler():

	conv = mqtt.Client(client_id="are6c1grj2ojp532jr3u")
	my_conv = Conveyer(conv)

	conv.on_connect = Conveyer.on_connect
	conv.on_message = my_conv.on_message
	conv.on_publish = Conveyer.on_publish

	conv.tls_set(ca_certs="../crt/rootCA.crt", certfile="../keys_certs/cert_conveyer.pem",
					 keyfile="../keys_certs/key_conveyer.pem", cert_reqs=ssl.CERT_REQUIRED,
					 tls_version=ssl.PROTOCOL_TLSv1_2)
	conv.connect("mqtt.cloud.yandex.net", port=8883)
	print("ready_n_go")
#	conv.publish("$devices/are6c1grj2ojp532jr3u/events", payload="ready", qos=1)
	#your_func()
	conv.loop_forever()


if __name__ == "__main__":
	handler()
