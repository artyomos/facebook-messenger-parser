'''
There is no explanation for what I will do in this file...

If you really want to figure it out, do the hard work I did
'''


from bs4 import BeautifulSoup as soup
import re
from collections import Counter

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


#Counter containing all words
word_list = Counter()


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
        #print('{0} on {1} said: "{2}"'.format(user,date,message)
        if (len(content[1].div.contents[1]) == 0):
            pass
        else:
            print('Error: TimeStamp of {0}'.format(date))
            #print(len(content[1].div.contents[1]))
            #print(content[1].div.contents[1].contents)
            message = ''
            for item in content[1].div.contents[1].contents:
                if isinstance(item, str):
                    message += item
            #print(type(content[1].div.contents[1].contents))
            print(message)
            try:
                words = re.findall(r'\w+', message)
                #print(words)
                words = [word.title() for word in words]

                word_list.update(words)
            except TypeError:
                print(message)




print(word_count)
print(character_count)

#TODO: Ignore common english words
print(word_list.most_common(50))
