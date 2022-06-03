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

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        content = get("https://meme-api.herokuapp.com/gimme").text
        data = json.loads(content, )
        meme = discord.Embed(
            title=f"{data['title']}",
            color=0x5865F2).set_image(url=f"{data['url']}")
        await ctx.reply(embed=meme)

def setup(bot):
    bot.add_cog(Fun(bot))#test