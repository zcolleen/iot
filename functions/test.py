import paho.mqtt.Client as mqtt

def on_connect(client, userdata, flags, rc):
  print("Connected:" + rc)

  client.subscribe("$devices/are18v6krffaq7o1mldk/commands", qos=1)

def on_message(client, userdata, message):
  print(message.topic + " " + message.payload)

client = mqtt.Client(client_id="are18v6krffaq7o1mldk")