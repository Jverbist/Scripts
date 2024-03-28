#import subprocess
import subprocess
# Run RandomizeUsernames.py
main = """
Populate AD Script
------------------------
1. Randomize Usernames
2. Run Powershell script to populate AD
3. Exit
------------------------
"""

while_bool = True


while while_bool == True:
    print(main)
    user_input = input("Enter a number: ")
    if user_input == "1":
        # Executes RandomizeUsernames.py that randomizes usernames
        exec(open('Usernames\RandomizeUsernames.py', encoding='utf-8').read())
    elif user_input == "2":
        # Executes Powershell script that populates AD
        subprocess.Popen('powershell -command Import-Module Microsoft.PowerShell.Security')
        subprocess.call(["C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe", "PowershellScripts\PopulateAD.ps1"])
    elif user_input == "3":
        while_bool = False
    else:
        print("Invalid input")









