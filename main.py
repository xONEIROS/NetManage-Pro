import os
import random
import ipaddress
import logging
import paramiko
import smtplib
from flask import Flask, jsonify, render_template
from datetime import datetime


logging.basicConfig(filename=os.path.expanduser("~/netmanage_pro.log"),
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

def validate_prefix(prefix):
    try:
        prefix_network = ipaddress.IPv6Network(prefix, strict=False)
        if not (16 <= prefix_network.prefixlen <= 64):
            raise ValueError("Prefix length must be between /16 and /64")
        return prefix_network
    except ValueError as e:
        logging.error(f"Invalid IPv6 prefix: {e}")
        raise ValueError("Invalid IPv6 prefix provided.")

def generate_ipv6_addresses_random(prefix_network, count):
    addresses = set()
    while len(addresses) < count:
        suffix = random.getrandbits(128 - prefix_network.prefixlen)
        ip = prefix_network.network_address + suffix
        addresses.add(ip)
    return addresses

def generate_ipv4_addresses(count):
    addresses = set()
    while len(addresses) < count:
        suffix = random.getrandbits(32)
        ip = ipaddress.IPv4Address(suffix)
        addresses.add(ip)
    return addresses

def generate_eui64_address(mac, prefix):
    mac_parts = mac.split(":")
    mac_parts[0] = format(int(mac_parts[0], 16) ^ 0x02, '02x')
    mac_eui64 = mac_parts[:3] + ['ff', 'fe'] + mac_parts[3:]
    eui64 = ":".join(mac_eui64[i] + mac_eui64[i + 1] for i in range(0, len(mac_eui64), 2))
    return ipaddress.IPv6Address(prefix.network_address) + ipaddress.IPv6Address(eui64)
def save_to_file(addresses, filename, output_format="text"):
    if output_format == "text":
        with open(filename, 'w') as file:
            for address in addresses:
                file.write(str(address) + '\n')
    elif output_format == "json":
        import json
        with open(filename, 'w') as file:
            json.dump([str(address) for address in addresses], file, indent=2)
    elif output_format == "csv":
        import csv
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            for address in addresses:
                writer.writerow([str(address)])
    logging.info(f"Saved {len(addresses)} addresses to {filename} in {output_format} format.")
def execute_ssh_command(host, user, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    ssh.close()
    return stdout.read().decode('utf-8')
def generate_up_down_scripts(addresses, interfaces, home_directory):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    up_script_path = os.path.join(home_directory, f"up_ipv6_addr_{timestamp}.sh")
    down_script_path = os.path.join(home_directory, f"down_ipv6_addr_{timestamp}.sh")

    with open(up_script_path, 'w') as up_file, open(down_script_path, 'w') as down_file:
        for interface in interfaces:
            for address in addresses:
                up_file.write(f"ip -6 addr add {address} dev {interface}\n")
                down_file.write(f"ip -6 addr del {address} dev {interface}\n")

    logging.info(f"Scripts generated: {up_script_path}, {down_script_path}")

def check_interface_status(interfaces):
    for interface in interfaces:
        os.system(f"ip -6 addr show dev {interface}")
        logging.info(f"Checked status for interface: {interface}")

def send_alert_email(subject, message, recipient):
    smtp = smtplib.SMTP('smtp.your-email.com', 587)
    smtp.starttls()
    smtp.login('your-email', 'password')
    message = f"Subject: {subject}\n\n{message}"
    smtp.sendmail('your-email', recipient, message)
    smtp.quit()

@app.route('/')
def dashboard():
    ipv6_data = {
        'total_addresses': 100,
        'active_addresses': 80,
        'inactive_addresses': 20
    }
    return render_template('dashboard.html', data=ipv6_data)

def main_menu():
    while True:
        print("\nNetManage Pro - Main Menu")
        print("1. Generate IPv6/IPv4 Addresses")
        print("2. Generate EUI-64 IPv6 Addresses")
        print("3. Save Addresses (Text, JSON, CSV)")
        print("4. Execute SSH Command")
        print("5. Check Network Interface Status")
        print("6. Add/Remove IPv6 Addresses on Interface")
        print("7. Configure VLAN")
        print("8. Monitor IPv6 Address Real-time")
        print("9. Send Alert Email")
        print("10. Backup/Restore Network Configurations")
        print("11. Open Web Dashboard")
        print("12. Exit")

        choice = input("Select an option (1-12): ")

        if choice == "1":
            count = int(input("Enter the number of addresses to generate: "))
            version = input("IPv4 or IPv6 (v4/v6)? ").lower()
            if version == "v6":
                prefix = input("Enter IPv6 prefix (e.g., 2001:db8::/64): ")
                prefix_network = validate_prefix(prefix)
                addresses = generate_ipv6_addresses_random(prefix_network, count)
                print(f"Generated IPv6 Addresses: {addresses}")
            elif version == "v4":
                addresses = generate_ipv4_addresses(count)
                print(f"Generated IPv4 Addresses: {addresses}")
        elif choice == "2":
            mac = input("Enter MAC address (e.g., 00:1A:2B:3C:4D:5E): ")
            prefix = input("Enter IPv6 prefix (e.g., 2001:db8::/64): ")
            prefix_network = validate_prefix(prefix)
            eui64_address = generate_eui64_address(mac, prefix_network)
            print(f"Generated EUI-64 IPv6 Address: {eui64_address}")
        elif choice == "3":
            filename = input("Enter filename to save: ")
            output_format = input("Choose format (text/json/csv): ").lower()
            save_to_file(addresses, filename, output_format)
        elif choice == "4":
            host = input("Enter SSH host: ")
            user = input("Enter SSH username: ")
            password = input("Enter SSH password: ")
            command = input("Enter command to execute: ")
            output = execute_ssh_command(host, user, password, command)
            print(f"Command Output: {output}")
        elif choice == "5":
            interfaces = input("Enter interfaces (comma separated): ").split(',')
            check_interface_status(interfaces)
        elif choice == "6":
            interfaces = input("Enter interfaces (comma separated): ").split(',')
            generate_up_down_scripts(addresses, interfaces, os.path.expanduser("~"))
        elif choice == "7":
            interface = input("Enter interface: ")
            vlan_id = input("Enter VLAN ID: ")
            configure_vlan(interface, vlan_id)
        elif choice == "8":
            address = input("Enter IPv6 address to monitor: ")
            if ping_ipv6_address(address):
                print(f"IPv6 Address {address} is active.")
            else:
                print(f"IPv6 Address {address} is not responding.")
        elif choice == "9":
            subject = input("Enter email subject: ")
            message = input("Enter email message: ")
            recipient = input("Enter recipient email: ")
            send_alert_email(subject, message, recipient)
        elif choice == "10":
            action = input("Backup or Restore (backup/restore): ").lower()
            filename = input("Enter backup filename: ")
            if action == "backup":
                backup_settings(filename)
            elif action == "restore":
                restore_settings(filename)
        elif choice == "11":
            app.run(debug=True)
        elif choice == "12":
            print("Exiting NetManage Pro.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main_menu()
