import discord
from discord.ext import commands
from discord import slash_command


class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.slash_command()
    async def unit(self, ctx):
        """
        About Vulture International Security 
        """

        embed = discord.Embed(title=f'{self.bot.user.name} About', colour=ctx.author.colour)
        embed.add_field(name="About Vulture International Security", value="Vulture International Security was founded in November 2021 following the dissolution of our previous unit: Joint Task Force Vulture. Our Goal is to provide the best gaming experience possible by adding a reasonable amount of realism while respecting the limitations of the ARMA 3 Game engine.")

        await ctx.respond(embed=embed)


    @commands.slash_command()
    async def members(self, ctx):
        """
        Displays the current number of members. 
        """

        member_count = len(ctx.guild.members)
        embed = discord.Embed(title=f'{self.bot.user.name} Member Count', colour=ctx.author.colour)
        embed.add_field(name='The current number of members is:', value=member_count)

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(about(bot))