import threading
import time
from time import sleep

import discord
import asyncio
from random import randint


intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

token = ''

def updatePayload(_):
    pass
updateFreq = 0


def clearFile(filename):
    open(filename, 'w').close()

@client.event
async def on_ready():
    global updatePayload, updateFreq
    print('Dbot Status: ONLINE')

    # Get the target channel
    channel = client.get_channel(1117938434963689603)

    # Start a loop to send messages every 5 seconds
    while True:
        updatePayload(updateFreq)

        with open('payload.txt', 'r') as payloadFile:
            payloadContent = payloadFile.read()
        if len(payloadContent) >= 5:
            payloads = payloadContent.split('\n\n')
            print(payloads)
            for payload in payloads:
                if payload != '':
                    await channel.send(payload)
                    time.sleep(randint(500, 2000) / 1000.0)

            # Allow buffer time
            clearFile('Payload.txt')



def init():
    global token, updateFreq
    sleep(1)
    token = input('Enter DBot Token\n>')
    updateFreq = float(input('Newsletter Frequency (hours)\n>'))

def begin(updateP):
    global updatePayload, updateFreq
    updatePayload = updateP
    client.run(token)











