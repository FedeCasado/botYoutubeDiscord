from turtle import color
import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re 

bot = commands.Bot(command_prefix='>', description='Esto es un HelperBot')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def suma(ctx, numOne: int,numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",description='Lorem ImpsumLorem ImpsumLorem Impsum', timestamp=datetime.datetime.utcnow(), color=discord.Color.blue() )
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner",  value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server Id", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, * , search):
   query_string =  parse.urlencode({'search_query': search})
   htmlContent = request.urlopen('http://www.youtube.com/results?' + query_string )
   resultadosBusqueda = re.findall(r'/watch\?v=(.{11})', htmlContent.read().decode())
   ## print(resultadosBusqueda)
   await ctx.send('https://www.youtube.com/watch?v=' + resultadosBusqueda[0])

# Envents
@bot.event
async def on_ready():
     await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="https://www.twitch.tv/soyrada"))
     print('My bot is ready!')

bot.run('OTMxOTc1MjY4ODc1MjcyMjYy.YeMPmw.BumRgoUI8q3uLrIV6I9Xxbkfxr8')


