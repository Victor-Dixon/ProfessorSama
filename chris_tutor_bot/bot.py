"""
Chris Tutor Bot — Main Entry Point
Run with: python bot.py
"""

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ {bot.user} is online and ready!")
    await bot.load_extension("cogs.quiz")
    await bot.load_extension("cogs.progress")
    await bot.load_extension("cogs.homework")
    await bot.load_extension("cogs.help_cmd")


bot.run(TOKEN)
