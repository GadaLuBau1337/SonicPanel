# 🚀 SONIC NETWORK – CLI Panel

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Linux-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-Educational-orange)

A powerful and lightweight **CLI Control Panel DDoS** built with Python.  
Designed for **network stress testing simulations and educational research purposes only**.

---

## ⚡ Features

- 🎨 Clean Colored CLI Interface
- 🔐 Login System
- 🧠 Command Parsing System
- 🖥 Layer4/Layer7/AMP Methods
- 📊 Attack Banner Output

---

## 📂 Project Structure

```
SONIC-NETWORK/
│
├── main.py
├── src/
│   └── layer4/
│       ├── TCP-DOWN
│       └── (other methods)
└── README.md
└── LICENSE
```

---

## 🖥 Example Command

Inside the panel:

```
TCP-DOWN <ip> <port> <threads> <pps> <time>
```

Example:

```
TCP-DOWN 1.1.1.1 80 100 1000 60
```

---

## 🧩 How It Works

1. User inputs command in CLI.
2. Script parses arguments using `cmd.split()`.
3. Module is executed via `subprocess.Popen`.
4. Custom banner is displayed.
5. Script waits using `time.sleep()` based on user input duration.

---

## 🔒 Login System

The panel includes a basic login mechanism to restrict access before command execution.

---

## 🎨 CLI Preview

```
┌──[Panel] - [sonic]
└─➤
```

---

## ⚙ Requirements

- Python 3.x

Install dependencies (if needed):

```
pip install -r requirements.txt
```

---

## ⚠ Disclaimer

This project is created strictly for:

- Educational purposes
- Network research
- Security testing in controlled environments

The developer is **not responsible** for misuse or illegal activities.  
Always obtain proper authorization before testing any system.

---

## 👤 Developer

**(GadaLuBau)**  
SONIC NETWORK

---

## ⭐ Support

If you like this project:

- ⭐ Star the repository
- 🍴 Fork it
- 🛠 Improve it
