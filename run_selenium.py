import os
import winrm

# Set the IP address and port of the Windows server
server_ip = '3.92.245.243'
server_port = 5985

# Set the credentials for the Windows server
username = 'Administrator'
password = '$Voc8lIJ8L?g!1LylQTTZrWjHMVr)W1%'

# Construct the WinRM URL
winrm_url = f'http://{server_ip}:{server_port}/wsman'

# Set up the WinRM session
session = winrm.Session(winrm_url, auth=(username, password))

try:
    # Execute the command on the Windows server
    response = session.run_cmd('dir')

    # Print the output
    print(response.std_out)
except winrm.exceptions.InvalidCredentialsError:
    print("The provided credentials were rejected by the server.")
except winrm.exceptions.InvalidComputerNameError:
    print(f"Unable to connect to the server at {winrm_url}. Please check the IP address and port.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
