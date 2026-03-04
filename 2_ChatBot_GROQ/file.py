
import json

def getChat():
    try:
        with open("memory.json", "r") as file:
            convo = json.load(file)
            if convo :
                return convo
    except:
        pass

    config = load_config()
    return [{"role": "system", "content": config["system_prompt"]}]

def load_config():
    with open("config.json") as f:
        return json.load(f)
    
def addChat(conversation):
    with open("memory.json" , "w") as file : 
        json.dump(conversation , file)


