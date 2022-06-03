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

    @commands.command(aliases=["cf"])
    async def coinflip(self, ctx, message):
        answer = message.lower()
        choices = ["tails", "heads"]
        computers_answer = random.choice(choices)
        if answer not in choices:
            embed=discord.Embed(title="That is not a valid option. Please use heads or tails", color=0xFF0000)
            await ctx.reply(embed=embed)
            return
        else:
            if computers_answer == answer:
                embed=discord.Embed(title=f"You guessed correctly! The coin was {computers_answer}", color=0x00FF00)
                await ctx.reply(embed=embed)
            if computers_answer != answer:
                embed=discord.Embed(title=f"You guessed incorrectly! The coin was {computers_answer}", color=0xFF0000)
                await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot)) #test