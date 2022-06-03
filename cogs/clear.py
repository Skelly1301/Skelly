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


    @commands.command(aliases=["purge"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        authors = {}
        async for message in ctx.channel.history(limit=amount + 1):
            if message.author not in authors:
                authors[message.author] = 1
            else:
                authors[message.author] += 1
            await message.delete()
    
        embed=discord.Embed(title=f"Cleared {amount} messages", color=0x5865F2)
        await ctx.channel.send(embed=embed, delete_after=7)


def setup(bot):
    bot.add_cog(Moderation(bot)) #test