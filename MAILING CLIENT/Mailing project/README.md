# 📧 SMTP Email Sending Script

This project demonstrates how to send an email using Python's `smtplib` and `email` libraries. The script connects to a Gmail SMTP server to send an email with a text file as its body content. The email sender's password is read from a file for security purposes.

## 📜 Requirements

- Python 3.x
- `smtplib` and `email` modules (included in the Python Standard Library)

## 📂 Project Structure

```
.
├── pass.txt
├── text.txt
└── send_email.py
```

- `pass.txt`: A file containing your email password.
- `text.txt`: A file containing the email body text.
- `send_email.py`: The main script to send the email.

## 📝 Usage

1. **Clone the repository** or download the `send_email.py` file.
2. **Create and prepare** the `pass.txt` file:
   - Put your email password inside `pass.txt`.
3. **Create and prepare** the `text.txt` file:
   - Put the email body content inside `text.txt`.
4. **Update the script** with your email credentials:
   - Add your email address in the `server.login('your_email@gmail.com', password)` line.
   - Update the `msg['From']` and `msg['To']` fields with the sender and recipient email addresses.
5. **Enable "Less Secure App Access" in your Google account**:
   - Go to your Google Account settings.
   - Navigate to the "Security" tab.
   - Scroll down to the "Less secure app access" section.
   - Turn on "Allow less secure apps" (Note: This setting is necessary for the script to work with Gmail SMTP, but be aware it might reduce your account's security).
6. **Run the script**:
   ```bash
   python send_email.py
   ```

## 📚 Code Explanation

Here's a breakdown of the main components in the script:

### 1. Importing Required Libraries

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
```

### 2. Setting Up SMTP Server

```python
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.ehlo()
```

### 3. Reading the Email Password

```python
with open('pass.txt', 'r') as f:
    password = f.read().strip()
```

### 4. Logging into the SMTP Server

```python
server.login('your_email@gmail.com', password)
```

### 5. Creating the Email Message

```python
msg = MIMEMultipart()
msg['From'] = 'your_email@gmail.com'
msg['To'] = 'recipient_email@gmail.com'
msg['Subject'] = 'TEST'
```

### 6. Attaching the Email Body

```python
with open('text.txt', 'r') as f:
    text = f.read()
    msg.attach(MIMEText(text, 'plain'))
```

### 7. Sending the Email

```python
text = msg.as_string()
try:
    server.sendmail(msg['From'], msg['To'], text)
    print("Email sent successfully! ✉️")
except Exception as e:
    print(f"Failed to send email. Error: {str(e)} ❌")
finally:
    server.quit()
```

## 🚀 Running the Script

Run the script using the following command:

```bash
python send_email.py
```

If everything is set up correctly, you should see a message indicating that the email was sent successfully.

## ⚠️ Important Notes

- **Security**: Avoid hardcoding your email password in the script. Use environment variables or secure vaults for managing sensitive information.
- **Gmail SMTP Access**: Ensure that "Less secure app access" is enabled in your Google account settings if you are using Gmail. Alternatively, consider using an app password for enhanced security.
  - **Enable Less Secure App Access**:
    1. Go to your [Google Account](https://myaccount.google.com/).
    2. Navigate to the "Security" tab.
    3. Scroll down to the "Less secure app access" section.
    4. Turn on "Allow less secure apps".
- **App Passwords**: For better security, consider using [Google App Passwords](https://support.google.com/accounts/answer/185833?hl=en). This way, you don’t need to enable less secure app access and can generate a specific password for your script.

---

Feel free to customize and enhance the script according to your requirements. Happy emailing! 🚀📧

## 💬 Connect and Troubleshoot

If you encounter any issues or have questions, please feel free to reach out:

- **Google SMTP Documentation**: [Using Gmail SMTP server](https://support.google.com/a/answer/176600?hl=en)
- **Stack Overflow**: Post your questions with the tag `#python` and `#smtplib`.
- **Contact Me**: [nazarov31ali@gmail.com](mailto:nazarov31ali@gmail.com)

Good luck and happy coding! 💻✨
