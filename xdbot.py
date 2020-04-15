
import discord
from discord.ext import commands

from random import seed
from random import randint

import datetime

bot = commands.Bot(command_prefix='$')
BOT = discord.Client()

def getToken():
    tokenFile = open('token.txt','r')
    tokentxt = tokenFile.read()
    return tokentxt

@bot.event
async def on_ready():
    print('logged in as '+str(bot.user))

@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        word =  ctx.content.lower()
        if word.find('xd') != -1:
            await ctx.channel.send(xdRandom())

def xdRandom():
    time = datetime.datetime.now()
    mic = time.microsecond
    seed(mic)
    i = randint(1,6)
    if(i!=1):
        xd =  open('xd_text/XD2.txt')
        xd = xd.read()
        xd = xd.split('\n')
        return xd[i-1]
    elif (i==1):
        xd =  open('xd_text/XD1.txt')
        xd = xd.read()
        return xd

bot.run (getToken())