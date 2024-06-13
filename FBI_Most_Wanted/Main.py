from fetch_data.fetch import fetch_fbi_data
from process_data.process_fbi_data import process_fbi_data

def main():
    try:
        items = fetch_fbi_data()
        if items:
            missing_persons, gang_members = process_fbi_data(items)

            print("Missing Persons:")
            for person in missing_persons:
                print(f"ID: {person.id}, Name: {person.first_name} {person.last_name}, Last Seen: {person.last_seen}")

            print("\nGang Members:")
            for member in gang_members:
                print(f"ID: {member.id}, Name: {member.first_name} {member.last_name}, Gang Name: {member.gang_name}")
        else:
            print("No items fetched from FBI API.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
