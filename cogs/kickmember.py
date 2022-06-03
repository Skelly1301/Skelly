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

        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kickmember(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        embed = discord.Embed(title=f"{member} has been kicked from the server. Goodbye!", color=0x5865F2)
        await member.kick(reason=reason)
        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))#test