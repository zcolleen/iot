import paho.mqtt.client as mqtt
import ssl
import time


class Register:

	state = dict({'storage': "b'not_ready'", 'conveyer': "b'ready'"})  # put in not ready state for conveyer

	def __init__(self, save):
		self.publisher = save

	@staticmethod
	def on_connect(client, userdata, flags, rc):
		print("Connected: " + str(rc))
		client.subscribe("$devices/are18v6krffaq7o1mldk/events", qos=1)  # subscribing for devices(storage)
		client.subscribe("$devices/are6c1grj2ojp532jr3u/events", qos=1)  # subscribing for devices(conveyer)
		print("Subscribed")

	@staticmethod
	def on_message(client, userdata, message):
		print(message.topic + ' ' + str(message.payload))
		if message.topic == '$devices/are18v6krffaq7o1mldk/events':
			Register.state['storage'] = str(message.payload)
		if message.topic == '$devices/are6c1grj2ojp532jr3u/events':  # for conveyer
			Register.state['conveyer'] = str(message.payload)

	@staticmethod
	def on_publish(client, userdata, mid):
		print("Message published")

	@staticmethod
	def on_message_put(client, userdata, message):
		print(str(message.payload))

	def polling_devices(self, register):
		while not all(value == "b'ready'" for value in Register.state.values()):  # sending message till all devices are not ready
			if Register.state['storage'] == "b'not_ready'":
				register.publish("$devices/are18v6krffaq7o1mldk/commands", payload="state", qos=1)
			if Register.state['conveyer'] == "b'not_ready'":
				register.publish("$devices/are6c1grj2ojp532jr3u/commands", payload="state", qos=1)  # uncomment this for conveyer
			time.sleep(5)
		self.publisher.publish("$devices/are18v6krffaq7o1mldk/commands", payload="put", qos=1)


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
