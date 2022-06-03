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
    async def slap(self, ctx, member:discord.User=None):
        if (member == ctx.message.author or member == None):
            emb = discord.Embed(title="Wow!", description = f"For the whole chat there was a noise from {ctx.author.mention} slapping themselves in the face!", color=0x5865F2)
            emb.set_thumbnail(url="https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/2I5JKRVOJUI6ZHN5BVDATVCMDQ.jpg")
            await ctx.channel.send(embed=emb) 
        else:
            emb = discord.Embed(title="Wow!", description = f"For the whole chat there was a noise from {ctx.author.mention} slapping {member.mention} in the face!", color=0x5865F2)
            emb.set_thumbnail(url="https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/2I5JKRVOJUI6ZHN5BVDATVCMDQ.jpg")
            await ctx.channel.send(embed=emb)

def setup(bot):
    bot.add_cog(Fun(bot))#test