import time

def initialise(channel_id, slack):
    messages = []
    lastmessage = str(time.time())
    hasmore = True
    while hasmore == True:
        response = slack.channels.history(channel_id, latest= lastmessage)

        new = response.body.get('messages')

        lastmessage = new[-1].get('ts')

        messages.append(new) #array met laatste berichten

        hasmore = response.body.get('has_more')
    print(messages)
