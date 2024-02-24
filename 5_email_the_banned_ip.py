import subprocess
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

import config

# Check the fail2ban-client status for sshd jail
def get_fail2ban_banned_ips():
    # Get the list of currently banned IPs
    result = subprocess.run(['fail2ban-client', 'status', 'sshd'], capture_output=True, text=True)
    if result.returncode == 0:
        output = result.stdout
        banned_ips_line = next((line for line in output.split('\n') if 'Banned IP list:' in line), None)
        if banned_ips_line:
            banned_ips = banned_ips_line.split(':')[-1].strip()
            print(f"Banned IP List: {banned_ips.split()}")
            return banned_ips.split()
    print("No Banned IPS.")
    return []

# Sednd an email to notify about the banned IP
def send_email(subject, message, to_email):
    # Email setup
    from_email = config.SMTP_EMAIL
    from_password = config.SMTP_APP_PASS
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create email message
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Send email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

def main():
    checked_ips = set()
    while True:
        banned_ips = get_fail2ban_banned_ips()
        new_bans = set(banned_ips) - checked_ips
        if new_bans:
            for ip in new_bans:
                send_email('Fail2Ban IP Banned', f'The following IP has been banned: {ip}', config.EMAIL)
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time
                print(f'Notification sent for IP: {ip}  time: {current_time}')
            checked_ips.update(new_bans)
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
