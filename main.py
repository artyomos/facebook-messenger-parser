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

        payload = {
            'user':content[0].string,
            'message':content[1].div.contents[1].string,
            'date':content[2].string,
        }

        #Increase User's total message count
        messenger_chat['members'][payload['user']]['total_messages'] += 1
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
        #Parse through for images and videos
        parse_media(payload,message)
        #Find and parse links send in the chat
        parse_links(payload,message)

    print("Analysis was successful!")
    print('Writing to file anaylsis results...')


    #Give a usable list in console and write to file
    with open('messenger_stats.txt', 'w') as f:
        #Header
        f.write('File Generated Using Nate\'s Messenger Parser (https://github.com/artyomos/messenger-parser)\nVersion 0.0.1\n\n')

        # Group Chat Title
        f.write('Messenger Chat: {0}\n\n'.format(currentTitle))

        #Stats nnnnnnnnnnnn
        f.write('Total Messages: {0}\n'.format(messenger_chat['total_messages']))
        f.write('Word Count: {0}\n'.format(messenger_chat['word_count']))
        f.write('Character Count: {0}\n'.format(messenger_chat['character_count']))
        f.write('Images Sent: {0}\n'.format(messenger_chat['image_count']))
        f.write('Gifs Sent: {0}\n'.format(messenger_chat['gif_count']))
        f.write('Videos Sent: {0}\n'.format(messenger_chat['video_count']))
        f.write('Audio Files Sent: {0}\n'.format(messenger_chat['audio_count']))
        f.write('Links Sent: {0}\n'.format(messenger_chat['link_count']))
        f.write('Reactions Given: {0}\n'.format(messenger_chat['reaction_count']['given']))
        f.write('Reaction Totals:\n')
        for reaction in messenger_chat['reaction_count']['reaction_counter']:
            f.write('\t{0}:{1}'.format(reaction, messenger_chat['reaction_count']['reaction_counter'][reaction]))
        #TODO Add other section
        f.write('\nThe 50 Most Common Words:\n')
        words = remove_common(messenger_chat['words_counter']).most_common(50)
        for word in words:
            f.write('\t{0}:{1}'.format(word[0], word[1]))

        #User Stats
        #f.write('\n\nStats by User:')
        #for user in


def remove_common(counter):
    #Common useless messenger words
    common_words = ['A','An','The','I','To','And','That','Sent','Is','Photo','S','T','You','Of','Like', 'It', 'In','My','This','For','M','We','At','Was','On','So','But','Just','Be','Good','If','Ll']
    for word in common_words:
        del counter[word]
    return counter
#Dictionary containing everything about the chat
messenger_chat = {
    'total_messages':0,
    'word_count':0,
    'character_count':0,
    'image_count':0,
    'gif_count':0,
    'video_count':0,
    'audio_count':0,
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
    'members':{},
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
        #TODO Rewrite for loop
        index = 0 #Sad but necessary
        for user in giving_users:
            individual = messenger_chat['members'][user]
            individual['reaction_count']['given'] += 1
            individual['reaction_count']['given_counter'].update(pure_reactions[index])
            index += 1

        #print(giving_users)

def parse_media(payload, message):
    user = messenger_chat['members'][payload['user']]
    images = message.find_all('img')
    if images:
        for image in images:
            #If image is in fact a gif
            if image['src'][-3:] == 'gif':
                messenger_chat['gif_count'] += 1
                user['gif_count'] += 1
            else:
                #Otherwise update normally one at a time
                messenger_chat['image_count'] += 1
                user['image_count'] += 1
    videos = message.find_all('video')
    if videos:
        messenger_chat['video_count'] += len(videos)
        user['video_count'] += len(videos)
    audio = message.find_all('audio')
    if audio:
        messenger_chat['audio_count'] += len(audio)
        user['audio_count'] += len(audio)

def parse_links(payload, message):
    user = messenger_chat['members'][payload['user']]
    links = message.find_all('a')
    if links:
        for link in links:
            if link['href'][:4] == 'http':
                messenger_chat['link_count'] += 1
                user['link_count'] += 1

def parse_participants(members):
    """ Given a String as dictated by Facebook Messenger, parse it into the messenger chat dictionary """
    members = members.replace('Participants:', '')
    members = members.replace(' and ', ', ')
    members = members.strip().split(', ')
    #print(members)
    for participant in members:
        messenger_chat['members'][participant] = {
            'total_messages':0,
            'word_count':0,
            'character_count':0,
            'image_count':0,
            'gif_count':0,
            'video_count':0,
            'audio_count':0,
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
main(messenger_chat)
print(messenger_chat)
