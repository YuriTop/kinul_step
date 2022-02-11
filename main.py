import discord
from discord.ext import commands
from modules.config import Config
from os import listdir

bot = commands.Bot(command_prefix='crashed.')

if __name__ == '__main__':
    bot.load_extension('cogs.crasher')

bot.run("ODY5ODIwNzI2NzM0MDk0Mzg3.YQDxrQ.9PL4nQtMryEen3f0HH4huR-Em-o")
