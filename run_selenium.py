import os
import winrm # type: ignore

username = 'Administrator'
password = '$Voc8lIJ8L?g!1LylQTTZrWjHMVr)W1%'
server_ip = '3.81.186.24'
selenium_file_dir = r'C:\Users\Administrator\Downloads'
selenium_file_name = 'selenium_driver_code.py'

session = winrm.Session(server_ip, auth=(username, password), transport='ntlm')

# Construct the full file path
selenium_file_path = os.path.join(selenium_file_dir, selenium_file_name)

# Change the current working directory on the remote server
response = session.run_cmd('cd', [selenium_file_dir])
if response.status_code != 0:
    print(f"Error changing directory: {response.std_err}")
else:
    # Execute the Python script
    response = session.run_cmd('python', [selenium_file_name])
    print(response.std_out)
    print(response.std_err)