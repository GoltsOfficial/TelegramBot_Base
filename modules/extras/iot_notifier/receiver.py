import asyncio
import paho.mqtt.client as mqtt
from aiogram import Bot
from .config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, ALERT_CHAT_ID
from Gear.config import config

bot = Bot(token=config.BOT_TOKEN)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    asyncio.create_task(bot.send_message(ALERT_CHAT_ID, f"Уведомление с устройства:\n{message}"))

def start_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()
