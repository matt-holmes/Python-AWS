import json

print('Loading function')

def lamba_handler(event, context):
    print('Receive event: ' +
        json.dumps(event, indent=2))
    if 'name' in event:
        name = event['name']
    else:
        name = 'World'
    greetings = 'Hello ' + name + '!'
    print(greetings)
    return greetings
