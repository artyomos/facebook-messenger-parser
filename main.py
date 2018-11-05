'''
There is no explanation for what I will do in this file...

If you really want to figure it out, do the hard work I did
'''


from bs4 import BeautifulSoup as soup

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

#for message in messages:
    #print(message)
