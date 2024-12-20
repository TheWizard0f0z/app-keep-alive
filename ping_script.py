import os
import requests
import logging

def ping_endpoints():
    endpoints = os.getenv("PING_ENDPOINTS").split(",")  # Comma-separated list in environment variable
    
    for url in endpoints:
        try:
            response = requests.get(url, timeout=10)
            logging.info(f"Pinged {url}. Status code: {response.status_code}")
        except Exception as e:
            logging.error(f"Error pinging {url}: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    ping_endpoints()
