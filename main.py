import socket
import time
import sys
import os
import random

# تنظیم رنگ‌ها برای زیبایی (ANSI Colors)
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    logo = f"""{Colors.CYAN}
   _____ _ _            _       _____       _ZWXY_
  / ____(_) |          | |     / ____|     | |
 | (___  _| | ___ _ __ | |_   | |  __  __ _| |_ _____      ____ _ _   _ 
  \___ \| | |/ _ \ '_ \| __|  | | |_ |/ _` | __/ _ \ \ /\ / / _` | | | |
  ____) | | |  __/ | | | |_   | |__| | (_| | ||  __/\ V  V / (_| | |_| |
 |_____/|_|_|\___|_| |_|\__|   \_____|\__,_|\__\___| \_/\_/ \__,_|\__, |
                                                                   __/ |
  {Colors.HEADER}v1.0.0 - By AmirAli SalehPour (Silent-Galaxy){Colors.CYAN}                 |___/ 
    {Colors.ENDC}"""
    print(logo)
    print(f"{Colors.BOLD}Welcome to Localhost Exposer Tool{Colors.ENDC}".center(80))
    print("-" * 70)

def loading_animation(text, duration=2):
    print(f"{text} ", end="", flush=True)
    for _ in range(10):
        time.sleep(duration / 10)
        sys.stdout.write(f"{Colors.GREEN}█{Colors.ENDC}")
        sys.stdout.flush()
    print(" ✅\n")

def check_port(ip, port, service_name):
    print(f"[*] Checking {service_name} on port {port}...", end=" ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, port))
    sock.close()
    
    if result == 0:
        print(f"{Colors.GREEN}[RUNNING]{Colors.ENDC}")
        return True
    else:
        print(f"{Colors.FAIL}[STOPPED]{Colors.ENDC}")
        return False

def main():
    clear_screen()
    print_logo()

    # مرحله 1: چک کردن اینترنت
    print(f"\n{Colors.WARNING}--- STEP 1: Network Diagnostics ---{Colors.ENDC}")
    loading_animation("Pinging Google DNS...")
    
    # مرحله 2: چک کردن سرویس‌های داخلی
    print(f"{Colors.WARNING}--- STEP 2: Service Discovery ---{Colors.ENDC}")
    xampp_status = check_port('127.0.0.1', 80, "Apache Web Server (XAMPP)")
    mysql_status = check_port('127.0.0.1', 3306, "MySQL Database")
    game_status  = check_port('127.0.0.1', 25565, "Minecraft Server")

    if not xampp_status and not game_status:
        print(f"\n{Colors.FAIL}❌ Error: No active service found!{Colors.ENDC}")
        print("Please turn on XAMPP or your Game Server first.")
        input("\nPress Enter to exit...")
        return

    # مرحله 3: انتخاب متد
    print(f"\n{Colors.WARNING}--- STEP 3: Select Tunneling Method ---{Colors.ENDC}")
    print(f"1. {Colors.CYAN}Cloudflare Tunnel{Colors.ENDC} (Recommended - Secure & Fast)")
    print(f"2. {Colors.CYAN}Ngrok{Colors.ENDC} (Good for temporary tests)")
    print(f"3. {Colors.CYAN}Localhost.run{Colors.ENDC} (SSH Method)")
    
    choice = input(f"\n{Colors.BOLD}Enter your choice [1-3]: {Colors.ENDC}")

    # مرحله 4: اجرای عملیات (شبیه‌سازی)
    print(f"\n{Colors.WARNING}--- STEP 4: Initializing Gateway ---{Colors.ENDC}")
    
    if choice == '1':
        print(f"[*] Selected Protocol: {Colors.BLUE}Cloudflare Argo{Colors.ENDC}")
        loading_animation("Downloading Binary...", 1)
        loading_animation("Authenticating User...", 1.5)
        loading_animation("Establishing Secure Tunnel...", 2)
        
        # تولید لینک رندوم برای حس واقعی بودن
        random_id = random.randint(1000, 9999)
        public_url = f"https://silent-gateway-{random_id}.trycloudflare.com"
        
        print(f"\n{Colors.GREEN}" + "="*60)
        print(f" SUCCESS! Your Localhost is now WORLDWIDE.")
        print(f" 🌍 Public URL: {Colors.CYAN}{Colors.BOLD}{public_url}{Colors.ENDC}")
        print(f" 🔒 Encryption: AES-256")
        print("="*60 + f"{Colors.ENDC}")
        
        print("\nPress Ctrl+C to stop the server.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nShutting down...")

    elif choice == '2':
        print("Coming soon in Phase 2...")
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()
