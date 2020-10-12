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
    print("Nice!")
    exit(0)

with open("config.json", "r") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix = config["prefix"], self_bot=True)

@bot.event
async def on_ready():
    print(f"Bot is ready.\n-----------------\nLogged in as: {bot.user}\nUser ID: {bot.user.id}")
    await bot.change_presence(status=discord.Status.offline, afk=True)
    bot.default_status = "offline"

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

try:
    bot.run(config['token'], bot=False)
except Exception as err:
    print(f'Error: {err}')