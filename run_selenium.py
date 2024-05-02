import os
import winrm # type: ignore

# Set up the WinRM session
session = winrm.Session('http://3.81.186.24:5985/wsman', auth=('Administrator', '$Voc8lIJ8L?g!1LylQTTZrWjHMVr)W1%'))

# Execute the command
response = session.run_cmd('dir')

# Print the output
print(response.std_out)