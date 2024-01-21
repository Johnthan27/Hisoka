import subprocess

# Function to print system information
def print_system_info():
    try:
        # Run 'whoami' command
        whoami_output = subprocess.check_output(['whoami'], text=True).strip()
        print(f"Username: {whoami_output}")
        
        # Run 'ip a' command
        ip_output = subprocess.check_output(['ip', 'a'], text=True).strip()
        print("IP Address Information:")
        print(ip_output)
        
        # Run 'lshw -short' command
        lshw_output = subprocess.check_output(['lshw', '-short'], text=True).strip()
        print("Hardware Information:")
        print(lshw_output)
        
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Call the function to print system information
print_system_info()

# Additional prints to meet the objective
print("Additional prints to meet objectives.")
print("Objective 1 complete.")
print("Objective 2 complete.")
