import os
import discord
from discord.ext import commands
import random
import requests
import json
from requests import get
import datetime
import asyncio
import sys
import traceback
import DiscordUtils
import keep_alive
from math import floor


TOKEN = ""
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove_command('help')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")




@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready')
    await bot.change_presence(activity=discord.Streaming(name="$help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="You don't have the permissions to do that", color=0xFF0000)
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed1 = discord.Embed(title="You're missing a required argument. If you're stuck use $help", color=0xFF0000)
        await ctx.reply(embed=embed1)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command),
              file=sys.stderr)
        traceback.print_exception(type(error),
                                  error,
                                  error.__traceback__,
                                  file=sys.stderr)
    if isinstance(error, commands.CommandOnCooldown):
        msg = "Woah! Slow down! You have to wait {:.2f} seconds before you can do that again".format(
            error.retry_after)
        await ctx.reply(msg)






@bot.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title="Skelly", description="Use `$help <command>` for more info on a command. `<> = required argument`, `[] = optional argument`", color=0x5865F2)
    embed.set_author(name="Help", icon_url="https://media.discordapp.net/attachments/953360620978323517/973971817674973204/assassination_c_room.jpg")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/953360620978323517/973971817674973204/assassination_c_room.jpg")
    embed.add_field(name="Moderation", value="`mute` `unmute` `slowmode` `kickmember` `clear`", inline=False)
    embed.add_field(name="Fun", value="`meme` `avatar` `slap` `kick` `coinflip` `smart`", inline=False)
    await ctx.reply(embed=embed)
    await ctx.author.send("You can check the bot GitHub for extensive information, and source code - https://github.com/skelly1301/Skelly")

@help.command()
async def mute(ctx):
    embed = discord.Embed(title="Mute", description="Mutes a specific member from the server", color=0x5865F2)
    embed.add_field(name="**Syntax**", value="`$mute <@user> <time> [reason]`")
    await ctx.reply(embed=embed)

@help.command()
async def unmute(ctx):
    embed = discord.Embed(title="Unmute", description="Unmutes a specific member from the server", color=0x5865F2)
    embed.add_field(name="**Syntax**", value="`$unmute <@user>`")
    await ctx.reply(embed=embed)

@help.command()
async def meme(ctx):
    embed = discord.Embed(title="Meme", description="Sends a random meme from reddit", color=0x5865F2)
    embed.add_field(name="**Syntax**", value="`$meme`")
    await ctx.reply(embed=embed)

@help.command()
async def avatar(ctx):
    embed = discord.Embed(title="Avatar", description="Sends a requested users avatar", color=0x5865F2)
    embed.add_field(name="**Syntax**", value="`$pfp [@user]`")
    await ctx.reply(embed=embed)

@help.command()
async def slowmode(ctx):
    embed = discord.Embed(title="Slowmode", description="Sets the slowmode of the channel to a certian amount of seconds", color=0x5865F2)
    embed.add_field(name="**Syntax**", value="`$sm <seconds>`")
    await ctx.reply(embed=embed)

@help.command()
async def kickmember(ctx):
    embed = discord.Embed(title="Kickmember", description="Kicks a member from the server", color=0x5865F2)
    embed.add_field(name="**Syntax**", value="`$kickmember <@user>`")
    await ctx.reply(embed=embed)

@help.command()
async def clear(ctx):
    embed = discord.Embed(title="Clear", description="Clears a certain amount of messages from the channel the command is executed from", color=0x5865F2)
    embed.add_field(name="**Syntax**", value="`$clear <amount>`")
    await ctx.reply(embed=embed)

@help.command()
async def slap(ctx):
    embed = discord.Embed(title="Slap", description="Slaps a mentioned user, or if no one is mentioned, yourself!", color=0x5865F2)
    embed.add_field(name="**Syntax**", value="`$slap <@user>`")
    await ctx.reply(embed=embed)

@help.command()
async def kick(ctx):
    embed = discord.Embed(title="Kick", description="Kicks a mentioned user, or if no one is mentioned, yourself!", color=0x5865F2)
    embed.add_field(name="**Syntax**", value="`$kick <@user>`")
    await ctx.reply(embed=embed)

@help.command()
async def coinflip(ctx):
    embed = discord.Embed(title="Coinflip", description="Flip a coin!", color=0x5865F2)
    embed.add_field(name="**Syntax**", value="`$cf <choice>`")
    await ctx.reply(embed=embed)

@help.command()
async def smart(ctx):
    embed = discord.Embed(title="Smart", description="See how smart you are, or check how smart another member is!", color=0x5865F2)
    embed.add_field(name="**Syntax**", value="`$smart [@user]`")
    await ctx.reply(embed=embed)


  




#, color=0x5865F2

keep_alive.keep_alive()
bot.run(TOKEN)
