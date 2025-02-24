def show_help():
    help_text = """
Available commands:
/help      - Show this help message
/exit      - Exit the program
"""
    print(help_text)

banner = """  
___   ___   _________  ______     ___   ___   ________   ______    ______    ______   __       ______                                                    
/__/\ /__/\ /________/\/_____/\   /__/\ /__/\ /_______/\ /_____/\  /_____/\  /_____/\ /_/\     /_____/\                                                   
\::\ \\  \ \\__.::.__\/\:::_ \ \  \::\ \\  \ \\::: _  \ \\:::_ \ \ \:::_ \ \ \:::_ \ \\:\ \    \:::_ \ \                                                  
 \::\/_\ .\ \  \::\ \   \:(_) \ \  \::\/_\ .\ \\::(_)  \ \\:(_) ) )_\:(_) ) )_\:\ \ \ \\:\ \    \:\ \ \ \                                                 
  \:: ___::\ \  \::\ \   \: ___\/   \:: ___::\ \\:: __  \ \\: __ `\ \\: __ `\ \\:\ \ \ \\:\ \____\:\ \ \ \                                                
   \: \ \\::\ \  \::\ \   \ \ \      \: \ \\::\ \\:.\ \  \ \\ \ `\ \ \\ \ `\ \ \\:\_\ \ \\:\/___/\\:\/.:| |                                               
    \__\/ \::\/   \__\/    \_\/       \__\/ \::\/ \__\/\__\/ \_\/ \_\/ \_\/ \_\/ \_____\/ \_____\/ \____/_/                                               

                          Made by: Anas, Peter, Klaas
"""

print(banner)
show_help()
import subprocess

while True:
    command = input("Enter command: ").strip().lower()
    
    if command == "/help":
        show_help()
    elif command == "/exit":
        print("Exiting program...")
        break
    else:
        print("Unknown command. Type /help for available commands.")

def manage_firewall(action):
    powershell_commands = {
        "disable": "Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False",
        "enable": "Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True",
        "status": "Get-NetFirewallProfile | Select-Object Name, Enabled"
    }

    if action not in powershell_commands:
        print("Ongeldige actie! Gebruik: 'enable', 'disable' of 'status'.")
        return

    command = f"powershell -Command \"{powershell_commands[action]}\""
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Fout bij het uitvoeren van het commando:", result.stderr)

manage_firewall("status")  