import yaml
import os
from colorama import Fore

# Load configuration from YAML file
with open('config.yaml', 'r') as file:
    data = yaml.safe_load(file)

def connect():
    print(Fore.GREEN + """
 _____ _____ _   _   _   _             
/  ___/  ___| | | | | | | |            
\ `--.\ `--.| |_| | | | | |_ __  _ __  
 `--. \`--. \  _  | | | | | '_ \| '_ \ 
/\__/ /\__/ / | | | \ \_/ / |_) | | | |
\____/\____/\_| |_/  \___/| .__/|_| |_|
                          | |          
                          |_|            
""")
    try:
        print(Fore.CYAN + "[+] Trying to Connect to the SSH server")
        server_user = data['ServerConfig']['ServerUser']
        server_ip = data['ServerConfig']['ServerIp']
        server_port = data['ServerConfig']['ServerPort']
        private_key_path = data['ServerConfig']['PrivateKeyPath']
        os.system(f"ssh -D 1080 {server_user}@{server_ip} -p {server_port} -i {private_key_path} -o PubkeyAuthentication=yes -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null")
    except Exception as e:
        print(Fore.RED + f"[*] We have an error: {e}")

connect()
