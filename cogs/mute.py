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
    async def mute(self, ctx, member: discord.Member, time, reason=None):
        desctime = time
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")
        time_convert = {"s":1, "m":60, "h":3600, "d":86400, "w":604800, "mo":18144000, "y":31536000}
        tempmute = int(time[:-1]) * time_convert[time[-1]]
        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")
            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        embed = discord.Embed(title=f"**{member}** was muted for **{desctime}**", color=0x5865F2)
        embed.add_field(name="reason:", value=reason, inline=True)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await asyncio.sleep(tempmute)
        await member.remove_roles(mutedRole)

def setup(bot):
    bot.add_cog(Moderation(bot))
#test