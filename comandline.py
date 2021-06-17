# Imported libraries that will be required 
import requests # helps fetching apis
import pprint
import time

# ========== INTRODUCTION TO THE APP ================
print('Hello, bookholic :), welcome to Ami\'s library \n')
time.sleep(2) # Allows user to have sometime to read
print('This is the best place to find your favourite books, new and interesting reads \n')
time.sleep(2) # Allows user to have sometime to read
url = "https://www.googleapis.com/books/v1/volumes?q=" # API URL
interest = input('What interests you?  You can write the author, book title or genra that comes to your mind \n') # User will add what type of books they're looking for
urlInterest = str(url + interest) # Attaches the standard url to the input from the user

# ============ API ERROR HANDLING SECTION ================== 
apiHandle = requests.get(urlInterest)
if apiHandle.status_code == 200: # If the request is successful
    print('Success!')
    print("This is the list of the 5 closest books to what you want \n")
else: # This will handle 404, 500 and all other types
    print('Not Found. Please run the app again and enter a valid value')

# =============== BOOKS SECTION ====================== 

requesting = requests.get(urlInterest).json()
items = requesting['items']

for item in items:
    author = item['volumeInfo']['authors'] # Find the authors
    title = item['volumeInfo']['title'] # Find the title of the book
    publisher = item['volumeInfo']['publisher'] # Find the publishing company
    print("AUTHORS: " )
    print(author)
    print("TITLE: \n" + title)
    print("PUBLISHER: \n" + publisher)    
    print("\n")


# ============ ADDING ITEMS TO THE READING LIST ==========
readingList = input("Would you like to add any books into your reading list? Y/N ")
if readingList == 'Y' or readingList == 'y':
    list = [] # Items that the costumer wants on their reading list will be added to this empty list
    print('Press \'a\' if you want to add it to your reading list or any other if not \n') # Instructions on how to add items to the reading list
    for item in items:
        readingListTitle = item['volumeInfo']['title'] # Shows the title of the book
        time.sleep(1)
        question = input(readingListTitle + " ")
        print(question)

        if question == 'a':
            list.append(readingListTitle) # Only the title of the book will be added to the reading list
    print("THIS IS YOOUR READING LIST \n")
    lists = pprint.pprint(list)
    print(lists)
    print("\n Thanks for coming to Ami\'s library, we hope to see you soon :)")
else:
    print("Thanks for coming to Ami\'s library, have an amazing day and see you soon :)")