# Study Log Automation with Selenium

A Python automation project that uses **Selenium WebDriver** to automatically record daily study sessions through a Google Form.

This project was created as part of **Professional Portfolio Projects** from Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

---

## 📌 Project Overview

Keeping track of daily study sessions manually can become repetitive. This project automates that process by allowing the user to enter their study details in the terminal while Selenium handles the browser interaction.

The program:

1. Automatically gets the current date.
2. Takes study information from the user.
3. Opens a Google Form using Chrome.
4. Automatically fills in the form fields.
5. Submits the form.
6. Safely closes the browser.

---

## ✨ Features

- 📅 **Automatic Date** – Uses the current date automatically.
- ⌨️ **Terminal Input** – Accepts study details directly from the user.
- 🌐 **Browser Automation** – Opens and interacts with Google Forms using Selenium.
- 📝 **Automatic Form Filling** – Enters all study information automatically.
- 🚀 **Automatic Submission** – Submits the completed form without manual interaction.
- 🔒 **Safe Browser Cleanup** – Uses `try/finally` to ensure the browser closes properly.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Selenium | Browser automation |
| Google Forms | Study log data collection |
| Google Chrome | Automated browser |

---
## ⚙️ How It Works

1. The program starts Chrome using Selenium WebDriver.
2. Today's date is automatically generated using Python's `datetime` module.
3. The user enters:
   - Subject
   - Hours studied
   - Topic studied
   - Notes
4. Selenium opens the configured Google Form.
5. The program fills in each form field automatically.
6. Selenium clicks the **Submit** button.
7. The browser is safely closed after submission.

---
