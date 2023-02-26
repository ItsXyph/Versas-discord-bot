import discord
from discord.ext import commands
import datetime
import dotenv
import os

bot = discord.Bot()
token = dotenv.load_dotenv()

@bot.event
async def on_ready():
    print(f"We've logged in as: {bot.user}")

@bot.slash_command(name = "purge", description = "Purges a set amount of messages.")
async def purge(ctx, limit : int):
    embed = discord.Embed(color=discord.Colour.blurple(), title=f"{limit} Messages were purged.", timestamp=datetime.datetime.now())
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1048935994323370024/1079520156398653450/v-letter-logo-icon-for-business-and-company-vector.jpg")
    embed.set_author(name=bot.user.name, icon_url="https://cdn.discordapp.com/attachments/1048935994323370024/1079520156398653450/v-letter-logo-icon-for-business-and-company-vector.jpg")
    await ctx.channel.purge(limit = limit)
    await ctx.respond(embed=embed)

bot.run(os.getenv('TOKEN'))