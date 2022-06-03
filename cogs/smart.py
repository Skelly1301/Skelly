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
    async def smart(self, ctx, member: discord.User=None):
        low = random.randint(1,33)
        med = random.randint(34,66)
        high = random.randint(67,100)
        smart = [low, med, high]
        smartness = random.choice(smart)
        if member == None:
          if smartness == low:
            embed = discord.Embed(title=f"Your smartness rating is {smartness}%!", color=0xFF0000)
            await ctx.reply(embed=embed)
          elif smartness == med:
            embed = discord.Embed(title=f"Your smartness rating is {smartness}%!", color=0xFFFF00)
            await ctx.reply(embed=embed)
          elif smartness == high:
            embed = discord.Embed(title=f"Your smartness rating is {smartness}%!", color=0x00FF00)
            await ctx.reply(embed=embed)
        if member != None:
          if smartness == low:
            embed = discord.Embed(title=f"{member} your smartness rating is {smartness}%!", color=0xFF0000)
            await ctx.reply(embed=embed)
          elif smartness == med:
            embed = discord.Embed(title=f"{member} your smartness rating is {smartness}%!", color=0xFFFF00)
            await ctx.reply(embed=embed)
          elif smartness == high:
            embed = discord.Embed(title=f"{member} your smartness rating is {smartness}%!", color=0x00FF00)
            await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))#test