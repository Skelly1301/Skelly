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


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=["sm"])
    @commands.has_permissions(kick_members=True)
    async def slowmode(self, ctx, seconds: int):
        embed = discord.Embed(title=f"Set this channels slowmode to {seconds} seconds!", color=0x5865F2)
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Moderation(bot))#test