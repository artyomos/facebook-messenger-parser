'''
There is no explanation for what I will do in this file...

If you really want to figure it out, do the hard work I did
'''


from bs4 import BeautifulSoup as soup
import re
from collections import Counter

def main(messenger_chat):
    print('Nate\'s HTML Parser - Version 0.0.1')
    print('\nPlease wait while the document loads... For large files this could take upwards of several minutes...')

    with open('message.html') as html:
        file = soup(html, 'html.parser')

    print('File has finished loading. Parsing data...\n')

    print('Parsing the file...')

    #Get the current title
    currentTitle = file.title.string

    #Print Chat Name
    print('Performing analysis on {0}...'.format(currentTitle))

    #navigate to where messenger arranges the messages
    parser = file.body.div.div.div.contents[1].contents[1]

    #Organizes the participants in their respective dictionary keys
    parse_participants(parser.div.div.string)

    #Get the messages
    messages = parser.contents[1:]

    #Sets the chat's total messages
    messenger_chat['total_messages'] = len(messages)

    #Iterate through all messages
    for message in messages:
        content = message.contents
        #TODO add everything else (Images/stickers/emoji checking)
        payload = {
            'user':content[0].string,
            'message':content[1].div.contents[1].string,
            'date':content[2].string,
        }
        if not parse_words(payload):
            # If the message is not Null, fix the mesage with no linebreak statements
            if (len(content[1].div.contents[1]) != 0):
                message = ''
                for item in content[1].div.contents[1].contents:
                    if isinstance(item, str):
                        message += item
                payload['message'] = message
                if not parse_words(payload):
                    print("A Secondary Parse Failed... :(")

    #TODO: Ignore common english words
    print(messenger_chat['words_counter'].most_common(50))

#Dictionary containing everything about the chat
messenger_chat = {
    'members':{},
    'total_messages':0,
    'word_count':0,
    'character_count':0,
    'image_count':0,
    'gif_count':0,
    'video_count':0,
    'link_count':0,
    'reaction_count':{
        'given':0,
        'reaction_counter':Counter(),
        },
    'other': {
        'like_usage':0,
        'emoji_usage':0,
        'emoji_counter':Counter(),
        'sticker_usage':0,
        'sticker_counter':Counter(),
    },
    'words_counter':Counter(),
}



def parse_words(payload):
    try:
        words = re.findall(r'\w+', payload['message'])
        words = [word.title() for word in words]
        messenger_chat['words_counter'].update(words)
    except TypeError:
        if payload['message'] is not None:
            print('Error: TimeStamp of {0}'.format(payload['date']))
            print('Message: "{0}"'.format(payload['message']))
        return False
    return True

def parse_participants(members):
    """ Given a String as dictated by Facebook Messenger, parse it into the messenger chat dictionary """
    members = members.replace('Participants:', '')
    members = members.replace(' and ', ', ')
    members = members.strip().split(', ')
    #print(members)
    for participant in members:
        messenger_chat['members'][participant] = {
            'word_count':0,
            'character_count':0,
            'image_count':0,
            'gif_count':0,
            'video_count':0,
            'link_count':0,
            'reaction_count':{
                'given':0,
                'received':0,
                'reaction_counter':Counter(),
                },
            'other': {
                'like_usage':0,
                'emoji_usage':0,
                'emoji_counter':Counter(),
                'sticker_usage':0,
                'sticker_counter':Counter(),
            },
            'words_counter':Counter(),
        }

#Runs the file
main(messenger_chat)

print(messenger_chat)
