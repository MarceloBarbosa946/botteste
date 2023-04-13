import discord
from discord.ext import commands

botid = 'MTA5NTUxMjI5NDI3Mzg1MTUxMg.G_Sgl1.Z5b19vEB458Mn5LuaNhEIRVcjUPuJWRPQLxO-w'
channelId = 1095512294273851512

bot = commands.Bot(command_prefix ='!', intents=discord.Intents.all())

#a

# evento de criação do de comando do bot
@bot.event
async def on_ready():
    print("Hello there, What's Your excuse now?")
    # codigo que limita as respostas do bot a aquele id de canal de txt
    channel = bot.get_channel(channelId)
    await channel.send('Hello there . . . i am working')

@bot.command()
async def add(ctx, x, y):
    result = int(x) + int(y)
    await ctx.send('Hello!')

bot.run(botid)