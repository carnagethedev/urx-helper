from discord import Embed
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_components import DiscordComponents, Button, ButtonStyle
from dotenv import load_dotenv
import os

load_dotenv()  # Load the variables from .env file

token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='u?', intents=intents)
slash = SlashCommand(bot, sync_commands=True)
DiscordComponents(bot)  # Initialize the DiscordComponents extension

selected_role = None

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def hello(ctx):
    await ctx.reply("**Hey!**")

@slash.slash(name="hello", description="Slash command for hello")
async def slash_hello(ctx):
    await ctx.send("**Hey!**")

@bot.command()
async def button_roles(ctx):
    await ctx.send(
        "Click the buttons to assign roles.",
        components=[
            Button(style=ButtonStyle.green, label="Minecraft⛏️", custom_id="1"),
            Button(style=ButtonStyle.blue, label="GTA V", custom_id="2"),
            Button(style=ButtonStyle.red, label="Valorant", custom_id="3"),
            Button(style=ButtonStyle.red, label="BGMI", custom_id="4"),
            Button(style=ButtonStyle.red, label="Free Fire", custom_id="5")
        ],
    )

@bot.command()
async def color_roles(ctx):
    global selected_role

    if selected_role is not None:
        await ctx.author.remove_roles(selected_role)

    await ctx.send(
        "**Choose Your Color!**",
        components=[
            Button(style=ButtonStyle.blue, label="Cyan", custom_id="6"),
            Button(style=ButtonStyle.green, label="Yellow", custom_id="7"),
            Button(style=ButtonStyle.gray, label="Black", custom_id="8"),
            Button(style=ButtonStyle.red, label="Red", custom_id="9"),
            Button(style=ButtonStyle.green, label="Lime", custom_id="10"),
        ],
    )

@bot.event
async def on_button_click(interaction):
    global selected_role
    
    if selected_role is not None:
        await interaction.user.remove_roles(selected_role)
    
    if interaction.custom_id == "1":
        role = discord.utils.get(interaction.guild.roles, name="Minecraft")
        await interaction.user.add_roles(role)
        await interaction.send(content="You have been given the Minecraft Role!")
    elif interaction.custom_id == "2":
        role = discord.utils.get(interaction.guild.roles, name="GTA V")
        await interaction.user.add_roles(role)
        await interaction.send(content="You have been given the GTA V Role!")
    elif interaction.custom_id == "3":
        role = discord.utils.get(interaction.guild.roles, name="Valorant")
        await interaction.user.add_roles(role)
        await interaction.send(content="You have been given the Valorant Role!")
    elif interaction.custom_id == "4":
        role = discord.utils.get(interaction.guild.roles, name="Bgmi")
        await interaction.user.add_roles(role)
        await interaction.send(content="You have been given the BGMI Role!")
    elif interaction.custom_id == "5":
        role = discord.utils.get(interaction.guild.roles, name="Free Fire")
        await interaction.user.add_roles(role)
        await interaction.send(content="You have been given the Free Fire Role!")
    elif interaction.custom_id == "6":
        role = discord.utils.get(interaction.guild.roles, name="Cyan")
        await interaction.user.add_roles(role)
        await interaction.send(content="You have been given the Cyan Color!")
    elif interaction.custom_id == "7":
        role = discord.utils.get(interaction.guild.roles, name="Yellow")
        await interaction.user.add_roles(role)
        await interaction.send(content="You have been given the Yellow Color!")
    elif interaction.custom_id == "8":
        role = discord.utils.get(interaction.guild.roles, name="Black")
        await interaction.user.add_roles(role)
        await interaction.send(content="You have been given the Black Color!")
    elif interaction.custom_id == "9":
        role = discord.utils.get(interaction.guild.roles, name="Red")
        await interaction.user.add_roles(role)
        await interaction.send(content="You have been given the Red Color!")
    elif interaction.custom_id == "10":
        role = discord.utils.get(interaction.guild.roles, name="Lime")
        await interaction.user.add_roles(role)
        await interaction.send(content="You have been given the Lime Color!")
    
    selected_role = role

bot.run(token)