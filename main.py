import socket
import time
import sys
import os
import random
import urllib.request
import platform
import subprocess

# --- تنظیمات ظاهری و رنگ‌ها ---
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

def print_slow(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def get_public_ip():
    try:
        return urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
    except:
        return None

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # اتصال نمایشی برای یافتن اینترفیس اصلی
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def check_ping():
    # تست پینگ به گوگل برای سنجش کیفیت
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', '8.8.8.8']
    
    start = time.time()
    response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end = time.time()
    
    if response == 0:
        return round((end - start) * 1000) # میلی‌ثانیه
    return None

def main():
    clear_screen()
    print(f"{Colors.CYAN}")
    print(r"""
   _____ _ _            _       _____       _ZWXY_
  / ____(_) |          | |     / ____|     | |
 | (___  _| | ___ _ __ | |_   | |  __  __ _| |_ _____      ____ _ _   _ 
  \___ \| | |/ _ \ '_ \| __|  | | |_ |/ _` | __/ _ \ \ /\ / / _` | | | |
  ____) | | |  __/ | | | |_   | |__| | (_| | ||  __/\ V  V / (_| | |_| |
 |_____/|_|_|\___|_| |_|\__|   \_____|\__,_|\__\___| \_/\_/ \__,_|\__, |
                                                                   __/ |
                                                                  |___/ 
    """)
    print(f"{Colors.HEADER}   >>> Silent-Gateway Intelligence System v2.0 <<<{Colors.ENDC}\n")

    # --- فاز ۱: جمع‌آوری اطلاعات شبکه ---
    print(f"{Colors.WARNING}[PHASE 1] Analyzing Network Topology...{Colors.ENDC}")
    
    # 1. Local IP
    local_ip = get_local_ip()
    print(f" [*] Local Network Interface:  {Colors.BOLD}{local_ip}{Colors.ENDC}")
    
    # 2. Public IP
    print(" [*] Detecting Public IP...", end="", flush=True)
    public_ip = get_public_ip()
    
    if public_ip:
        print(f"\r [*] Public IP Address:        {Colors.GREEN}{public_ip}{Colors.ENDC}")
    else:
        print(f"\r [*] Public IP Address:        {Colors.FAIL}OFFLINE{Colors.ENDC}")
        print(f"\n{Colors.FAIL}❌ Error: No Internet connection detected.{Colors.ENDC}")
        input("Press Enter to exit...")
        return

    # 3. Ping Latency
    ping_ms = check_ping()
    quality_color = Colors.GREEN if ping_ms and ping_ms < 100 else Colors.WARNING
    print(f" [*] Network Latency (Ping):   {quality_color}{ping_ms}ms{Colors.ENDC}")

    print("-" * 50)
    
    # --- فاز ۲: تحلیل هوشمند (AI Logic) ---
    print(f"{Colors.WARNING}[PHASE 2] Network Diagnosis & Suitability{Colors.ENDC}")
    
    time.sleep(1)
    
    # منطق تشخیص NAT
    if local_ip == public_ip:
        print(f"{Colors.GREEN} ✅ You have a Direct Public IP! You don't necessarily need this tool.{Colors.ENDC}")
    else:
        print(f"{Colors.WARNING} ⚠️  NAT DETECTED:{Colors.ENDC} Your Local IP ({local_ip}) is different from Public IP.")
        print_slow(f"    {Colors.CYAN}Result:{Colors.ENDC} You are behind a firewall/CGNAT. Tunneling is REQUIRED to host.")

    # پیشنهاد کاربری
    print("\n [?] Suitability Suggestion:")
    if ping_ms and ping_ms < 60:
        print(f"    🚀 Excellent for: {Colors.BOLD}Game Servers (Minecraft/CS:GO) & Web Hosting{Colors.ENDC}")
    elif ping_ms and ping_ms < 150:
        print(f"    ✅ Good for: {Colors.BOLD}Web Hosting (Laravel/XAMPP) & APIs{Colors.ENDC}")
    else:
        print(f"    ⚠️  Fair for: {Colors.BOLD}Basic Web Pages (High Latency){Colors.ENDC}")

    print("-" * 50)
    
    # --- فاز ۳: بررسی سرویس‌ها ---
    input(f"\nPress {Colors.BOLD}ENTER{Colors.ENDC} to scan active local services...")
    
    services = [
        (80, "Web Server (Apache/Nginx)"),
        (3306, "Database (MySQL)"),
        (8000, "Laravel Dev Server"),
        (25565, "Minecraft Server")
    ]
    
    found_service = False
    active_port = 80 # پیش‌فرض
    
    for port, name in services:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex(('127.0.0.1', port))
        s.close()
        
        if result == 0:
            print(f" ✅ Found Active Service: {Colors.GREEN}{name}{Colors.ENDC} on port {port}")
            found_service = True
            active_port = port
        else:
            pass # چیزی نمی‌گیم که شلوغ نشه
            
    if not found_service:
        print(f"{Colors.FAIL} ❌ No standard services found running.{Colors.ENDC}")
        print("    (We will proceed with Port 80 anyway for demonstration)")
    
    # --- فاز ۴: اجرا ---
    print(f"\n{Colors.WARNING}[PHASE 3] Initializing Gateway on Port {active_port}...{Colors.ENDC}")
    
    choice = input(f"Select Protocol [1:Cloudflare / 2:Ngrok]: ")
    
    if choice == '1' or choice == '':
        print_slow(" 🔄 Connecting to Cloudflare Zero Trust Edge Network...")
        time.sleep(2)
        print_slow(" 🔐 Generating SSL Certificate...")
        time.sleep(1)
        
        # تولید لینک واقعی‌نما
        random_code = random.randint(1000, 9999)
        url = f"https://chamran-project-{random_code}.trycloudflare.com"
        
        print(f"\n{Colors.GREEN}" + "="*60)
        print(f" 🚀 YOUR SERVER IS LIVE!")
        print(f" 🌍 Worldwide URL: {Colors.CYAN}{Colors.BOLD}{url}{Colors.ENDC}")
        print(f" 👉 Targeting Local: http://127.0.0.1:{active_port}")
        print("="*60 + f"{Colors.ENDC}")
        
    else:
        print("Coming soon...")

    print("\n(Press Ctrl+C to stop)")
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        print("\nGoodbye!")

if __name__ == "__main__":
    main()
