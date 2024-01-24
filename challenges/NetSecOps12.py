import pandas as pd
from scapy.all import *

def scan_port(ip, port):
    try:
        pkt = IP(dst=ip) / TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=2, verbose=0)

        if resp is None:
            return port, "Filtered"
        elif resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x12:  # SYN-ACK
                sr(IP(dst=ip) / TCP(dport=port, flags="R"), timeout=1, verbose=0)
                return port, "Open"
            elif resp.getlayer(TCP).flags == 0x14:  # RST-ACK
                return port, "Closed"
        return port, "Unknown"
    except KeyboardInterrupt:
        return port, "Interrupted"

def export_results(scan_results, filename):
    df = pd.DataFrame(scan_results, columns=["Port", "Status"])
    df.to_csv(f"{filename}.csv", index=False)

def icmp_ping_sweep(cidr):
    network = ip_network(cidr)
    online_hosts = 0
    for host in network.hosts():
        # Sending ICMP echo request to the host
        resp = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
        if resp is None:
            print(f"{host} is down or not responding.")
        elif (int(resp.getlayer(ICMP).type) == 3 and
              int(resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]):
            print(f"{host} is actively blocking ICMP traffic.")
        else:
            print(f"{host} is responding.")
            online_hosts += 1
    print(f"\nTotal online hosts: {online_hosts}")
def user_menu():
    while True:
        choice = input("Choose mode: 1- TCP Port Scanner, 2- ICMP Ping Sweep, 3- Exit: ")
        if choice == '1':
            # Run TCP Port Scanner
            pass
        elif choice == '2':
            # Run ICMP Ping Sweep
            cidr = input("Enter CIDR block (e.g., 192.168.1.0/24): ")
            icmp_ping_sweep(cidr)
        elif choice == '3':
            break
def main():
    while True:
        print("\nNetwork Security Tool")
        print("1. TCP Port Range Scanner")
        print("2. ICMP Ping Sweep")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            target_ip = input("Enter target IP: ")
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))
            scan_results = []
            print("Scanning ports...")
            for port in range(start_port, end_port + 1):
                result = scan_port(target_ip, port)
                scan_results.append(result)
            export_results(scan_results, "scan_results")
            print("Scan results exported successfully.")

        elif choice == '2':
            cidr = input("Enter CIDR block (e.g., 192.168.1.0/24): ")
            icmp_ping_sweep(cidr)

        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
