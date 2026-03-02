def main():
    print("=== Network Traffic Security Analyzer ===\n")

    port = int(input("Enter the port number (e.g., 80, 22, 443, 3389): "))
    transfer_size = int(input("Enter the data transfer size in megabytes (MB): "))
    risk = traffic_analyzer(port, transfer_size)

    print("\nFIREWALL LOG:")
    print(f"Port: {port}, Transfer Size: {transfer_size} MB")
    print(f"Risk Assessment: {risk}")
    print("------------------------")

def traffic_analyzer(port, transfer_size):
    if (port == 22 or port == 3389) and transfer_size >= 100:
        risk = "HIGH RISK: Potential unauthorized remote access detected!"
    elif port == 80 and transfer_size > 100:
        risk = "MEDIUM RISK: Large unencrypted data transfer detected."
    elif port == 443:
        risk = "LOW RISK: Secure encrypted transfer detected."
    else:
        risk = "UNKNOWN: Unrecognized traffic pattern."
        
    return risk

main()