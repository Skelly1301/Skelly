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
    async def unmute(ctx, member: discord.Member):
        guild = ctx.guild
        unmutedRole = discord.utils.get(guild.roles, name="Muted")
        await member.remove_roles(unmutedRole)
        embed = discord.Embed(title=f"**{member}** was unmuted", color=0x5865F2)
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Moderation(bot))#test