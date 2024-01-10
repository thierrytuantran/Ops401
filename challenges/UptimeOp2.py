import os
import time
from datetime import datetime

def check_host_status(destination_ip):
    try:
        # Using subprocess to execute the ping command
        subprocess.run(['ping', '-c', '1', '-W', '1', destination_ip], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    destination_ip = input("Enter your Ip address: ")

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        success = check_host_status(destination_ip)

        if success:
            status = "Success"
        else:
            status = "Failure"

        print(f"{timestamp} - Destination IP: {destination_ip}, Status: {status}")

        time.sleep(2)

if __name__ == "__main__":
    main()
