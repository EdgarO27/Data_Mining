# -------------------------------------------------------------------------
# AUTHOR: Edgar Ortiz
# FILENAME: Similiar Documents
# SPECIFICATION: Find the most Similar documents based on cosine between vectors
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: current 5 hours
# -----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy or pandas.
#You have to work here only with standard dictionaries, lists, and arrays

# Importing some Python libraries
import csv
from sklearn.metrics.pairwise import cosine_similarity

documents = []

#reading the documents in a csv file
with open('cleaned_documents.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         documents.append (row)

#Building the document-term matrix by using binary encoding.
#You must identify each distinct word in the collection using the white space as your character delimiter.
#--> add your Python code here



#This holds all distinct words found in the documents
wordList = []


# #goes through a single doc
for singleDoc in documents[4:6]:
  #Make a new word list for every document to then make it the space we need for columns for each document
  
  #Looking inside a single document we skip the first index since its the number place of that document
  for words in singleDoc[1:]:

    #Here we need to get length of the word list to make the columns 
    for i in words.split(' '):

      #checks if word is part of columns
      if i not in wordList:
        wordList.append(i)

    # print(wordList)
  print(len(wordList))

docTermMatrix = []


'''
CSV 

'''

for singleDoc in range(0, 2):
#NESTED LIST COMPREHENSION

  #Appending a list inside a list
  docTermMatrix.append([1 if i in wordList else 0 for single in documents[:3] for word in single[1:] for i in word.split(' ')])



print(f'This is docuTermMartix indexed document index: {0}')

print(docTermMatrix[1])

print(f'This is the length of the index document with binary encoding')

print(len(docTermMatrix[1]))

print(f'This is the length of all the documents inside: {0}')

print(len(docTermMatrix))

print(f'This is the length of the wordList: {0}')

print(len(wordList))


for i in docTermMatrix:

  print(i)
  print()
  print(len(i))
test = docTermMatrix[1]
print(f'{" ".join(wordList[:7])}')

for i in test[:7]:
  print(i, " ")
  

# strings = [ ['foo', 'bar'], ['baz', 'taz'], ['w', 'koko'] ]
# test = [ (letter, idx) for idx, lst in enumerate(strings) for word in lst if len(word)>2 for letter in word]

# print(test)



# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> Add your Python code here


# Print the highest cosine similarity following the information below
# The most similar documents are document 10 and document 100 with cosine similarity = x
# --> Add your Python code here