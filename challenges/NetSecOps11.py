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

def main():
    try:
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

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

if __name__ == "__main__":
    main()
