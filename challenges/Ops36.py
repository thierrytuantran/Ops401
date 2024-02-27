import subprocess

def banner_grabbing(target, port):
    # Banner grabbing using netcat
    print("Banner grabbing using netcat:")
    try:
        netcat_result = subprocess.check_output(["nc", "-n", "-z", "-w 1", target, str(port)])
        print(netcat_result.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e)

    # Banner grabbing using telnet
    print("\nBanner grabbing using telnet:")
    try:
        telnet_result = subprocess.check_output(["telnet", target, str(port)])
        print(telnet_result.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e)

    # Banner grabbing using Nmap
    print("\nBanner grabbing using Nmap:")
    try:
        nmap_result = subprocess.check_output(["nmap", "-p", str(port), "--script=banner", target])
        print(nmap_result.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e)

if __name__ == "__main__":
    target = input("Enter the target URL or IP address: ")
    port = int(input("Enter the port number: "))
    banner_grabbing(target, port)
