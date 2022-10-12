import discord
from discord.ext import commands
class View(discord.ui.View):
    def __init__(self):
        super().__init__()
        sopurl = f"h"
        medurl = f""
        markurl = f"h"
    
        self.add_item(discord.ui.Button(label="SOPs", emoji="📃", url=sopurl, row=0))
        self.add_item(discord.ui.Button(label="Medical Document", emoji="🚑", url=medurl, row=1))
        self.add_item(discord.ui.Button(label="Marksman Document", emoji="🎯", url=markurl, row=2))

        

class docs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command() # Create a slash command
    async def docs(self, ctx):
        await ctx.respond("Here are the documents", view=View())

def setup(bot):
    bot.add_cog(docs(bot))