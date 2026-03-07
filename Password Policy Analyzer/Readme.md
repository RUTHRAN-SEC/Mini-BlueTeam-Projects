# Password Policy Analyzer (NIST Password Compliance Based)

## Project Description

Password Policy Analyzer is a Blue Team security project that checks an organization's password policy against modern security standards such as NIST SP 800-63B.

This tool helps identify weak password rules and provides simple recommendations to improve security and reduce the risk of cyber attacks.

It is designed for:

* Security students
* SOC analysts
* Blue team learners
* Compliance auditors
* IT administrators

The goal of this project is to demonstrate security policy analysis, compliance checking, and risk communication in a simple and practical way.

---

## What This Project Demonstrates

* Password security knowledge
* Understanding of NIST guidelines
* Password Compliance based auditing
* Risk analysis and reporting
* Defensive security mindset

---

## Requirements for This Project

To understand and build this project, you should know:

* Basic Python programming
* What is a password policy
* Basic understanding of cybersecurity
* How to run Python files using terminal or command prompt

No advanced knowledge is required.

---

## Software Requirements

* Python 3.14.3 
* VS Code | PyCharm | Any Code Editor
* Command Prompt | Terminal

---

## Python Libraries Used

This project uses only built in Python libraries:

* `json` → To read password policy files (JSON format)

No external libraries are required for the basic version.

---

## Why This Project Is Important

Many companies still use weak password policies such as:

* Short passwords (less than 8 characters)
* Forced special characters
* Frequent password expiry
* No passphrase support

Weak password policies increase the risk of:

* Account compromise
* Brute force attacks
* Credential stuffing
* Data breaches

This tool helps organizations identify weaknesses and improve their security posture.

---

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/password-policy-analyzer.git
cd password-policy-analyzer
```

### Step 2: Run the Script

```bash
python password_analyzer.py
```

### Step 3: Output

```
Password Policy Compliance Report

Minimum length is less than 8
NIST does NOT recommend forcing special characters
Frequent password expiry is not recommended
Passphrases should be allowed
```
---

## Structure

Password-Policy-Analyzer/
- password_analyzer.py
- sample company policy.json 
- README.md           

---

## Example Policy Input (sample company policy.json)

```json
{
  "min_length": 6,
  "require_uppercase": true,
  "require_lowercase": true,
  "require_numbers": true,
  "require_special": true,
  "password_expiry_days": 30,
  "allow_passphrases": false
}
```

---

## Sample Output

```
Password Policy Compliance Report

Minimum length is less than 8
NIST does NOT recommend forcing special characters
Frequent password expiry is not recommended
Passphrases should be allowed

Risk Level: High
```
## ScreenShot
<img width="831" height="464" alt="image" src="https://github.com/user-attachments/assets/6d7830e4-a14d-40e3-8ae9-ca73a158e234" />

---

## Futures that can be added later for Improvements
You can improve this project by adding:

* Web version using Flask
* Dashboard with compliance percentage
* PDF report export
* Email report sending
* Active Directory policy integration
* CIS Benchmark comparison
* Logging and audit history
* Breached password list checking
* Risk scoring system with visual indicators
* GUI version using Tkinter or PyQt

---

## Business Value

This project helps organizations:

* Strengthen password security
* Reduce breach risks
* Improve compliance posture
* Support internal security audits
* Prepare for security certifications

---

## ⚠️ Disclaimer

This project is intended strictly for educational and ethical purposes.
All testing must be performed only on systems you own or have explicit authorization to test.
The author is not responsible for any misuse or illegal activity resulting from the use of this project.

## Author
### RUTHRAN-SEC

