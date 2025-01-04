#importing as json
import json
file_path="../data/main.json"
with open(file_path, "r") as file:
    main = json.load(file)


def create_head():

    #creating id
    last_id=list(main.keys())[-1]
    print(last_id)
    new_id=str(int(last_id)+1).zfill(6)
    print(new_id)

    #create new json file
    import os
    folder_path = "../data"
    file_name = f"{new_id}.json"
    file_path = os.path.join(folder_path, file_name)
    # Create the directory if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    #accept values from user
    name=input("enter name of organisation")
    password=input("create a password")

    # Create JSON structure
    org_data = {
        new_id: {
            "name": name,
            "password": password,
            "suborgs": {}
        }
    }

    # Write the data to the new JSON file
    with open(file_path, "w") as new_file:
        json.dump(org_data, new_file, indent=4)

    # Update main.json with the new ID
    main[new_id] = name
    with open("../data/main.json", "w") as main_file:
        json.dump(main, main_file, indent=4)

    print(f"Organisation '{name}' created successfully with ID {new_id}!")


#--------------------------------------
create_head()