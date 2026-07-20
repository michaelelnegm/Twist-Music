<div align="center">

# 🎵 Twist Music Loyalty Auto-Claimer 🎵

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Type-Automation%20%2F%20API-purple?style=for-the-badge&logo=probot&logoColor=white" />
<img src="https://img.shields.io/badge/UI-Colorized%20CLI-cyan?style=for-the-badge&logo=gnubash&logoColor=white" />

---

### 🥷 "Automate the boring stuff and secure your rewards in seconds."

An interactive, multi-endpoint Python script designed to automate the authentication (OTP send/verify) and the daily action loop for the **Twist Music** loyalty rewards program.

---
</div>

## ✨ Features
*   **Complete Auth Flow:** Automated OTP transmission and token verification (`accessToken`, `tgToken`, `tgRefreshToken`).
*   **Balance Checker:** Automatically fetches and displays your current coin balance before executing tasks.
*   **Loop Automation:** Iterates through 22 pre-configured reward points endpoints (`SIGNUP`, `DAILY_CHECKIN`, `STREAM_SONG`, etc.).
*   **Interactive UI:** Fully stylized and color-coded CLI outputs using `colorama`.
*   **Delay Guard:** Built-in sleep interval between requests to remain stable and avoid sudden rate limits.

---

## 🛠️ Requirements & Installation

1. Clone the repository to your environment:
   ```bash
   git clone [https://github.com/michaelelnegm/Twist-Music-Auto-Claimer.git](https://github.com/michaelelnegm/Twist-Music-Auto-Claimer.git)
   cd Twist-Music-Auto-Claimer
