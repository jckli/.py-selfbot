import discord
import asyncio
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["streaming", "watching", "listening"])
    async def playing(self, ctx, *, arg1: str = None):
        """Set discord status."""
        if ctx.invoked_with == "playing":
            await self.bot.change_presence(activity=discord.Game(name=arg1))
            await ctx.send("Changed your status to playing {}".format(arg1))
        elif ctx.invoked_with == "streaming":
            await self.bot.change_presence(activity=discord.Streaming(name=arg1, url="https://www.twitch.tv/toucanee"))
            await ctx.send("Changed your status to streaming {}".format(arg1))
        elif ctx.invoked_with == "listening":
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=arg1))
            await ctx.send("Changed your status to listening {}".format(arg1))
        elif ctx.invoked_with == "watching":
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=arg1))
            await ctx.send("Changed your status to watching {}".format(arg1))

    @commands.command()
    async def removestat(self, ctx):
        """Removes discord status."""
        await self.bot.change_presence(status=discord.Status.offline, activity=None, afk=True)
        message = "Done!"
        await ctx.send(message)

    @commands.command(name='logout')
    async def _logout(self, ctx):
        """Shuts the bot down"""
        await ctx.send('`Shutting down`')
        await self.bot.logout()

def setup(bot):
    bot.add_cog(Utility(bot))