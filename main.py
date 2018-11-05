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
        #Parse through the words
        if not parse_words(payload):
            # If the message is not Null, fix the mesage with no linebreak statements
            if not content[1].div.contents[1]:
                message = ''
                for item in content[1].div.contents[1].contents:
                    if isinstance(item, str):
                        message += item
                payload['message'] = message
                if not parse_words(payload):
                    print("A Secondary Parse Failed... :(")
        #Parse through the reactions
        parse_reactions(payload, message)
        #Parse through for images
        #Others?
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

        #Update Chat Values
        messenger_chat['words_counter'].update(words)
        messenger_chat['word_count'] += len(words)
        messenger_chat['character_count'] += len(''.join(words))

        #Update User's Values
        user = messenger_chat['members'][payload['user']]
        user['words_counter'].update(words)
        user['word_count'] += len(words)
        user['character_count'] += len(''.join(words))
    except TypeError:
        if payload['message'] is not None:
            print('Error: TimeStamp of {0}'.format(payload['date']))
            print('Message: "{0}"'.format(payload['message']))
        return False
    except KeyError:
        print("Discovered person who left chat!")
        return False
    return True

def parse_reactions(payload, message):
    reactions = message.find_all('li')
    if reactions:
        pure_reactions = [obj.string[:1] for obj in reactions]
        #print(pure_reactions)

        #Update Chat Values
        messenger_chat['reaction_count']['given'] += len(reactions)
        messenger_chat['reaction_count']['reaction_counter'].update(pure_reactions)

        #Update User Values
        receiving_user = messenger_chat['members'][payload['user']]
        giving_users = [obj.string[1:] for obj in reactions]

        #Receiving User
        receiving_user['reaction_count']['received'] += len(reactions)
        receiving_user['reaction_count']['received_counter'].update(pure_reactions)

        #Giving Users
        index = 0 #Sad but necessary
        for user in giving_users:
            individual = messenger_chat['members'][user]
            individual['reaction_count']['given'] += 1
            individual['reaction_count']['given_counter'].update(pure_reactions[index])
            index += 1

        #print(giving_users)


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
                'given_counter':Counter(),
                'received_counter':Counter(),
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
#main(messenger_chat)

#print(messenger_chat)
'''
file = soup('<div class="pam _3-95 _2pi0 _2lej uiBoxWhite noborder"> <div class="_3-96 _2pio _2lek _2lel">Ben Richards</div> <div class="_3-96 _2let"> <div> <div/> <div/> <div/> <div/> <div> <div> <a href="messages/JammyJimmysII_df3ac54957/photos/28126344_417494668672627_1069695574_o_417494668672627.png"> <img src="messages/JammyJimmysII_df3ac54957/photos/28126344_417494668672627_1069695574_o_417494668672627.png" class="_2yuc _3-96" /> </a> </div> </div> <div> <ul class="_tqp"> <li>😍Alexander Romios</li> <li>😍Ryan De Leon</li> </ul> </div> </div> </div> <div class="_3-94 _2lem">Feb 16, 2018 10:17pm</div> </div>', 'html.parser')
print(file.div.li.contents)

ap = file
print(ap)
print(ap.find_next_siblings('li'))
'''
