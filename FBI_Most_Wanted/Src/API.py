from models.PersonClass import Person, MissingPerson, GangMember
import fetch_data
import process_data


def main():
    items = fetch_data.fetch_fbi_data()
    if items:
        missing_persons, gang_members = process_data.process_fbi_data(items)
        
        print("Missing Persons:")
        for person in missing_persons:
            print(f"ID: {person.id}, Name: {person.first_name} {person.last_name}, Last Seen: {person.last_seen}")

        print("\nGang Members:")
        for member in gang_members:
            print(f"ID: {member.id}, Name: {member.first_name} {member.last_name}, Gang Name: {member.gang_name}")

if __name__ == "__main__":
    main()
