
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

#testing command
@bot.command(name = "test")
async def test(ctx, arg):
    i = int(arg)
    await ctx.channel.send(xdRandom(i))

#programmed consent
@bot.command(name = "stop")
async def stop(ctx):
    print("close command detected, killing self :(")
    await bot.close()

@bot.command(name = "ascii")
async def ascii(ctx, arg):
    print(f"converting {arg} to ascii")
    try:
        await ctx.channel.send(asciify(arg))
        print("converted")
    except:
        print("failure")
    
@bot.event
async def on_message(ctx):

    if ctx.author != bot.user:
        words =  ctx.content.lower()
        wordlist = words.split(' ')
        if "xd" in wordlist:
            await ctx.channel.send(xdRandom())
        elif antiHax(words) == 1:
            await ctx.channel.send(xdRandom())
        elif antiHax(words) == 2:
            
            emoji = '<:XD:699673121287962654>'
            await ctx.add_reaction(emoji)

    await bot.process_commands(ctx)


#random output generator
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
    else:
        xd = open(f"xd_text/XD{i-8}.txt")
        xd = xd.read()
        return xd
    
def antiHax(words):
    if words.find('x') != -1:
        
        i = words.find('x')
        if words[i:].find('d') != -1:
            
            j = words[i:].find('d') + i
            
            for ch in words[i+1:j]:
                if ch.isalpha():
                    return 2
                
            return 1 #wont be executed if ch.isalpha() returns false
        else:
            return 0
    else:
        return 0
                
def asciify(phrase):
    str = ""
    art = open("ascii/ascii.txt",'r')
    arttxt = art.read().split("$")
    i = 0
    while(i<10):
        for ch in phrase:
            artchar = arttxt[ord(ch)-97]
            artline = artchar.split("\n")
            str = str + artline[i]
        str = str + "\n"
        i = i + 1
    str = str + "\n"
    str = "```" + str + "```"
    return str
    
bot.run (getToken())