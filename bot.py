import discord
import json
import os
from discord.ext import commands

with open("config.json", "r") as f:
    config = json.load(f)

client = commands.Bot(command_prefix = config["prefix"], self_bot=True)
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def status(ctx, arg1, arg2):
    """Please enter correct context."""
    if "playing" in arg1:
        await client.change_presence(activity=discord.Game(name=arg2))
        await ctx.send("Changed your status to {} {}".format(arg1, arg2))
    elif "stream" in arg1:
        await client.change_presence(activity=discord.Streaming(name=arg2, url="https://www.twitch.tv/toucanee"))
        await ctx.send("Changed your status to {} {}".format(arg1, arg2))
    elif "listening" in arg1:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=arg2))
        await ctx.send("Changed your status to {} {}".format(arg1, arg2))
    elif "watching" in arg1:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=arg2))
        await ctx.send("Changed your status to {} {}".format(arg1, arg2))

client.run(config["token"], bot=False)