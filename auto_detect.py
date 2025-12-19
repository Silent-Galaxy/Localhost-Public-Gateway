import socket
import os

def check_xampp_running():
    # سوکت می‌سازیم تا پورت 80 (پورت وب‌سرور) رو چک کنه
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 80))
    
    if result == 0:
        print("✅ Success: XAMPP/Apache is running on Port 80!")
        print("🚀 Starting the Tunneling process...")
        # اینجا بعداً دستور وصل شدن به کلودفلر رو می‌نویسیم
        # os.system("cloudflared tunnel --url localhost:80") 
    else:
        print("❌ Error: Web Server is NOT running.")
        print("💡 Please start Apache in XAMPP control panel.")
    sock.close()

if __name__ == "__main__":
    print("--- Silent-Gateway Auto Detector ---")
    check_xampp_running()
    input("\nPress Enter to exit...")
