# SSL Expiry Date Finder
This Python script allows you to easily find the expiry date of an SSL certificate for a given hostname. It uses the `ssl` and `socket` modules to establish an SSL connection with the specified hostname and retrieve the peer certificate. The expiry date is then extracted from the certificate and displayed.

## Prerequisites
- Python 3.x

## Usage
The script will establish an SSL connection with the specified hostname and retrieve the SSL certificate's expiry date. If successful, it will display the expiry date.

## Error Handling
The script includes basic error handling for certificate errors, SSL errors, and socket errors. If any of these errors occur, an appropriate error message will be displayed.