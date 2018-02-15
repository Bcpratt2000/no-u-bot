import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

client = Bot(description="responds no u", command_prefix="", pm_help = False)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	return await client.change_presence(game=discord.Game(name='the drums')) #This is buggy, let us know if it doesn't work.

@client.event
async def on_message(message):

	#only work on battle-bots channel
	if(message.channel.name == "battle-bots") | (message.author.name == "cabobalot"):
		print(message.author.name + ": " + message.content)
		if(message.content == "no u") & (message.author.bot == false):
			await client.send_message(message.channel, "false, 'tis indeed thou.")
		elif(message.content.lower() == "!setbattle true"):
			await client.send_message(message.channel, "!setBattle False")
			await client.send_message(message.channel, "false, 'tis indeed thou.")
			await client.send_message(message.channel, "You think you can best me? You ninnyhammer!")

client.run('NDEzNDY2MTQxMTg5NzM0NDMw.DWZSnw.W6Di4Rldu70f4SdyORmSvDmVaRE')
