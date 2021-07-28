import discord

TOKEN = 'ODY5OTYyMTE1ODI4NTU1ODU2.YQF1Ww.Of-numdMpdwCEdl91o-SYosWuRE'

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!hello'):
    await message.channel.send('Hello!')

client.run(TOKEN)