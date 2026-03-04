
import json

def load_config():
    with open("config.json") as f:
        return json.load(f)
    
def getChat():
    try:
        with open("history.json", "r") as file:
            convo = json.load(file)
            if convo : 
                return convo
    except:
        pass 

    config = load_config()
    return [{
        "role": "system",
        "content": config["system_prompt"]
    }]

def addChat(conversation):
    with open("history.json" , "w") as file : 
        json.dump(conversation , file)


