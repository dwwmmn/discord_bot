import discord
from discord.ext import commands
import random
import requests
import asyncio
import stand
import randomGameGenerator
import token

command_prefix='$'
bot = commands.Bot(command_prefix)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')

def userCheck(ctx, fella):
    banFile = open("banList.txt", "r")
    for line in banFile:
        if line.rstrip('\n') == fella:
            return True
     
@bot.command()
async def botHelp(ctx):
    helpFile = open("README.txt")
    for line in helpFile:
        await ctx.send(line.rstrip('\n'))

@bot.command()
async def echo(ctx, *arg):
    print(ctx.author)
    print(ctx.author.id)
    if(userCheck(ctx, str(ctx.author.id))):
        return
    message = ""
    for i in arg:
        message += (i + " ")
    await ctx.send(message)

@bot.command()
async def randomGame(ctx, playerCount):
    #takes in number of players and returns an appropriate game
    print(ctx.author)
    print(ctx.author.id)
    if(userCheck(ctx, str(ctx.author.id))):
        return
    gamesList = randomGameGenerator.getList(playerCount)
    game = random.choice(gamesList)
    await ctx.send(game)

@bot.command()
async def randomDrink(ctx, arg):
    #takes in liquor, wine, or beer and returns a 
    return

@bot.command()
async def listGames(ctx, playerCount):
    #returns list of all games with given player count
    print(ctx.author)
    print(ctx.author.id)
    if(userCheck(ctx, str(ctx.author.id))):
        return
    gamesList = randomGameGenerator.getList(playerCount)
    await ctx.send(gamesList)

@bot.command()
async def suggest(ctx, *arg):
    #need to change arg to *
    print(ctx.author)
    print(ctx.author.id)
    if(userCheck(ctx, str(ctx.author.id))):
        return
    message = "Suggestion received: "
    for i in arg:
        message += (i + " ")
    f = open("suggestion.txt","a")
    f.write(message + '\n')
    f.close()
    await ctx.send(message)

@bot.command()
async def standAwaken(ctx, name, user, description, destructivePower, speed, range, durability, precision, developmentPotential):
    await ctx.send("awaken begin")
    newStand = Stand(name, user, description, destructivePower, speed, range, durability, precision, developmentPotential)
    message = newStand.readInfo()
    await ctx.send(message)

@bot.command()
async def standEdit():
    await ctx.send()

@bot.command()
async def standHelp(ctx):
    await ctx.send("Use $stand awaken \"Stand Name\", \"Stand User\", \"Description\", \"Destructive Power\", \"Speed\", \"Range\", \"Durability\", \"Precision\", \"Development Potential\"")

bot.run(token)
