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

print(file.body.div.contents)
#Loop through every tag in the file
tag = file.body
while len(tag) > 0:
    #print (str(tag) + ' ')
    tag = tag.div
    print(type(tag))
    if (tag == None):
        break
