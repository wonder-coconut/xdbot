
import discord
from discord.ext import commands

from random import seed
from random import randint

import datetime

bot = commands.Bot(command_prefix='~')

def getToken():
    tokenFile = open('TOKEN.txt','r')
    tokentxt = tokenFile.read()
    return tokentxt

@bot.event
async def on_ready():
    print('logged in as '+str(bot.user))

@bot.command()
async def test(ctx, arg):
    i = int(arg)
    await ctx.channel.send(xdRandom(i))

@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        word =  ctx.content.lower()
        if word.find('xd') != -1:
            await ctx.channel.send(xdRandom())
        
    await bot.process_commands(ctx)



def xdRandom(i = 0):
    if(i==0):

        time = datetime.datetime.now()
        mic = time.microsecond
        seed(mic)
        i = randint(1,13)
        
    print(f'random number generated is {i}')
    if(i>=1 and i<=9):
        xd =  open('xd_text/XD1.txt')
        xd = xd.read()
        xd = xd.split('\n')
        return xd[i]
    elif (i==10):
        xd =  open('xd_text/XD2.txt')
        xd = xd.read()
        return xd
    elif (i==11):
        xd = open('xd_text/XD3.txt')
        xd = xd.read()
        return xd 
    elif (i==12):
        xd = open('xd_text/XD4.txt')
        xd = xd.read()
        return xd 
    elif (i==13):
        xd = open('xd_text/XD5.txt')
        xd = xd.read()
        return xd 
    elif (i==14):
        xd = open('xd_text/XD6.txt')
        xd = xd.read()
        return xd 
    

bot.run (getToken())