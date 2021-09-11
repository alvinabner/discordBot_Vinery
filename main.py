import discord
from discord import guild
from discord.channel import VoiceChannel
from discord.ext import commands

client = commands.Bot(command_prefix="--")

@client.command()
async def p (ctx, url:str, channel):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="Special Role")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

client.run("")