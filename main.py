'''
There is no explanation for what I will do in this file...

If you really want to figure it out, do the hard work I did
'''


from bs4 import BeautifulSoup as soup
import re
from collections import Counter

def main():
    print('Nate\'s HTML Parser - Version 0.0.1')
    print('\nPlease wait while the document loads... For large files this could take upwards of several minutes...')

    with open('message.html') as html:
        file = soup(html, 'html.parser')

    print('File has finished loading. Parsing data...\n')

    #Print Chat Name
    print('Performing analysis on {0}...'.format(file.title.string))

    print('Parsing the file...')

    #Create a dictionary of participants
    participants = dict()

    #Create a dictionary of the participant's names
    aliases = dict()

    #print(file.body.div)
    #Loop through every tag in the file

    #navigate to where messenger arranges the messages
    parser = file.body.div.div.div.contents[1].contents[1]
    #print(parser)
    #Get the current title
    currentTitle = file.title.string
    print(currentTitle)

    #TODO organize into dictionary
    participants = parser.div.div.string
    print(participants)


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
        try:
            word_count += len(message.split())
            character_count += len(message)

            words = re.findall(r'\w+', message)
            #print(words)
            words = [word.title() for word in words]

            word_list.update(words)
        except:
            # If the message is not Null, fix the mesage with no linebreak statements
            if (len(content[1].div.contents[1]) != 0):
                message = ''
                for item in content[1].div.contents[1].contents:
                    if isinstance(item, str):
                        message += item
                parseWords(message, date)



    print(word_count)
    print(character_count)

    #TODO: Ignore common english words
    print(word_list.most_common(50))

#Counter containing all words
word_list = Counter()

def parseWords(message, date):
    try:
        words = re.findall(r'\w+', message)
        words = [word.title() for word in words]
        word_list.update(words)
    except TypeError:
        print('Error: TimeStamp of {0}'.format(date))
        print('Message: "{0}"'.format(message))
        return False
    return True




#Runs the file
main()
