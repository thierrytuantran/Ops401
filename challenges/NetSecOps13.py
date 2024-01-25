import pandas as pd
from scapy.all import *
def is_host_up(ip):
    icmp = IP(dst=ip)/ICMP()
    resp = sr1(icmp, timeout=10, verbose=0)
    if resp is None:
        return False
    elif resp.haslayer(ICMP):
        return True
    else:
        return False
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

def perform_port_scan(ip, start_port, end_port):
    if is_host_up(ip):
        scan_results = []
        for port in range(start_port, end_port + 1):
            status = scan_port(ip, port)
            scan_results.append((port, status))
            print(f"Port {port}: {status}")
        export_results(scan_results, f"{ip}_scan_results")
        print("Port scan complete.")
    else:
        print(f"{ip} is down or not responding to ICMP.")
def main():
    target_ip = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    perform_port_scan(target_ip, start_port, end_port)

if __name__ == "__main__":
    main()
