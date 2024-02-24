import subprocess

def disable_firewall():
    try:
        subprocess.run(["netsh", "advfirewall", "set", "allprofiles", "state", "off"], check=True)
        print("Firewall disabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to disable firewall: {e}")

if __name__ == "__main__":
    disable_firewall()
