import discord
from discord.ext import commands
import random
import json
import loadpic
loadpic.load()

with open('pic.json','r',encoding='utf8') as jfile:
    config = json.load(jfile)

bot = commands.Bot(command_prefix='/kai ',intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    print('fffffffff')

@bot.command()
async def pic (ctx):
    randompic = random.choice(config['pic'])
    pic = discord.File(randompic)
    await ctx.send(file=pic)

# @bot.event #未完成
# async def on_reaction_add(reaction, user):
#     if user == bot.user:
#         return
#     if reaction.emoji.id != "U+1F622" :
#         return
#     if reaction.message.attachments:
#         for attachment in reaction.message.attachments:
#             if attachment.content_tyep not in ["application/vnd.microsoft.portable-executable", "application/vnd.ms-excel"]:
#                 pass
#             else:
#                 count.detect
#                 filepic = await attachment.read()
#                 with open(f"C:\\Users\\jerry\\Desktop\\kaikaibabe\\pic\\{attachment.filename}", "wb") as file:
#                     file.write(filepic)
#                 await reaction.message.add_reaction("U+2705")
bot.run(config["TOKEN"])