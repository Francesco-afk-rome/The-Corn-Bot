import discord
from discord import app_commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")  # Render environment variable

class CornBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("Slash commands synced")

bot = CornBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (The Corn Bot)")

# /gif command
@bot.tree.command(name="gif", description="Send gifs")
async def gif(interaction: discord.Interaction):
    await interaction.response.send_message("Command Executed", ephemeral=True)

    gifs = [
        "https://cdn.discordapp.com/attachments/1364830848846925854/1457500321956888690/togif.gif?ex=695c3a73&is=695ae8f3&hm=1528eb98a85378c80ebde3dcbc84d9c7af66cee1a5e416e395300f4985af83d8&",
        "https://cdn.discordapp.com/attachments/1364830848846925854/1457500612341137539/togif.gif?ex=695c3ab9&is=695ae939&hm=9d388944a514fd592d0b31e916ada2d31e2d6388d0a3e744c2131431b098075c&",
        "https://cdn.discordapp.com/attachments/1364830848846925854/1457500929115816089/togif.gif?ex=695c3b04&is=695ae984&hm=83385d8f18c5f67e5bf97a05e79a80ac2ab0714a0d7bcf5ecf54ddd356a1cd43&",
        "https://discord.com/channels/@me/1364830848846925854/1457501191926841499",
        "https://cdn.discordapp.com/attachments/1364830848846925854/1457501532085031147/togif.gif?ex=695c3b94&is=695aea14&hm=65b99ebf78c36f0663a45d3200eaab6aa86431ae5aa4c421586d97865ca344bd&",
    ]

    for gif_url in gifs:
        await interaction.channel.send(gif_url)

# /say command
@bot.tree.command(name="say", description="Make the bot say something")
@app_commands.describe(message="What the bot should say")
async def say(interaction: discord.Interaction, message: str):
    await interaction.response.defer(ephemeral=True)
    await interaction.channel.send(message)
    await interaction.delete_original_response()

bot.run(TOKEN)
