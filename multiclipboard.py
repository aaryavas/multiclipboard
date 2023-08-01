import sys
import clipboard
import json

#copys data that was already in the clipboard
clipboard.copy('hot dogs')
#pastes the data from the clipboard this variable 
data = clipboard.paste()
ß

SAVED_DATA = 'clipboard.json'

#function that creates json file
def save(filepath, data):
    with open(filepath, 'w') as file: #override file if already exists or create a new one 
        json.dump(data, file)
#running code for function above        
save("test.json", {"key": "value"})

#function that reads jsoon file
def load(filepath):
    try: #try for not sure if the code with execute or not
        with open(filepath, 'r') as file:
            data = json.load(file) #gives python representation of created json file
            return data
    except:#if try fails
        return {}#empty dict
        

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load(SAVED_DATA)
    
    #saves item 
    if command == 'save':
        key =  input("Enter key:")
        data[key] = clipboard.paste()
        save(SAVED_DATA, data)
        print('save was successful')
    
    elif command == 'load':
        key = input("Enter key:")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard")
        else:
            print("key does not exist")
        
    elif command == 'list':
        print(data)
        
    else:
        print('Unknown command')
        
else:
    print("Error: please pass just one command")
    
