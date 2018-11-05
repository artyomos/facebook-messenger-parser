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

    #Print Chat Name
    print('Performing analysis on {0}...'.format(file.title.string))

    print('Parsing the file...')

    #navigate to where messenger arranges the messages
    parser = file.body.div.div.div.contents[1].contents[1]

    #Get the current title
    currentTitle = file.title.string
    print(currentTitle)

    #Organizes the participants in their respective dictionary keys
    participants = parser.div.div.string
    parse_participants(participants)


    messages = parser.contents[1:]
    message_count = len(messages)
    print(message_count)

    #Word Count of all messages
    word_count = 0
    #Character Count of all messages
    character_count = 0





    #Iterate through all messages
    for message in messages:
        content = message.contents
        user = content[0].string
        #print(user)
        message = content[1].div.contents[1].string
        #print(message)
        date = content[2].string
        #print(date)
        if not parse_words(message, date):
            # If the message is not Null, fix the mesage with no linebreak statements
            if (len(content[1].div.contents[1]) != 0):
                message = ''
                for item in content[1].div.contents[1].contents:
                    if isinstance(item, str):
                        message += item
                if not parse_words(message, date):
                    print("Failed :(")



    print(word_count)
    print(character_count)

    #TODO: Ignore common english words
    print(messenger_chat['chat_words'].most_common(50))


#Create a dictionary of participants
chat_participants = dict()

#Dictionary containing everything about the chat
messenger_chat = {
    'members':{},
    'chat_word_count':0,
    'chat_character_count':0,
    'chat_reaction_count':0,
    'chat_image_count'
    'chat_counter':Counter(),
}

template = {
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
#TODO change to dictionary payload
def parse_words(message, date):
    try:
        words = re.findall(r'\w+', message)
        words = [word.title() for word in words]
        messenger_chat['chat_words'].update(words)
    except TypeError:
        if message is not None:
            print('Error: TimeStamp of {0}'.format(date))
            print('Message: "{0}"'.format(message))
        return False
    return True

def parse_participants(members):
    #Very clever variable names I know
    members = members.replace('Participants:', '')
    members = members.replace(' and ', ', ')
    members = members.strip().split(', ')
    #print(members)
    for participant in members:
        messenger_chat['members'][participant] = {
        'word_count':0,
        'character_count':0,
        'aliases':[],
        }
    print(messenger_chat)

#Runs the file
main(messenger_chat)
