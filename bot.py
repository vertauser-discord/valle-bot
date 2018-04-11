#check out DiskOperator!
GeneratedToken = "Token"
import random
from random import randint
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix="va-")
client = discord.Client()

@bot.event
async def on_ready():
    print("READY")
    print("ID: " + bot.user.id)
    print("NAME: " + bot.user.name)
    print("TOKEN: " + GeneratedToken)
    await bot.change_presence(game=discord.Game(name="[1.2.5] - On github! bit.ly/vallegitbot"))

@bot.command(pass_context=True)
async def b(ctx):
    embed = discord.Embed(title="valle-bot info", description="Current version made 2018-03-23 (Version 1.2)", color=0x42e5f4)
    embed.add_field(name="Made with :heart: in :flag_se: by VertaUser", value="Environment: discord.py")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def n(ctx):
    embed = discord.Embed(title="Random number", description=randint(0,99999), color=0x42e5f4)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def u(ctx, user: discord.Member):
    embed = discord.Embed(title="Info about {}".format(user.name), description="I found this about {}".format(user.name), color=0x42e5f4)
    embed.add_field(name="User ID", value=user.id, inline=True)
    embed.add_field(name="User joindate", value=user.joined_at, inline=True)
    embed.add_field(name="User status", value=user.status)
    embed.add_field(name="User role", value=user.top_role, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def c(ctx):
    color = "%06x" % random.randint(0, 0xFFFFFF)
    embed = discord.Embed(title="Random color", description=color)
    await bot.say(embed=embed)

    #Testing below
@bot.command(pass_context=True)
async def DMTesting(ctx, user: discord.Member):
    await bot.send_message(ctx.message.author, 'Warning! Experimental nuclear testing!')

bot.run(GeneratedToken)
