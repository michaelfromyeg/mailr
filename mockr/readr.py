import poplib
from email.parser import BytesParser

# Configuration
pop3_server = 'localhost'
port = 7110
username = 'michaelfromyeg'

def fetch_emails(server, port, username):
    try:
        # Connect to the POP3 server
        pop_conn = poplib.POP3(server, port)
        
        pop_conn.user(username)

        # List all emails in the mailbox
        num_messages = len(pop_conn.list()[1])
        print(f"Number of messages: {num_messages}")

        # Fetch and parse each email
        for i in range(num_messages):
            # Fetch the email
            response, lines, octets = pop_conn.retr(i + 1)
        
            msg_data = b'\n'.join(lines)
            
            # Parse the email
            msg = BytesParser().parsebytes(msg_data)
            
            # Print email subject and sender
            print(f"Subject: {msg['subject']}")
            print(f"From: {msg['from']}")
            print(msg)
            print('---')

        # Close the connection
        pop_conn.quit()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_emails(pop3_server, port, username)
