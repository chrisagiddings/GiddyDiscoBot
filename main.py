import discord
import os

from discord import Intents

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if str(message.author) == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if str(message.content.contains).lower() == "good bot":
    await message.add_reaction("\u2764\uFE0F")


@client.event
async def on_reaction_add(reaction, user):
  await reaction.message.channel.send(
      str(user) + " reacted with " + str(reaction.emoji))


@client.event
async def on_message_edit(before, after):
  if before.content == after.content:
    return
  await after.channel.send(
      str(after.author) + " edited their message from " + str(before.content) +
      " to " + str(after.content))


client.run(os.getenv('TOKEN'))
