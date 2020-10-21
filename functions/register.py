import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import ssl
import time


def on_connect(client, userdata, flags, rc):
    print("Connected:" + str(rc))
    client.subscribe("$devices/are18v6krffaq7o1mldk/events", qos=1) # subscribing for devices(storage) 
#    client.subscribe("$devices/are6c1grj2ojp532jr3u/events", qos=1) # subscribing for devices(conveyer)
    print("Subscribed")


def on_message(client, userdata, message):
    global state
    print(message.topic + ' ' + str(message.payload))
    if message.topic == '$devices/are18v6krffaq7o1mldk/events':
      state['storage'] = str(message.payload)
#    if message.topic == '$devices/are6c1grj2ojp532jr3u/events': # for conveyer
#      state['conveyer'] == message.payload
      

def on_publish(client, userdata, mid):
    print("Message published")




state = dict({'storage' : 'not_ready', 'conveyer' : 'not_ready'})

register = mqtt.Client(client_id="aresgcakub7pk92mbhej")

register.on_connect = on_connect
register.on_message = on_message
register.on_publish = on_publish
#register.message_callback_add()


register.tls_set(ca_certs="../crt/rootCA.crt", certfile="../keys_certs/cert_register.pem",
keyfile="../keys_certs/key_register.pem", cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2)
register.connect("mqtt.cloud.yandex.net", port=8883)
register.loop_start()

while all(value=='ready' for value in state.values()) == False: # sending message till all devices are not ready
  if state['storage'] == 'not_ready':
    register.publish("$devices/are18v6krffaq7o1mldk/commands", payload="state", qos=1)
#  if state['conveyer'] == 'not_ready':
#    register.publish("$devices/are6c1grj2ojp532jr3u/commands", # for conveyer
#    payload="state", qos=1)
  time.sleep(5)


#register.disconnect()
register.loop_forever()
