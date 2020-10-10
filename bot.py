import discord
import json
import os
import argparse
from discord.ext import commands

def parse_cmd_arguments():  # allows for arguments
    parser = argparse.ArgumentParser(description="Discord-Selfbot")
    parser.add_argument("-test", "--test-run",  # test run flag for Travis
                        action="store_true",
                        help="Makes the bot quit before trying to log in")
    parser.add_argument("--force-mac",  # Allows for Testing of mac related code
                        action="store_true",
                        help="Forces to run the Mac checks")
    parser.add_argument("--reset-config",  # Allows for Testing of mac related code
                        action="store_true",
                        help="Reruns the setup")
    parser.add_argument("-s", "--silent",  # Allows for Testing of mac related code
                        action="store_true",
                        help="Supresses all errors")
    return parser

args = parse_cmd_arguments().parse_args()
_test_run = args.test_run
_force_mac = args.force_mac
_reset_cfg = args.reset_config
_silent = args.silent
_force_admin = False

if _test_run:
    print("Quitting: test run")
    exit(0)

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