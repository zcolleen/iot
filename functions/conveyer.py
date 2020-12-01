import paho.mqtt.client as mqtt
import ssl
from time import sleep


class Conveyer:

	flag_publish = 0

	def __init__(self, save):
		self.publisher = save

	@staticmethod
	def on_connect(client, userdata, flags, rc):
		print("Connected: " + str(rc))
		client.subscribe("$devices/are6c1grj2ojp532jr3u/commands", qos=1)
		print("Subscribed")

	def on_message(self, client, userdata, message):
		if str(message.payload) == "b'stop'":
			print("Forces stop of conveyer")
			Conveyer.flag_publish = 2
		elif str(message.payload) == "b'state'":
			self.publisher.publish("$devices/are6c1grj2ojp532jr3u/events", payload="ready", qos=1)
			print("Conveyer is ready")
		elif str(message.payload) == "b'process'":
			print("Conveyer processing command")
			sleep(10)
			Conveyer.flag_publish = 1

	@staticmethod
	def on_publish(client, userdata, mid):
		print("Message published")


def publisher(conv):
	i = 0
	while i < 2:
		conv.publish("$devices/are6c1grj2ojp532jr3u/events/done", payload="ready", qos=1)
		print("message published")
		sleep(10)
		i = i + 1


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

	conv.loop_start()
	while True:
		if Conveyer.flag_publish == 1:
			publisher(conv)
			Conveyer.flag_publish = 0
		if Conveyer.flag_publish == 2:
			conv.loop_stop()
			exit(1)


if __name__ == "__main__":
	handler()
