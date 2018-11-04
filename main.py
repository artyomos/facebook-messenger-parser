from bs4 import BeautifulSoup as soup

print('Nate\'s HTML Parser - Version 0.0.1')
print('\nPlease wait while the document loads... For large files this could take upwards of several minutes...')

with open('message.html') as html:
    file = soup(html, 'html.parser')

print('File has finished loading. Parsing data...')

print('Performing analysis on {0}...'.format(file.title.string))
