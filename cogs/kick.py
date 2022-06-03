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
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx, member:discord.User=None):
        if (member == ctx.message.author or member == None):
            emb = discord.Embed(title="Wow!", description = f"For the whole chat there was a noise from {ctx.author.mention} kicking themselves into the metaverse!", color=0x5865F2)
            emb.set_thumbnail(url="http://images6.fanpop.com/image/answers/3210000/3210445_1365905041240.17res_399_300.jpg")
            await ctx.channel.send(embed=emb) 
        else:
            emb = discord.Embed(title="Wow!", description = f"For the whole chat there was a noise from {ctx.author.mention} kicking {member.mention} into the metaverse!", color=0x5865F2)
            emb.set_thumbnail(url="http://images6.fanpop.com/image/answers/3210000/3210445_1365905041240.17res_399_300.jpg")
            await ctx.channel.send(embed=emb)

def setup(bot):
    bot.add_cog(Fun(bot))#test