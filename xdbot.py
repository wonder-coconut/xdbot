
import discord
from discord.ext import commands

from random import seed
from random import randint

import datetime

bot = commands.Bot(command_prefix='~')
bot.remove_command('help') 

def getToken():
    tokenFile = open('TOKEN.txt','r')
    tokentxt = tokenFile.read()
    return tokentxt

@bot.event
async def on_ready():
    print('logged in as '+str(bot.user))

#help command
@bot.command(name = "help")
async def help(ctx):
    await ctx.channel.send(
'''> this bot is purely to prank those mfs who use xD way too often
   > command prefix  :   '~'
   > commands:
   > test    :   test out specific responses
   > stop    :   kill the bot
   > ascii   :   convert text to ascii art''')

#testing command
@bot.command(name = "test")
async def test(ctx, arg):
    i = int(arg)
    await ctx.channel.send(xdRandom(i))

#programmed consent
@bot.command(name = "stop")
async def stop(ctx):
    if await ctx.bot.is_owner(ctx.author):
        print("close command detected, killing self :(")
        await bot.close()
    else:
        await ctx.channel.send(death())

#ascii
@bot.command(name = "ascii")
async def ascii(ctx, arg):
    print(f"converting {arg} to ascii")
    try:
        await ctx.channel.send(asciify(arg))
        print("converted")
    except Exception as e:
        print(e)
    
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

#antihax
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

#ascii converter            
def asciify(phrase):
    phrase = phrase.lower()
    str = ""
    art = open("ascii/ascii.txt",'r')
    arttxt = art.read().split("$")
    i = 0
    while(i<10):
        for ch in phrase:
            if ch.isalpha():
                artchar = arttxt[ord(ch)-97]
            else:
                artchar = arttxt[26]
            artline = artchar.split("\n")
            str = str + artline[i]
        str = str + "\n"
        i = i + 1
    str = str + "\n"
    str = "```" + str + "```"
    return str

#death threats
def death():
        time = datetime.datetime.now()
        mic = time.microsecond
        seed(mic)
        i = randint(0,9)
        
        death = open("death/death.txt",'r')
        death = death.read().split('\n')
        return death[i]
        

bot.run (getToken())