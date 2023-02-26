import discord
from discord.ext import commands
import dotenv
import os

bot = discord.Bot()
token = dotenv.load_dotenv()

@bot.event
async def on_ready():
    print(f"We've logged in as: {bot.user}")

@bot.slash_command(name = "purge", description = "Purges a set amount of messages.")
async def purge(ctx, limit : int):
    await ctx.channel.purge(limit = limit)
    await ctx.send(f"{limit} messages have been deleted by {ctx.user}.")

bot.run(os.getenv('TOKEN'))