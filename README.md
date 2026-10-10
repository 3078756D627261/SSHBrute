# 🔐 SSHBrute - Simple SSH Password Testing Tool

[![GitHub](https://img.shields.io/badge/github-repo-3776AB?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=yellow)](https://www.python.org/)
[![Paramiko](https://img.shields.io/badge/paramiko-SSH%20library-green?style=for-the-badge&logo=python&logoColor=yellow)](https://www.paramiko.org/)
[![OS](https://img.shields.io/badge/Platform-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black")](https://img.shields.io/)
[![LAB](https://img.shields.io/badge/Security-Lab-8A2BE2?style=for-the-badge)]("https://github.com/3078756D627261/DNSBrute/")

---

## ⚠️ Disclaimer
> [!WARNING]
> Designed for **educational purposes, cybersecurity labs, and authorized security testing**, SSHBRUTE provides a simple introduction to SSH authentication and Python network programming.

---

## 📌 Overview

`SSHBRUTE` is a lightweight, command-line tool developed in Python that demonstrates SSH password authentication testing using the [Paramiko](https://www.paramiko.org/) library. The tool reads passwords from a user-provided wordlist and attempts to authenticate to an SSH server using a `specified username`. It reports authentication failures and stops when a password is accepted or an error prevents further attempts.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 SSH Authentication Testing |  Test password authentication against an SSH server |
| 📄 Wordlist Support |  Load candidate passwords from a text file |
| 🎯 Custom Target | Specify the target hostname or IP address |
| 🔌 Custom Port | Connect to SSH services running on non-standard ports |
| 👤 Custom Username | Choose the SSH account to test |
| ⚙️ Command-Line Interface | Configure the tool using simple command-line arguments |
| 🎨 Colored Output | Easily distinguish authentication failures, errors, and successful authentication |
| 🛡️ Input Validation | Check whether the specified wordlist exists and is not empty |
| ⏱️ Connection Timeout | Apply connection and authentication timeouts to prevent indefinitely hanging attempts |

---

## 📂 Project Structure

A suggested repository structure is:

```text
SSHBRUTE/
|
├── SSHBrute.py       # Main Python script
├── ssh_wordlist.txt  # Example password wordlist
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

### Example `requirements.txt`

```text
paramiko
```

You can install the dependencies listed in this file with:

```text
pip install -r requirements.txt
OR
sudo apt-get install python3-paramiko
```

---

## ⚙️ How It Works

`SSHBRUTE` follows a straightforward workflow:

1. **Parse arguments:** Read the target, port, username, and wordlist path from the command line.
2. **Display the banner:** Show the SSHBRUTE application banner.
3. **Validate the wordlist:** Check that the file exists and is not empty.
4. **Read candidates:** Load non-empty lines from the wordlist.
5. **Attempt authentication:** Use Paramiko to attempt SSH password authentication for the specified username.
6. **Handle responses:** Report authentication failures and stop if an SSH or other connection error occurs.
7. **Report success:** If authentication succeeds, display the accepted password and terminate the process.

The script uses the `paramiko.SSHClient` class to manage SSH connections.

---

## 🖥️ Example Output

The following output is `illustrative`. Actual output depends on the target server and the wordlist.

```text
╭──────────────────────────────────────────╮
│              SSHBRUTE v1.0               │
╰──────────────────────────────────────────╯

  Target : 192.168.1.100:22 
  Username : labuser 
  Wordlist : passwords.txt 
  Entries : 4

[•] Starting SSH password testing for a single username...

[x] Authentication failed : xxxx
[x] Authentication failed : yyyy
[+] FOUND: ZZZZ
```

If a candidate password is `accepted`, the script prints a success message containing that password.

---

## 🛠️ Requirements

Before using `SSHBRUTE`, ensure you have the following installed:

- Python 3.8 or later
- pip
- Paramiko

The tool is designed for environments where you have permission to test SSH authentication.

---

## 📥 Installation

### 1. Clone the repository

```text
git clone https://github.com/3078756D627261/SSHBrute.git
```

### 2. Navigate to the project directory

```text
cd SSHBRUTE
```

### 3. Install the required dependency

```text
pip install paramiko
OR
sudo apt-get install python3-paramiko
```

Alternatively, if your system uses `pip3`:

```text
pip3 install paramiko
```

### 4. Prepare a password wordlist

Create a file named `ssh_wordlist.txt` in the project directory.

Example:

```text
password123
admin123
lab-password
example-password
```

Each line should contain one candidate password.

---

## 🚀 Usage

Run the script using Python:

```text
python3 sshbrute.py
```

By default, `SSHBRUTE` uses the following settings:

| Argument | Default Value | Description |
|---|---|---|
| `-t`, `--target` | `192.168.1.1` | Target SSH server |
| `-p`, `--port` | `22` | SSH service port |
| `-u`, `--username` | `root` | SSH username |
| `-w`, `--wordlist` | `ssh_wordlist.txt` | Path to the password wordlist |

> [!IMPORTANT]
> Replace the `default target` with an SSH server you own or are explicitly authorized to test.

### Command-Line Options

Display the help menu:

```text
python3 sshbrute.py --help
```

The help menu lists the available arguments and their default values.

### Example: Specify a Target

```text
python3 sshbrute.py -t 192.168.1.100
```

This selects `192.168.1.100` as the target SSH server.

### Example: Specify a Custom Port

```text
python3 sshbrute.py -t 192.168.1.100 -p 2222
```

This configures the tool to connect to port `2222`.

### Example: Specify a Username

```text
python3 sshbrute.py -t 192.168.1.100 -u labuser
```

This selects `labuser` as the SSH username.

### Example: Specify a Wordlist

```text
python3 sshbrute.py -t 192.168.1.100 -u labuser -w passwords.txt
```

This uses `passwords.txt` as the candidate password file.

### Example: Combine All Options

```text
python3 sshbrute.py --target 192.168.1.100 --port 22 --username labuser --wordlist passwords.txt
```

---

## ⚠️ Limitations and Security Considerations

`SSHBRUTE` is an educational project, and its current implementation has several limitations.

### 1. Host Key Verification

The script uses:

```text
client.setmissinghostkeypolicy(paramiko.AutoAddPolicy())
```

This automatically accepts previously unknown SSH host keys.

> [!IMPORTANT]
> Although convenient for isolated labs, this weakens server identity verification and can expose connections to man-in-the-middle attacks. For real environments, verify host keys and use a trusted `known_hosts` file.

### 2. Connection and Authentication Failures

The script stops when it encounters an SSH error or another unexpected exception.

Possible causes include:

- An unreachable server.
- An incorrect port.
- A network timeout.
- SSH authentication restrictions.
- Server-side connection limits.
- Unsupported authentication methods.

A failed connection does not necessarily indicate an `incorrect password`.

### 3. Passwords Are Stored in Plain Text

The script prints the accepted password to the terminal.

> [!IMPORTANT]
> Avoid using real production credentials or storing sensitive output in logs, screenshots, or public repositories.

### 4. Memory Usage

The current implementation loads the entire wordlist into memory before processing it.

> [!IMPORTANT]
> For large files, reading the wordlist line by line would be more memory-efficient.

### 5. Server-Side Protections

SSH servers may implement `rate limits`, `account lockouts`, `authentication restrictions`, or `automated blocking`.

The script does not bypass these protections.

Use a controlled lab environment and follow the server administrator's testing limits.

---

## 🛡️ Defensive Recommendations

To improve SSH server security:

- Prefer SSH key-based authentication where appropriate.
- Disable password authentication when operationally feasible.
- Disable direct root login when possible.
- Use strong, unique account passwords.
- Apply rate limiting and account protection policies.
- Monitor authentication logs for suspicious activity.
- Restrict SSH access to trusted networks or approved source addresses.
- Keep the SSH server and its dependencies updated.

These measures help reduce the risk of password-guessing attacks.
