import ssl
import socket
from datetime import datetime

def get_ssl_expiry_date(hostname, port=443):
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                expiry_date = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                return expiry_date
    except ssl.CertificateError as e:
        print(f"Certificate error: {e}")
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
    except socket.error as e:
        print(f"Socket error: {e}")
    return None

# Example usage:
hostname = input("Enter the Hostname/Website Name: ")
expiry_date = get_ssl_expiry_date(hostname)
if expiry_date:
    print(f"The SSL certificate for {hostname} expires on {expiry_date}.")
