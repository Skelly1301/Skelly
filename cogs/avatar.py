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

    @commands.command(aliases=["pfp"])
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        if avamember == None:
          avamember = ctx.author
        userAvatarUrl = avamember.avatar_url
        await ctx.send(userAvatarUrl)

def setup(bot):
    bot.add_cog(Fun(bot)) #test