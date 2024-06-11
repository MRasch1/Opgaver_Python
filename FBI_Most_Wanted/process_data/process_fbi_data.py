import Fetch_data.fetch

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
            missing_persons.append(Fetch_data.MissingPerson(id, first_name, last_name))
        elif "Criminal Enterprise Investigations" in categories:
            gang_members.append(Fetch_data.GangMember(id, first_name, last_name))
    
    return missing_persons, gang_members