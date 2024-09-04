# 🚀 NetManage Pro

### Advanced IPv6 & IPv4 Network Management Tool

**NetManage Pro** is a comprehensive and powerful tool designed to simplify the management of IPv6 and IPv4 addresses, network interfaces, VLANs, routing configurations, and firewall rules. Whether you are a network administrator, DevOps engineer, or IT professional, NetManage Pro offers the features you need for generating, configuring, and monitoring networks.

---

## 📝 Features Overview

NetManage Pro includes a wide range of professional features that are useful for managing both small and large network infrastructures. The following features are included:

### 🎯 Key Features:

1. **IPv6 & IPv4 Address Generation**  
   Easily generate multiple random or sequential IPv6 and IPv4 addresses for use in your network configurations.

2. **EUI-64 Address Generation**  
   Generate IPv6 addresses based on EUI-64 (derived from MAC addresses) for interface identifiers.

3. **Save Addresses in Multiple Formats**  
   Save generated addresses in text, JSON, or CSV formats for further use or documentation.

4. **Execute Remote Commands via SSH**  
   Execute network-related commands on remote systems using secure SSH connections.

5. **Network Interface Status Monitoring**  
   Monitor the status of your network interfaces and ensure they are functioning correctly.

6. **Add/Remove IPv6 Addresses to/from Interfaces**  
   Dynamically add or remove IPv6 addresses from network interfaces.

7. **VLAN Configuration**  
   Configure VLANs to manage network segmentation and routing efficiently.

8. **Real-Time IPv6 Address Monitoring**  
   Ping IPv6 addresses in real-time to verify their availability and connectivity.

9. **Email Alerts for Network Events**  
   Send email notifications or alerts to administrators when critical events occur in the network.

10. **Backup and Restore Network Configurations**  
    Easily backup and restore network configurations to/from a tarball file for disaster recovery.

11. **Web-Based Dashboard**  
    Access a simple web dashboard to view real-time network status and address statistics.

12. **Firewall Rule Configuration**  
    Set up or modify firewall rules for IPv6 traffic to secure your network.

---

## 📦 Installation

### Prerequisites

1. **Python 3.x**
2. **pip (Python package installer)**
3. **Dependencies**: You can install all necessary packages using `pip`:

```
pip install paramiko smtplib flask ipaddress
```

### Clone the Repository
Clone the NetManage Pro repository from GitHub:

```
git https://github.com/xONEIROS/NetManage-Pro.git
cd netmanage-pro
```

---

## 🚀 Usage Instructions

To run the tool, simply execute the `main.py` script:

```
python main.py
```

The main menu will be displayed, where you can choose from the available options. Each feature is described below:

---

## 📋 Main Menu Options

### 1. **Generate IPv6/IPv4 Addresses**  
   - **Description**: Generates random IPv6 or IPv4 addresses based on the selected version.
   - **Usage**:  
     - Select whether to generate IPv4 or IPv6 addresses.
     - Enter the number of addresses you want to generate.
     - If IPv6, enter the prefix (e.g., `2001:db8::/64`).
   - **Example**:  

```
IPv4 or IPv6 (v4/v6)? v6
Enter IPv6 prefix (e.g., 2001:db8::/64): 2001:db8::/64
Enter the number of addresses to generate: 5
```

### 2. **Generate EUI-64 IPv6 Addresses**  
   - **Description**: Generates IPv6 addresses based on the EUI-64 format (using MAC addresses).
   - **Usage**:  
     - Enter the MAC address and IPv6 prefix.
     - The tool will generate the corresponding EUI-64 IPv6 address.
   - **Example**:  
```
Enter MAC address (e.g., 00:1A:2B:3C:4D:5E): 00:1A:2B:3C:4D:5E
Enter IPv6 prefix (e.g., 2001:db8::/64): 2001:db8::/64
```

### 3. **Save Addresses (Text, JSON, CSV)**  
   - **Description**: Saves the generated addresses in a format of your choice (text, JSON, or CSV).
   - **Usage**:  
     - After generating addresses, select the file format and specify the filename.
   - **Example**:  
```
Enter filename to save: my_ipv6_addresses
Choose format (text/json/csv): json
```

### 4. **Execute SSH Command**  
   - **Description**: Runs a command on a remote server over SSH.
   - **Usage**:  
     - Enter the remote server’s details (IP, username, password) and the command to be executed.
   - **Example**:  
```
Enter SSH host: 192.168.1.100
Enter SSH username: admin
Enter SSH password: ********
Enter command to execute: ip addr show
```

### 5. **Check Network Interface Status**  
   - **Description**: Displays the status of network interfaces on the system.
   - **Usage**:  
     - Enter the interface names (comma-separated) to monitor.
   - **Example**:  
```
Enter interfaces (comma-separated): eth0, eth1
```

### 6. **Add/Remove IPv6 Addresses on Interface**  
   - **Description**: Dynamically adds or removes IPv6 addresses from network interfaces.
   - **Usage**:  
     - Specify the interface(s) and select whether to add or remove the addresses.
   - **Example**:  
```
Enter interfaces (comma-separated): eth0
```

### 7. **Configure VLAN**  
   - **Description**: Configures a VLAN on the selected network interface.
   - **Usage**:  
     - Specify the interface and VLAN ID.
   - **Example**:  
```
Enter interface: eth0
Enter VLAN ID: 10
```

### 8. **Monitor IPv6 Address Real-Time**  
   - **Description**: Pings an IPv6 address to check its connectivity.
   - **Usage**:  
     - Enter the IPv6 address to monitor.
   - **Example**:  
```
Enter IPv6 address to monitor: 2001:db8::1
```

### 9. **Send Alert Email**  
   - **Description**: Sends an alert email to the recipient when specific events occur.
   - **Usage**:  
     - Enter the subject, message, and recipient’s email.
   - **Example**:  
```
Enter email subject: Network Alert
Enter email message: Interface eth0 is down!
Enter recipient email: admin@example.com
```

### 10. **Backup/Restore Network Configurations**  
   - **Description**: Backs up or restores network configurations.
   - **Usage**:  
     - Choose between backup or restore and provide the filename.
   - **Example**:  
```
Backup or Restore (backup/restore): backup
Enter backup filename: network_backup
```

### 11. **Open Web Dashboard**  
   - **Description**: Opens a simple web dashboard to view network statistics.
   - **Usage**:  
     - Open a web browser and go to `http://localhost:5000` to view the dashboard.
   - **Example**:  
```
Visit http://localhost:5000 to view the dashboard.
```

---

## 🛠 Advanced Features

- **Firewall Rule Configuration**: Manage firewall rules for IPv6 traffic using `ip6tables`.
- **Email Alerts for Network Events**: Set up automated email notifications for critical network events.
- **SSH Integration**: Remotely manage network devices and execute commands using SSH.
- **Backup & Restore**: Create backups of network configurations and restore them when needed.
- **VLAN Configuration**: Easily configure VLANs for network segmentation.

---

## 📊 Web-Based Dashboard

To access the **web-based dashboard**, run the following command:

```
python main.py
```

Then, open your browser and go to:

```
http://localhost:5000
```

You will see real-time network statistics, including the total number of addresses, active addresses, and inactive addresses.

---


## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Feel free to modify the documentation further according to your project's specific needs!

