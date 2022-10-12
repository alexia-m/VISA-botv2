import discord
import asyncio
from discord import slash_command

from discord.ext import commands
import a2s
from asyncio import TimeoutError 
game_map = "Select a Mission"
player_count = 0
maxp = 40
ping_stat = 0
ping = 0
serverstatus = "Online"
class server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.slash_command()
    async def server(self, ctx):
        global game_map
        global player_count
        global maxp
        global ping_stat
        global ping
        serverstatus = "Online"
        """
        Displays Server Stats
        """
        address = ('',2303)
        try:
            server = a2s.info(address)
        except:
            if (ConnectionRefusedError, TimeoutError):
                serverstatus = "Offline"
    
        if serverstatus =="Offline":
            embed = discord.Embed(title=f'{self.bot.user.name} Server Status', colour=ctx.author.colour)
            embed.add_field(name='Server Status', value="Offline",inline=False)
        
        else:
            name = server.server_name
            game_map = server.map_name
            player_count = server.player_count
            max = server.max_players
            ping = server.ping
            ping_stat=round(ping, ndigits=3)
        
        if game_map == '':
            game_map = "Selecting a Mission"
    
        if serverstatus == "Online":
            embed = discord.Embed(title=f'{self.bot.user.name} Server Status', colour=ctx.author.colour)
            embed.add_field(name="Server Status", value=serverstatus,inline=False)
            embed.add_field(name='Map', value=game_map,inline=False)
            embed.add_field(name='Players', value=f"{player_count}/{max}",inline=False)
            embed.add_field(name='Ping in seconds', value=ping_stat,inline=False)
            embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
    
        await ctx.respond(embed=embed)
        
    @commands.slash_command()
    async def connect(self, ctx):
        """
        Direct connect to the servers
        May not work properly
        WIP
        """
        TSURL = f''
        steamURL = f'
        embed = discord.Embed(title=f'{self.bot.user.name} Server Direct Connections', colour=ctx.author.colour)
        embed.add_field(name="Arma Server Direct Connect", value=steamURL,inline=False)
        embed.add_field(name="TeamSpeak Server Direct Connect", value=TSURL,inline=False)
        embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(server(bot))