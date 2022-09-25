"""
In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below,
extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Kassia.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: T
Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment
without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point.
The point is to write a clever Python program to solve the program.
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for i in range(count):
    print('Retrieving: ', tags[position-1].get('href', None))
    url = tags[position-1].get('href', None)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
print('Last name in sequence: ', tags[position-1].contents[0])

# Enter URL: http://py4e-data.dr-chuck.net/known_by_Kassia.html
# Enter count: 7
# Enter position: 18






