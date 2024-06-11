import requests
import time

class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

class MissingPerson(Person):
    def __init__(self, id, first_name, last_name, last_seen="Unknown"):
        super().__init__(id, first_name, last_name)
        self.last_seen = last_seen

class GangMember(Person):
    def __init__(self, id, first_name, last_name, gang_name="Unknown"):
        super().__init__(id, first_name, last_name)
        self.gang_name = gang_name

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

def process_fbi_data(items):
    missing_persons = []
    gang_members = []
    
    for item in items:
        categories = item.get('subjects', [])
        id = item.get('uid', 'Unknown')
        names = item.get('title', 'Unknown').split()
        first_name = names[0] if names else 'Unknown'
        last_name = names[1] if len(names) > 1 else 'Unknown'
        
        if "missing person" in categories:
            missing_persons.append(MissingPerson(id, first_name, last_name))
        elif "Criminal Enterprise Investigations" in categories:
            gang_members.append(GangMember(id, first_name, last_name))
    
    return missing_persons, gang_members

def main():
    items = fetch_fbi_data()
    if items:
        missing_persons, gang_members = process_fbi_data(items)
        
        print("Missing Persons:")
        for person in missing_persons:
            print(f"ID: {person.id}, Name: {person.first_name} {person.last_name}, Last Seen: {person.last_seen}")

        print("\nGang Members:")
        for member in gang_members:
            print(f"ID: {member.id}, Name: {member.first_name} {member.last_name}, Gang Name: {member.gang_name}")

if __name__ == "__main__":
    main()
