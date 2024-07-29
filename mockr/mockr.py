import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
import getpass
import os


def send_email(
    smtp_server: str,
    smtp_port: int,
    username: str,
    password: str,
    from_addr: str,
    to_addr: str,
    subject: str,
    html_file_path: str,
) -> None:
    """
    Send an email with the given HTML content to the specified recipient.
    """
    if not os.path.isfile(html_file_path):
        print(f"Error: The file {html_file_path} does not exist.")
        return

    with open(html_file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    print("HTML content read successfully!", html_content[:100])

    # msg = MIMEText(html_content, "html", "utf-8")
    # msg["From"] = formataddr((str(Header("Sender", "utf-8")), from_addr))
    # msg["To"] = to_addr
    # msg["Subject"] = Header(subject, "utf-8")

    # try:
    #     server = smtplib.SMTP(smtp_server, smtp_port)
    #     server.sendmail(from_addr, to_addr, msg.as_string())
    #     server.quit()
    #     print("Email sent successfully!")
    # except Exception as e:
    #     print(f"Error: {e}")

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.sendmail(from_addr, to_addr, html_content)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("Welcome to the Interactive Email Sender!")

    smtp_server = "localhost"
    smtp_port = 7725

    username = "user" # input("Enter the SMTP server username: ")
    password = "pass" # getpass.getpass("Enter the SMTP server password: ")

    from_addr = "michaelfromyeg@gmail.com" # input("Enter the sender's email address: ")
    to_addr = "michaelfromyeg@gmail.com" # input("Enter the recipient's email address: ")
    subject = "SUBJECT" # input("Enter the subject of the email: ")
    html_file_path = input("Enter the path to the HTML file to be sent: ")

    send_email(
        smtp_server,
        smtp_port,
        username,
        password,
        from_addr,
        to_addr,
        subject,
        html_file_path,
    )
