import paho.mqtt.client as mqtt
import ssl


class Register:

	store = "b'not_ready'"

	@staticmethod
	def on_connect(client, userdata, flags, rc):
		print("Connected: " + str(rc))
		client.subscribe("$devices/are18v6krffaq7o1mldk/events/done", qos=1)
		print("Subscribed")

	@staticmethod
	def on_message(client, userdata, message):
		print(message.topic + ' ' + str(message.payload))
		if message.topic == '$devices/are18v6krffaq7o1mldk/events/done':
			Register.store = str(message.payload)

	@staticmethod
	def on_publish(client, userdata, mid):
		print("Message published")


def handler(event, context):

	register = mqtt.Client(client_id="aresgcakub7pk92mbhej")

	test_dict = dict(
{
    "messages": [
        {
            "event_metadata": {
                 "event_id": "2153b5d2-c6af-4c69-a28d-74ce965b7613",
                 "event_type": "yandex.cloud.events.iot.IoTMessage",
                 "created_at": "2019-09-25T15:51:17.872320525Z"
            },
            "details": {
                 "registry_id": "arenou2oj4ct42eq8g3n",
                 "device_id": "areqjd6un3afc3cefcvm",
                 "mqtt_topic": "$devices/areqjd6un3afc3cefcvm/events",
                 "payload": "VGVzdCA0"
            }
        },
        {
            "event_metadata": {
                 "event_id": "2153b5d2-c6af-4c69-a28d-74ce965b7613",
                 "event_type": "yandex.cloud.events.iot.IoTMessage",
                 "created_at": "2019-09-25T15:51:17.872320525Z"
            },
            "details": {
                 "registry_id": "arenou2oj4ct42eq8g3n",
                 "device_id": "areqjd6un3afc3cefcvm",
                 "mqtt_topic": "$devices/areqjd6un3afc3cefcvm/events",
                 "payload": "VGVzdCA0"
            }
        }
    ]
})

	print(test_dict['messages'][0]['details']['payload'])
	register.on_connect = Register.on_connect
	register.on_message = Register.on_message
	register.on_publish = Register.on_publish

	register.tls_set(ca_certs="../crt/rootCA.crt", certfile="../keys_certs/cert_register.pem",
					keyfile="../keys_certs/key_register.pem", cert_reqs=ssl.CERT_REQUIRED,
					tls_version=ssl.PROTOCOL_TLSv1_2)

	register.connect("mqtt.cloud.yandex.net", port=8883)
	register.loop_start()

#	print(envent)
	if Register.store == "b'ready'":
		register.publish("$devices/are6c1grj2ojp532jr3u/commands", payload="process", qos=1)
	register.loop_stop()


handler(10, 10)
