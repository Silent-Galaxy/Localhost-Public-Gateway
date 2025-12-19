@echo off
title Silent-Gateway v1.0 (By SilentGalaxy)
color 0b
cls

:: --- LOGO AREA ---
echo.
echo  =============================================================
echo   .d88888b.  G A T E W A Y
echo  d88P" "Y88b
echo  888     888
echo  888     888  8888b.  888  888  888  888  888  8888b.  888  888
echo  888     888     "88b 888  888  888  888  888     "88b 888  888
echo  888     888 .d888888 888  888  888  888  888 .d888888 888  888
echo  Y88b. .d88P 888  888 Y88b 888  Y88b 888 d88P 888  888 Y88b 888
echo   "Y88888P"  "Y888888  "Y88888   "Y8888888P"  "Y888888  "Y88888
echo                                                           888
echo      [ Developed by AmirAli SalehPour @ Chamran Uni ]    d88P
echo  =============================================================
echo.

:: --- STEP 1: CHECK INTERNET ---
echo  [STEP 1] Checking Internet Connection...
ping -n 1 google.com >nul
if errorlevel 1 (
    color 0c
    echo  [X] FAILED: No Internet Connection!
    echo.
    pause
    exit
) else (
    echo  [V] OK: Internet is Connected.
)
timeout /t 1 >nul
echo.

:: --- STEP 2: CHECK XAMPP/PORT 80 ---
echo  [STEP 2] Searching for Local Services (XAMPP/Apache)...
netstat -an | find ":80 " | find "LISTENING" >nul
if errorlevel 1 (
    color 0e
    echo  [!] WARNING: Port 80 is NOT active.
    echo      (Make sure XAMPP Apache is started)
    echo.
    echo      Press ANY KEY to continue anyway (Demo Mode)...
    pause >nul
    color 0b
) else (
    color 0a
    echo  [V] SUCCESS: Localhost Web Server is RUNNING!
    color 0b
)
echo.

:: --- STEP 3: MENU ---
echo  =========================================
echo   Select Tunneling Method:
echo  =========================================
echo   [1] Cloudflare Secure Tunnel (Recommended)
echo   [2] Ngrok (Temporary Link)
echo   [3] Exit
echo.
set /p method=" > Enter Option [1-3]: "

if "%method%"=="3" exit
if "%method%"=="2" goto ngrok_sim
if "%method%"=="1" goto cloudflare_sim

echo Invalid Option.
pause
goto :eof

:: --- SIMULATION: CLOUDFLARE ---
:cloudflare_sim
cls
color 09
echo.
echo  [*] Initializing Cloudflare Zero Trust Agent...
timeout /t 2 >nul
echo  [*] Authenticating User: SilentGalaxy...
timeout /t 1 >nul
echo  [*] Fetching configuration from Network...
timeout /t 2 >nul
echo  [*] Establishing Encryption Tunnel (AES-256)...
timeout /t 2 >nul
echo.
goto success

:: --- SIMULATION: NGROK ---
:ngrok_sim
cls
color 05
echo.
echo  [*] Starting Ngrok Agent...
timeout /t 2 >nul
echo  [*] Handshaking with US-West Server...
timeout /t 2 >nul
goto success

:: --- SUCCESS SCREEN ---
:success
color 0a
cls
echo.
echo  =======================================================
echo   CONNECTION ESTABLISHED SUCCESSFULLY!
echo  =======================================================
echo.
echo   Local Service:   http://localhost:80
echo   Status:          ONLINE (Forwarding)
echo   Protocol:        HTTPS (Secure)
echo.
echo   -----------------------------------------------------
echo   GLOBAL URL:      https://silent-gateway-%random%.trycloudflare.com
echo   -----------------------------------------------------
echo.
echo   [Use this link to access your PC from anywhere]
echo.
echo   Press Ctrl+C to stop the server.
pause
