import requests
import time

def fetch_fbi_data():
    url = "https://api.fbi.gov/wanted/v1/list"
    max_retries = 5
    retries = 0
    
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data['items']
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 429:
                retries += 1
                wait_time = int(response.headers.get("Retry-After", 60))  # Default wait time is 60 seconds
                print(f"HTTP 429 error occurred: {http_err}. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"HTTP error occurred: {http_err}")
                break
        except Exception as err:
            print(f"Other error occurred: {err}")
            break
    
    return []