import os
import discord
import jsonloader as jsonloader
from discord.ext import commands
from dotenv import load_dotenv
from sys import stderr


load_dotenv() # Parse .env file and load all variables found as environmental variables
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
bot = commands.Bot(command_prefix='!', help_command=None)
global guild

# Will be called when the bot is ready 
@bot.event
async def on_ready():
    global guild
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    print(f"{bot.user} has connected to guild: {guild.name}\nGuild ID: {guild.id}")

# Handles the event when a new member joins the guild
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hello, {member.name}. Welcome to {GUILD}!")

# Handles the event when a member sends a message
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == "Hello Belzebub.":
        await message.channel.send(f"Hello to you, {message.author}!")
    await bot.process_commands(message)

# Handles error-related events and writes them to err.log
@bot.event
async def on_error(event, *args, **kwargs):
    if event == "on_message":
        stderr.write(f"Unhandled message: {args[0]}\n")
    else:
        raise

# !rules
@bot.command(name="rules")
async def rules(ctx):
    embed = discord.Embed(description="**RULES**\n1) Do not disrespect each other.")
    await ctx.send(embed=embed)

@bot.command()
async def race(ctx, *, arg=None):
    if arg:
        if arg in jsonloader.race:
            raceEmbed = discord.Embed(description="**Description**\n"+jsonloader.race[arg]["Description"])
            await ctx.send(embed=raceEmbed)
        else:
            await ctx.send("Could not find a race by that name, could you please try again?")
    else:
        raceChannel = discord.utils.get(guild.text_channels, name="races")
        racesListEmbed = discord.Embed(description=f"""**List of races**:\n 1) Humans\n2) Felines\n3) Lupus\n4) Ursidae\n5) Aegir\n6) Avenio\n7) Lizarus\n8) Heilige\n9) Diablo\n
        If you would like to get more information on a race, try typing this:\n\n**!race [name-of-race]**\n
        Or, you can check out the <#{raceChannel.id}> channel!""")
        await ctx.send(embed=racesListEmbed)

@bot.command()
async def magic(ctx, *, arg=None):
    if arg:
        if arg in jsonloader.magiclist:
            magicEmbed = discord.Embed(description=f"**{arg} Description**\n"+jsonloader.magiclist[arg]["Description"])
            await ctx.send(embed=magicEmbed)
        else:
            await ctx.send("Could not find a magic by that name, try again.")


bot.run(TOKEN)




