import winrm

username = 'administrator'
password = 'your_windows_password'
server_ip = 'windows_server_ip'
selenium_file_path = 'C:\\Users\\Administrator\\Downloads\\selenium_driver_code.py'

session = winrm.Session(server_ip, auth=(username, password))
response = session.run_cmd('python', [selenium_file_path])

print(response.std_out)
print(response.std_err)