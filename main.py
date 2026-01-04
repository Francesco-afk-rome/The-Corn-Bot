import discord
from discord import app_commands
import os

# Get your bot token from Render environment variable
TOKEN = os.getenv("DISCORD_TOKEN")

class CornBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Sync slash commands
        await self.tree.sync()
        print("Slash commands synced")

bot = CornBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (The Corn Bot)")

# ===== /gif COMMAND =====
@bot.tree.command(name="gif", description="Send gifs")
async def gif(interaction: discord.Interaction):
    # Ephemeral message only you see
    await interaction.response.send_message("Command Executed", ephemeral=True)

    # GIFs you want to send
    gifs = [
        "https://cdn.discordapp.com/attachments/1364830848846925854/1457500321956888690/togif.gif?ex=695c3a73&is=695ae8f3&hm=1528eb98a85378c80ebde3dcbc84d9c7af66cee1a5e416e395300f4985af83d8&",
        "https://cdn.discordapp.com/attachments/1364830848846925854/1457500612341137539/togif.gif?ex=695c3ab9&is=695ae939&hm=9d388944a514fd592d0b31e916ada2d31e2d6388d0a3e744c2131431b098075c&",
        "https://cdn.discordapp.com/attachments/1364830848846925854/1457504672666619926/togif.gif?ex=695c3e81&is=695aed01&hm=b17f388cd9c5fdf9f8a73eca38dac6d2209c2692e5ca674f0eb2b8b98f69b9aa&",
        "https://cdn.discordapp.com/attachments/1364830848846925854/1457500929115816089/togif.gif?ex=695c3b04&is=695ae984&hm=83385d8f18c5f67e5bf97a05e79a80ac2ab0714a0d7bcf5ecf54ddd356a1cd43&",
        "https://cdn.discordapp.com/attachments/1364830848846925854/1457501194053226587/togif.gif?ex=695c3b43&is=695ae9c3&hm=5d05e55069123f06eabc89b88a34c35eada38c331d28a76e710b8a0ddbffc314&",
    ]

    # Combine all GIF URLs into one message
    message_content = "\n".join(gifs)

    # Send that message 5 times
    for _ in range(5):
        await interaction.channel.send(message_content)

# ===== /say COMMAND =====
@bot.tree.command(name="say", description="Make the bot say something")
@app_commands.describe(message="What the bot should say")
async def say(interaction: discord.Interaction, message: str):
    # Delete the user's slash command immediately
    await interaction.delete_original_response()
    
    # Send the message you typed
    await interaction.channel.send(message)

# Run the bot
bot.run(TOKEN)
