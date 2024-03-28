# This is a script that loads in Mock Data from a CSV file and populates an Active Directory with it.
# The script is designed to be run on a Windows Server with the Active Directory Domain Services role installed.

# Import the Active Directory module
# Make sure the RSAT tools are installed on the server
Import-Module ActiveDirectory
Install-Module Microsoft.PowerShell.Security
Import-Module Microsoft.PowerShell.Security
# Load the CSV file
$users = Import-Csv -Path "C:\Users\jornt\Documents\Scripts\populateADScript\Usernames\MOCK_DATA.csv"
$ADUsers = Get-ADUser -Filter * | Select-Object Name
# Loop through each user in the CSV file
foreach ($user in $users)
{
  # Create a new user object
  $newUser = New-Object PSObject -Property @{
    first_name = $user.first_name
    last_name = $user.last_name
    email = $user.email
  }
  Write-Output "Creating user $($newUser.first_name) with email address $($newUser.email)"
  # Create the new user in Active Directory
  # If user already exists, it will skip and say that the user already exists
  if ( $ADUsers -eq $newUser.email )
  {
    Write-Output "User with email address $($newUser.email) already exists"
  } else
  {
    # If user does not exist, it will create the user
    New-ADUser -Name "$($newUser.first_name + " " +  $newUser.last_name)" -GivenName $newUser.first_name -Surname $newUser.last_name -SamAccountName $newUser.email -UserPrincipalName "$($newUser.email)@example.com" -EmailAddress $newUser.email -Enabled $true -AccountPassword  "P@ssword" 
  }
}
# Show all created users
Get-ADUser -Filter * | Format-Table Name, SamAccountName -A
