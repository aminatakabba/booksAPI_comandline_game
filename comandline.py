# Imported libraries that will be required 
import requests # helps fetching apis
import pprint # makes json files much more readable
import time

# ========== INTRODUCTION TO THE APP ================
print('Hello, bookholic :), welcome to Ami\'s library')
# time.sleep(2) # Allows user to have sometime to read
print('This is the best place to find your favourite books, new and interesting reads')
# time.sleep(2) # Allows user to have sometime to read
url = "https://www.googleapis.com/books/v1/volumes?q=" # API URL
interest = input('What interests you?  You can write the author, book title or genra that comes to your mind \n') # User will add what type of books they're looking for
urlInterest = str(url + interest) # Attaches the standard url to the input from the user

# =============== BOOKS SECTION ====================== 
print("This is the list of the 5 closes books to what you want \n")

authSent = "Author: " 
titleSent = "Title: "
pubSent = "Publisher: "

#Book Number 1
author = requests.get(urlInterest).json()['items'][0]['volumeInfo']['authors'][0] # Finds the author
print(authSent + author)
title = requests.get(urlInterest).json()['items'][0]['volumeInfo']['title'] # Finds the title
print(titleSent + title)
publishing = requests.get(urlInterest).json()['items'][0]['volumeInfo']['publisher'] # Finds the publishing company
print(pubSent + publishing)
print("\n")

#Book Number 2
author2 = requests.get(urlInterest).json()['items'][2]['volumeInfo']['authors'][0]
print(authSent + author2)
title2 = requests.get(urlInterest).json()['items'][2]['volumeInfo']['title']
print(titleSent + title2)
publishing2 = requests.get(urlInterest).json()['items'][2]['volumeInfo']['publisher']
print(pubSent + publishing2)
print("\n")

#Book Number 3
author3 = requests.get(urlInterest).json()['items'][3]['volumeInfo']['authors'][0]
print(authSent + author3)
title3 = requests.get(urlInterest).json()['items'][3]['volumeInfo']['title']
print(titleSent + title3)
publishing3 = requests.get(urlInterest).json()['items'][3]['volumeInfo']['publisher']
print(pubSent + publishing3)
print("\n")

#Book Number 4
author4 = requests.get(urlInterest).json()['items'][4]['volumeInfo']['authors'][0]
print(authSent + author4)
title4 = requests.get(urlInterest).json()['items'][4]['volumeInfo']['title']
print(titleSent + title4)
publishing4 = requests.get(urlInterest).json()['items'][4]['volumeInfo']['publisher']
print(pubSent + publishing4)
print("\n")

#Book Number 5
author5 = requests.get(urlInterest).json()['items'][5]['volumeInfo']['authors'][0]
print(authSent + author5)
title5 = requests.get(urlInterest).json()['items'][5]['volumeInfo']['title']
print(titleSent + title5)
publishing5 = requests.get(urlInterest).json()['items'][5]['volumeInfo']['publisher']
print(pubSent + publishing5)
print("\n")


# ============ ADDING ITEMS TO THE READING LIST ==========
readingList = input("Would you like to add any books into your reading list? Y/N ")
if readingList == 'Y' or readingList == 'y':
    list = []
    # Options to add the book to your reading list 
    print('Press \'a\' if you want to add the book to your reading list and any other letter if not')
    time.sleep(2)
    one = input(title + ' ')
    print(one)

    two = input(title2+ ' ')
    print(two)

    three = input(title3 + ' ')
    print(three)

    four = input(title4 + ' ')
    print(four)

    five = input(title5 + ' ')
    print(five)
    
    # If the user replied a it will be added to the list
    if one == 'a':
        list.append(title)
    if two == 'a':
        list.append(title2)
    if three == 'a':
        list.append(title3)
    if four == 'a':
        list.append(title4)
    if five == 'a':
        list.append(title5)
    print("This is your reading list, enjoy and hope to see you soon") # End of the program
    time.sleep(1)
    print(list)
elif readingList == "N" or readingList == 'n':
    print("Hava a nice day and thats for coming to Ami's library") # End of the program
