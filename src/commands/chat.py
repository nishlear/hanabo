from discord.ext import commands

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        content = message.content.lower()
        
        if content == 'vcl':
            await message.reply('osu')
        elif content == 'jztr':
            await message.channel.send('j z troi')
        elif 'du ma' in content:
            await message.channel.send('troi du ma')
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

async def setup(bot):
    await bot.add_cog(FunCommands(bot))