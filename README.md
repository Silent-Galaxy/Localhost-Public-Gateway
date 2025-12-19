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
