import winrm # type: ignore

username = 'Administrator'
password = '$Voc8lIJ8L?g!1LylQTTZrWjHMVr)W1%'
server_ip = '3.81.186.24'
selenium_file_path = 'C:\\Users\\Administrator\\Downloads\\selenium_driver_code.py'

session = winrm.Session(server_ip, auth=(username, password))
response = session.run_cmd('python', [selenium_file_path])

print(response.std_out)
print(response.std_err)