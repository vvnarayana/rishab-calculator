import winrm

# Replace with the appropriate values
target_ip = "3.92.245.243"
username = "Administrator"
password = "$Voc8lIJ8L?g!1LylQTTZrWjHMVr)W1%"

# Create a session object
session = winrm.Session(target_ip, auth=("domain\\" + username, password))

# Execute a command
response = session.run_cmd("ipconfig", ["/all"])

# Print the output of the command
print(response.std_out.decode("utf-8"))

# Execute a PowerShell script
script = """
$folderPath = "C:\Scripts"
if (!(Test-Path $folderPath)) {
    New-Item -ItemType Directory -Path $folderPath
}
"""
response = session.run_ps(script)

# Print the output of the PowerShell script
print(response.std_out.decode("utf-8"))
