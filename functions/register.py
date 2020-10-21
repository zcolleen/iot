import paho.mqtt.client as mqtt
import ssl
import time


def on_connect(client, userdata, flags, rc):
    print("Connected: " + str(rc))
    client.subscribe("$devices/are18v6krffaq7o1mldk/events", qos=1) # subscribing for devices(storage) 
#    client.subscribe("$devices/are6c1grj2ojp532jr3u/events", qos=1) # subscribing for devices(conveyer)
    print("Subscribed")


def on_message(client, userdata, message):
    print(message.topic + ' ' + str(message.payload))
    if message.topic == '$devices/are18v6krffaq7o1mldk/events':
      state['storage'] = str(message.payload)
#    if message.topic == '$devices/are6c1grj2ojp532jr3u/events': # for conveyer
#      state['conveyer'] == str(message.payload)


def on_publish(client, userdata, mid):
    print("Message published")


def on_message_put(client, userdata, message):
    print(str(message.payload))


def polling_devices(register):
    while not all(value == "b'ready'" for value in state.values()): # sending message till all devices are not ready
      if state['storage'] == "b'not_ready'":
        register.publish("$devices/are18v6krffaq7o1mldk/commands", payload="state", qos=1)
    #  if state['conveyer'] == 'not_ready':
    #    register.publish("$devices/are6c1grj2ojp532jr3u/commands", # uncomment this for conveyer
    #    payload="state", qos=1)
      time.sleep(5)


def handler(event, context):
    global state
    state = dict({'storage' : "b'not_ready'", 'conveyer' : "b'ready'"}) # put in not ready state

    register = mqtt.Client(client_id="aresgcakub7pk92mbhej")

    register.on_connect = on_connect
    register.on_message = on_message
    register.on_publish = on_publish


    register.tls_set(ca_certs="../crt/rootCA.crt", certfile="../keys_certs/cert_register.pem",
    keyfile="../keys_certs/key_register.pem", cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2)
    register.connect("mqtt.cloud.yandex.net", port=8883)
    register.loop_start()

    polling_devices(register)
    register.publish("$devices/are18v6krffaq7o1mldk/commands", payload="put", qos=1)
    # while state['storage'] != 'ready':
    #  time.sleep(1)

    register.loop_stop()
    # register.loop_forever()


handler(10, 10)