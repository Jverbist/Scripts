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
        exec(open('Usernames\RandomizeUsernames.py', encoding='utf-8').read())
        #capture_output = subprocess.run(["cat", "UsernamesRandomized.txt"], shell=True, capture_output=True, text=True)
        #print(capture_output.stdout)
    elif user_input == "2":
        subprocess.call(["C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe", "PowershellScripts\PopulateAD.ps1"])
        #exec(open('PowershellScripts\PopulateAD.ps1', encoding='utf-8').read())
    elif user_input == "3":
        while_bool = False
    else:
        print("Invalid input")









