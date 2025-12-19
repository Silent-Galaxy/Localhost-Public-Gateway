# 🚀 Silent-Gateway (Localhost Exposer)

![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/github/license/Silent-Galaxy/Silent-Gateway?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20Batch%20%7C%20Python-blue?style=for-the-badge)

> **Turn your Localhost into a Global Server with One Click.**
> *تبدیل کامپیوتر شخصی به سرور جهانی با تمرکز بر سادگی (Batch Script) و هوشمندی (Python)*

---

## 🎓 Academic Context
| Role | Details |
| :--- | :--- |
| **University** | **Shahid Chamran Technical College of Rasht (TVU)** |
| **Department** | Computer Software Engineering (B.Sc) |
| **Professor** | **Master Abbas Mohammadi Rik** |
| **Lead Developer** | **AmirAli SalehPour** |

---

## 💡 Project Overview (معرفی پروژه)
**Silent-Gateway** is designed with a dual-layer architecture:
1.  **The Interface (.bat):** A Windows Batch Script designed for **End-Users**. It requires zero configuration. Just click and host.
2.  **The Core (.py):** Python logic for network analysis, NAT detection, and port scanning.

**Why Batch (.bat)?**
We prioritized the `.bat` file to ensure accessibility for all students. No complex installation is needed to start the gateway.

---

## 🗺️ For Researchers (مسیر تحقیقاتی)
If you are joining this project for **Academic Research**, here are the open problems we aim to solve:

1.  **NAT Traversal Techniques:** Analyzing different methods (STUN, TURN, Hole Punching) to find the best low-latency solution for Iranian ISPs.
2.  **Security Analysis:** Investigating the risks of exposing localhost and implementing automated firewall rules within the script.
3.  **Traffic Obfuscation:** Researching ways to hide tunnel traffic to prevent ISP throttling.

*We encourage you to fork this repo and document your findings in the `docs/` folder.*

---

## 🛠️ For Developers (راهنمای توسعه‌دهندگان)
If you want to build tools based on this project, here is the structure:

- **`Silent-Gateway.bat`**: The main entry point. Modify this to change the UI/UX.
- **`core/network_analyzer.py`**: The logic that detects IP and Open Ports.
- **`modules/tunneling/`**: (Planned) Where we integrate Cloudflare/Ngrok binaries.

**Contribution Ideas:**
- Port the `.bat` script to **Bash** for Linux users.
- Create a simple **GUI** using Python (Tkinter/PyQt).
- Add support for more tunneling providers (Localtunnel, Serveo).

---

## 🚀 Quick Start (راهنمای استفاده)

### Option 1: The Easy Way (Windows)
1.  Download the project.
2.  Double click on `Silent-Gateway.bat`.
3.  Follow the on-screen instructions.

### Option 2: The Developer Way
1.  Ensure Python is installed.
2.  Run `python main.py` to see the verbose network analysis.



مراحل تست واقعی پروژه عملی Silent-Gateway.bat
https://github.com/Silent-Galaxy/Localhost-Public-Gateway/blob/main/Silent-Gateway.bat

<img width="619" height="429" alt="image" src="https://github.com/user-attachments/assets/d0769bdf-6dc1-462f-a21e-35b9b66d59cc" />

<img width="818" height="626" alt="image" src="https://github.com/user-attachments/assets/01e9aac7-3f08-4eea-97b6-a2c568895342" />

<img width="979" height="512" alt="image" src="https://github.com/user-attachments/assets/0c4c3109-539b-49cc-839f-229b274bb161" />

<img width="619" height="380" alt="image" src="https://github.com/user-attachments/assets/9f64b15b-e35d-4215-91ae-1f0049540b15" />



---

## 🤝 Call for Contribution
We are looking for collaborators!
- **Research:** Help us document NAT behaviors.
- **Code:** Improve the `.bat` interface or Python logic.

**Join us to build the ultimate tool for students!**

---
### 👤 Author
**AmirAli SalehPour**
- Chamran College of Rasht
- GitHub: [@Silent-Galaxy](https://github.com/Silent-Galaxy)












***






<div align="center">

# 🌐 Localhost Public Gateway (Silent-Gateway)

**Turn your Localhost into a Public Server instantly | Bypass CGNAT & Firewalls**
<br>
**تبدیل لوکال‌هاست به سرور عمومی | عبور از محدودیت‌های شبکه و CGNAT**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Development-orange.svg)]()

[English](#english-documentation) | [فارسی](#persian-documentation)

</div>

---

<a name="english-documentation"></a>
## 🇬🇧 English Documentation

### 🚀 Introduction
**Localhost Public Gateway** (also known as *Silent-Gateway*) is an open-source research project designed to make local servers accessible from the public internet without the need for a Static IP or complex router configurations (Port Forwarding).

This tool is particularly useful for students, researchers, and developers living in regions with strict network restrictions (CGNAT) or those who need a quick way to showcase their work globally.

> **Note:** This is an academic project developed at *Technical and Vocational College of Shahid Chamran (Rasht)*.

### ✨ Key Features
*   **Zero Configuration:** No need to touch router settings.
*   **Bypass CGNAT:** Works even if your ISP puts you behind a Carrier-Grade NAT.
*   **Auto Detection:** Automatically analyzes network conditions and NAT types using Python.
*   **User Friendly:** Simple "One-Click" execution via Windows Batch script.

### 🛠️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Silent-Galaxy/Localhost-Public-Gateway.git
    cd Localhost-Public-Gateway
    ```

2.  **Install Dependencies:**
    Make sure you have Python installed.
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If `requirements.txt` is missing, check the imports in `main.py`)*

3.  **Run the Gateway:**
    Simply double-click on `Silent-Gateway.bat` or run via terminal:
    ```bash
    python main.py
    ```

### 🤝 How to Contribute
We welcome contributions from around the world! This project is in its early stages. We specifically need help with:
*   **Tunneling Modules:** Integrating SSH tunneling, Cloudflare Tunnel, or similar technologies.
*   **Security:** Improving the security layers to protect the host machine.
*   **Cross-Platform Support:** Adding support for Linux and macOS.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---

<a name="persian-documentation"></a>
## 🇮🇷 مستندات فارسی

### 🚀 معرفی پروژه
**Localhost Public Gateway** (یا همان *Silent-Gateway*) یک ابزار متن‌باز تحقیقاتی است که به شما اجازه می‌دهد کامپیوتر شخصی (Localhost) خود را بدون نیاز به آی‌پی ثابت (Static IP) یا تنظیمات پیچیده مودم، به اینترنت جهانی متصل کنید.

این پروژه با هدف کمک به دانشجویان و توسعه‌دهندگان برای عبور از محدودیت‌های شبکه (مانند CGNAT) و نمایش سریع پروژه‌ها طراحی شده است.

> **نکته:** این یک پروژه دانشجویی است که در *دانشکده فنی شهید چمران رشت* توسعه داده شده است.

### ✨ ویژگی‌های کلیدی
*   **بدون نیاز به تنظیمات پیچیده:** نیازی به پورت فورواردینگ در مودم نیست.
*   **عبور از محدودیت‌ها:** امکان عبور از CGNAT و فایروال‌های ISP.
*   **تشخیص هوشمند:** تحلیل خودکار وضعیت شبکه و نوع NAT با استفاده از پایتون.
*   **استفاده آسان:** اجرا تنها با یک کلیک روی فایل `Silent-Gateway.bat`.

### 🛠️ نصب و راه‌اندازی

1.  **دریافت مخزن:**
    ```bash
    git clone https://github.com/Silent-Galaxy/Localhost-Public-Gateway.git
    cd Localhost-Public-Gateway
    ```

2.  **نصب پیش‌نیازها:**
    مطمئن شوید که پایتون روی سیستم شما نصب است.
    ```bash
    pip install -r requirements.txt
    ```

3.  **اجرای برنامه:**
    فایل `Silent-Gateway.bat` را اجرا کنید یا در ترمینال بنویسید:
    ```bash
    python main.py
    ```

### 🤝 مشارکت در توسعه
ما از همکاری برنامه‌نویسان سراسر دنیا استقبال می‌کنیم! این پروژه در مراحل اولیه است و برای تکمیل شدن به یاری شما نیاز دارد، مخصوصاً در بخش‌های:
*   **ماژول‌های تانلینگ:** پیاده‌سازی روش‌های تانل‌زنی امن.
*   **امنیت:** ایمن‌سازی ارتباطات برای محافظت از سیستم میزبان.
*   **پشتیبانی از لینوکس و مک:** نوشتن اسکریپت‌های اجرایی برای سایر سیستم‌عامل‌ها.

---

<div align="center">
Developed with ❤️ by AmirAli Salehpour
</div>
