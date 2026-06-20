# AI-CODING-HELPER
AI Coding Helper is a web-based tool that helps beginners write and fix code in languages like Python, C, C++, Java, HTML, CSS, JavaScript, and Bash. It detects basic errors, suggests corrections, and provides an easy-to-use interface using HTML, CSS, JavaScript, Flask, and Python.
# 🤖 AI Coding Helper

## About the Project

AI Coding Helper is a simple web application developed to help beginners write and correct basic programming code. The main goal of this project is to make coding easier by detecting common syntax mistakes and suggesting corrected code. It supports several popular programming languages such as Python, C, C++, Java, HTML, CSS, JavaScript, and Bash Script.

The project is built using HTML, CSS, and JavaScript for the frontend, while Python and Flask are used for the backend. When a user enters code and clicks the **Fix** button, the application sends the code to the backend, where it is analyzed and corrected before displaying the result.

---

## Features

* Supports multiple programming languages.
* Detects common syntax mistakes.
* Suggests corrected code.
* Simple and user-friendly interface.
* Fast response using Flask backend.
* Easy to understand for beginners.

---

## Technologies Used

**Frontend**

* HTML
* CSS
* JavaScript

**Backend**

* Python
* Flask

**Logic**

* Python (`fixer.py`)

---

## Project Workflow

1. The user opens the application in a web browser.
2. A programming language is selected.
3. The user writes or pastes the source code.
4. After clicking the **Fix** button, JavaScript sends the code to the Flask server.
5. The backend receives the request and forwards it to the code correction module.
6. The correction module checks the code for common errors and generates a corrected version.
7. The corrected code is sent back to the frontend.
8. Finally, the output is displayed on the screen.

---

## Project Activities

* Accepts code from the user.
* Sends the code to the backend.
* Analyzes the submitted code.
* Identifies basic programming errors.
* Generates corrected code.
* Displays the corrected output instantly.

---

## Project Structure

```text
AI-Coding-Helper/
│
├── index.html
├── style.css
├── script.js
├── app.py
├── fixer.py
├── requirements.txt
└── README.md
```

---

## How to Run the Project

1. Install the required Python packages.

```bash
pip install -r requirements.txt
```

2. Start the Flask server.

```bash
python app.py
```

3. Open the `index.html` file in your browser.

4. Write your code and click the **Fix** button to get the corrected output.

---

## Future Scope

This project can be improved by adding advanced AI-based code generation, detailed error explanations, code execution support, user login, cloud integration, and support for more programming languages.

---

## Conclusion

AI Coding Helper is a beginner-friendly project that demonstrates how frontend and backend technologies can work together to create a useful coding assistant. It helps users identify and correct common programming mistakes quickly, making the learning process easier and more interactive.

---

### Author

**Sayan Chatterjee**
