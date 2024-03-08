# Import Active Directory module
Import-Module ActiveDirectory

# Function to create user accounts in Active Directory
function Create-ADUser {
    param(
        [string]$Username,
        [string]$Domain
    )
    
    # Define user properties
    $UserParams = @{
        SamAccountName    = $Username
        UserPrincipalName = "$Username@$Domain"
        Name              = $Username
        GivenName         = $Username
        Surname           = "Lastname"  # Change as needed
        AccountPassword   = (ConvertTo-SecureString -AsPlainText "Password123!" -Force)  # Set initial password
        Enabled           = $true
    }

    # Create user account
    New-ADUser @UserParams -PassThru
}

# Read randomized usernames from file
$usernames = Get-Content -Path "../UsernamesRandomized.txt"

# Get domain name from user input
$Domain = Read-Host "Enter your domain name (e.g., example.com)"

# Create users in Active Directory
foreach ($username in $usernames) {
    # Trim leading/trailing whitespace and create user
    $trimmedUsername = $username.Trim()
    Create-ADUser -Username $trimmedUsername -Domain $Domain
}

Write-Host "User creation completed."