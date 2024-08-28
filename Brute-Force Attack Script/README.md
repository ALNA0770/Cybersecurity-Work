---

# 📄 AIG Job Simulation: Brute-Force Attack Script

![AIG Logo](https://img.shields.io/badge/AIG-Job%20Simulation-blue) ![Python](https://img.shields.io/badge/Python-3.x-yellow) ![License](https://img.shields.io/badge/license-MIT-green)

## 🚀 Project Overview

This repository contains a Python script developed as part of the AIG Job Simulation on Forage. The script is designed to perform a brute-force attack on a password-protected ZIP file, demonstrating fundamental skills in cybersecurity, scripting, and problem-solving.

## 🛠️ Script Functionality

- **Brute-Force Attack**: The script attempts to extract a password-protected ZIP file by iterating through a list of potential passwords from a dictionary file.
- **Password Verification**: If the correct password is found, the script successfully extracts the contents of the ZIP file.
- **Error Handling**: The script includes error handling for incorrect password attempts and invalid ZIP files.

## 🗂️ Project Structure

```plaintext
├── bruteforce.py         # The main Python script for the brute-force attack
├── enc.zip               # The encrypted ZIP file to be brute-forced
├── rockyou.txt           # The password list used for brute-forcing
└── README.md             # This README file
```

## 💻 Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/aig-job-simulation.git
    cd aig-job-simulation
    ```

2. **Run the Script**:
    ```bash
    python bruteforce.py
    ```

3. **Script Output**:
    The script will attempt to extract the `enc.zip` file using passwords from `rockyou.txt`. If the correct password is found, it will be displayed in the terminal.

## 📚 Learning Objectives

- Understanding and implementing brute-force attack techniques.
- Working with file handling and error management in Python.
- Enhancing cybersecurity awareness and practical skills.

## 📈 Improvements

This task provided valuable insights, but could benefit from:
- Adding more complex scenarios to test different aspects of cybersecurity.
- Implementing additional features like multi-threading for faster password attempts.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

![Forage](https://img.shields.io/badge/Forage-AIG-red) ![Cybersecurity](https://img.shields.io/badge/Cybersecurity-%F0%9F%94%92-orange) ![Python](https://img.shields.io/badge/Python-%F0%9F%94%A5-lightgrey)

---

Feel free to customize this README further to match your personal style or preferences!
