import discord
from discord.ext import commands, tasks
import random
import json
import loadpic
loadpic.load()
from reactionmenu import ReactionMenu, ReactionButton
from reactionmenu import ViewMenu, ViewButton, ViewSelect ,Page
from aternosapi import AternosAPI
import os
import time
import count

with open('pic.json','r',encoding='utf8') as jfile:
    config = json.load(jfile)

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all()) 
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('wwwwwwwwwww'))
    print('fffffffff')

@bot.command() #picture
async def pic (ctx):
    randompic = random.choice(config['pic'])
    pic = discord.File(randompic)
    await ctx.send(file=pic)

@bot.command()    #kais gallery 參考https://github.com/Defxult/reactionmenu
async def kg(ctx: commands.Context):
    menu = ViewMenu(ctx, menu_type=ViewMenu.TypeEmbed,rows_requested = 3, remove_items_on_timeout=True, delete_interactions=True)
    back_button = ViewButton(style=discord.ButtonStyle.primary, label='', custom_id=ViewButton.ID_PREVIOUS_PAGE, emoji='<:emoji_32:878318476773687376>')
    menu.add_button(back_button)
    next_button = ViewButton(style=discord.ButtonStyle.primary, label='', custom_id=ViewButton.ID_NEXT_PAGE, emoji='<:handsome_middlefinger:860588679234977872>')
    menu.add_button(next_button)
    instagran_button_kai = ViewButton(style=discord.ButtonStyle.primary, label='', url='wwwwwwwwwwww', emoji='<:ryan_coin:860597363402735616>')
    menu.add_button(instagran_button_kai)
    instagran_button_xinyi = ViewButton(style=discord.ButtonStyle.primary, label='', url='wwwwwwwwwwwwwwww', emoji='<:unknown2:970260435863470100>')
    menu.add_button(instagran_button_xinyi)
    dir=os.path.join(os.path.dirname(__file__),'pic')
    for file_name_in_dir in os.listdir(dir):
        file_path = os.path.join(dir,file_name_in_dir)
        with open(file_path,'rb') as data:
            picture_going_to_output = discord.File(data)
        embed=discord.Embed(title="Kai's Gallery", color=0x7ff71d )
        embed.set_image(url=f"attachment://{file_name_in_dir}")
        menu.add_page(embed, files=[picture_going_to_output])
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar)
    await menu.start()

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    cahnnel = bot.get_channel(1181610361108041901)
    dir=os.path.join(os.path.dirname(__file__),'not_only_for_kai')
    if message.channel != cahnnel:
        return
    if message.author.id == bot.user.id:
        return
    if message.attachments:
        max_amount = 100
        if count.count() >= max_amount:
            time.sleep(1)
            await bot.get_channel(1181610361108041901).send("資料夾滿了")
            return
        for attachments in message.attachments:
            print(attachments)
            image_format =['.jpeg', '.png','.jpg']
            ext = os.path.splitext(attachments.filename)[-1]
            if ext in image_format:
                # await attachments.save(attachments.filename)
                await attachments.save(os.path.join(dir,attachments.filename))
                await bot.get_channel(1181610361108041901).send(f"上傳成功:剩餘{max_amount-count.count()}空閒欄位")

@bot.command() #picture(not only kai)
async def nfk (ctx):
    randompic = random.choice(config['pic_not_only_for_kai'])
    pic = discord.File(randompic)
    await ctx.send(file=pic)

bot.run(config["TOKEN"])