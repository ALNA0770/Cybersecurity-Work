---

# 🛡️ Linux Enumeration & General Commands Cheat Sheet

Welcome to the **Linux Enumeration & General Commands Cheat Sheet**! This guide is tailored for penetration testers and security enthusiasts to help you enumerate and gather critical information from a Linux system after gaining access. Enumeration is crucial not only before but also after compromising a system, providing insights into potential vulnerabilities and further exploitation paths.
####  📝 Note: I learned these commands and techniques through hands-on practice and challenges on TryHackMe.com, an excellent platform for cybersecurity training and labs.


## 🔍 Enumeration Commands

### 1. **`hostname`** - Identify the Target System
   - 📛 Returns the hostname of the target machine. Useful to identify the role of the machine within the network.
   ```bash
   hostname
   ```

### 2. **`uname -a`** - Display System Information
   - 🖥️ Prints detailed system information, including the kernel version, which is useful for identifying potential kernel vulnerabilities.
   ```bash
   uname -a
   ```

### 3. **`cat /proc/version`** - Kernel and Compiler Info
   - 🔧 Provides information about the kernel version and whether a compiler like GCC is installed.
   ```bash
   cat /proc/version
   ```

### 4. **`cat /etc/issue`** - Operating System Identification
   - 🗒️ Displays the contents of the `/etc/issue` file, which usually contains the OS version. Note that this file can be customized.
   ```bash
   cat /etc/issue
   ```

### 5. **`ps` Command** - View Running Processes
   - 🔄 Shows processes running on the system.
   - **Common Options**:
     - `ps -A`: View all running processes.
     - `ps aux`: View processes for all users with detailed info.
     - `ps axjf`: View processes in a tree format.
   ```bash
   ps -A
   ps aux
   ps axjf
   ```

### 6. **`env`** - View Environment Variables
   - 🌐 Displays environment variables that could reveal useful information, such as paths to interpreters or compilers.
   ```bash
   env
   ```

### 7. **`sudo -l`** - Check Sudo Privileges
   - 🛠️ Lists all commands your user can run with `sudo`. This is key for identifying potential privilege escalation paths.
   ```bash
   sudo -l
   ```

### 8. **`ls -la`** - List Directory Contents with Details
   - 📂 Lists all files, including hidden ones, with detailed permissions. This is crucial for discovering potential hidden files.
   ```bash
   ls -la
   ```

### 9. **`id`** - View User Privileges and Groups
   - 🆔 Displays the user’s privileges and group memberships, helping you understand the user’s role on the system.
   ```bash
   id
   ```

### 10. **`cat /etc/passwd`** - Discover System Users
   - 👥 Reads the `/etc/passwd` file to list system users. Useful for identifying potential targets for privilege escalation.
   ```bash
   cat /etc/passwd
   ```

### 11. **`history`** - View Command History
   - 📜 Displays the history of commands executed, which could reveal sensitive information like passwords or important files.
   ```bash
   history
   ```

### 12. **`ifconfig`** - View Network Interfaces
   - 🌐 Displays information about the network interfaces, which is vital for network enumeration and pivoting.
   ```bash
   ifconfig
   ```

### 13. **`netstat`** - Network Connections and Ports
   - 🌍 Provides detailed information about network connections and listening ports.
   - **Common Options**:
     - `netstat -a`: Show all listening ports and established connections.
     - `netstat -l`: List only listening ports.
     - `netstat -s`: Show network usage statistics by protocol.
   ```bash
   netstat -a
   netstat -l
   netstat -s
   ```

### 14. **`find` Command** - Search for Files and Directories
   - 🔍 The `find` command is a powerful tool for searching the filesystem. It can be used to find files by name, permissions, size, etc.
   - **Common Examples**:
     - `find / -name flag1.txt`: Find a file named "flag1.txt" anywhere on the system.
     - `find / -perm 0777`: Find files with 777 permissions.
     - `find / -type f -perm -u=s`: Find files with the SUID bit set (potential for privilege escalation).
   ```bash
   find / -name flag1.txt
   find / -perm 0777
   find / -type f -perm -u=s
   ```

## 📋 General Linux Commands

### 1. **`grep`** - Search Through Text
   - 🔍 `grep` searches through text using patterns. It's often used with other commands to filter output.
   ```bash
   grep "search_term" file.txt
   ```

### 2. **`cut`** - Remove Sections from Each Line of Files
   - ✂️ `cut` can be used to extract specific columns from text files.
   ```bash
   cut -d ':' -f 1 /etc/passwd
   ```

### 3. **`sort`** - Sort Lines of Text Files
   - 📑 `sort` arranges lines of text files alphabetically or numerically.
   ```bash
   sort file.txt
   ```

### 4. **`locate`** - Find Files by Name
   - 📍 `locate` is a faster alternative to `find` for finding files by name.
   ```bash
   locate filename
   ```

Happy hacking! 🛡️
