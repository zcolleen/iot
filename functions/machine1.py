import paho.mqtt.client as mqtt
import ssl
import time


class Machine1:

	flag_publish = 0

	def __init__(self, save):
		self.publisher = save

	@staticmethod
	def on_connect(client, userdata, flags, rc):
		print("Connected: " + str(rc))
		client.subscribe("$devices/are2p8db0r2mne8jbm4d/commands", qos=1)
		print("Subscribed")

	def on_message(self, client, userdata, message):
		if str(message.payload) == "b'stop'":
			print("Forces stop of machine1")
			exit(1)
		elif str(message.payload) == "b'state'":
			print("Machine1 is ready")
			Machine1.flag_publish = 2
			#self.publisher.publish("$devices/are2p8db0r2mne8jbm4d/events", payload="ready", qos=1)
		elif str(message.payload) == "b'process'":
			print("Machine1 processing command")
			time.sleep(20)
			print("Machine1 has finished processing command")
			Machine1.flag_publish = 1
			#self.publisher.publish("$devices/are6c1grj2ojp532jr3u/commands", payload="machine1_done", qos=1)

	@staticmethod
	def on_publish(client, userdata, mid):
		print("Message published")


def publisher(ma1):
	if Machine1.flag_publish == 2:
		ma1.publish("$devices/are2p8db0r2mne8jbm4d/events", payload="ready", qos=1)
		#print("Machine1 is ready" + " " + str(Machine1.flag_busy))
	if Machine1.flag_publish == 1:
		ma1.publish("$devices/are6c1grj2ojp532jr3u/commands", payload="machine1_done", qos=1)
	Machine1.flag_publish = 0


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
	ma1.loop_start()
	while True:
		if Machine1.flag_publish > 0:
			publisher(ma1)


if __name__ == "__main__":
	handler()
