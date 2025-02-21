# 🎬YT-control-multimedia-keys-shortcuts
This Python script allows you to control YouTube video playback using your keyboard’s media keys, even when the browser window is not in focus.

# 🚀 Features
✅ Use media keys to skip forward or backward in YouTube videos.<br>
✅ Works with any YouTube window, regardless of the video title.<br>
✅ Runs in the background and displays ASCII art when launched (I love Furina, but you can edit this by modifying the furina_ascii.txt file).<br>
✅ Lightweight and easy to use.<br>

# 🛠 Requirements
🔹 Python 3.8 or later.<br>
🔹 Libraries: pygetwindow, pyautogui, pynput.<br>

# 📌 Installation & Usage
1-Install dependencies by running:<br>
```
pip install pygetwindow pyautogui pynput
```
2-Run the script:<br>

```
python youtube_shortcuts.py
```
3-Use your media keys to control YouTube playback without switching windows.<br>
# 🎮 Controls<br>
Next Track Button (⏭️) → Skip forward 5 seconds.<br>
Previous Track Button (⏮️) → Skip backward 5 seconds.<br>
# 📝Notes<br>
PyInstaller was used to create the .exe file, this generates some incompatibility with some antivirus, so you can add the .exe to the exceptions or use the script if you have python installed and follow the previous steps.
# ⚠Warning<br>
Some of the antivirus that detect a false positive in the .exe include but are not limited to:  
| Antivirus | Code |
|-----------|-----------|
| Avast    | Win64:Malware-gen    |
| AVG    | Win64:Malware-gen    |
| DeepInstinct    | MALICIOUS    |
| Gridinsoft (no cloud)    | Spy.Win64.Keylogger.oa!s1    |
| SecureAge    | Malicious    |
| SentinelOne (Static ML)    | Static AI - Suspicious PE    |
| Skyhigh (SWG)    | BehavesLike.Win64.Generic.rc    |
| Zillya    | Trojan.Agent.Win32.4167152    |

analysis by VirusTotal.  
# 🛣Road Map
-Fix antivirus compatibility.  
-x86 version (maybe, if anyone needs it).  
-and that's all for now.  
# 👋🏻Bye
Love you ♥
