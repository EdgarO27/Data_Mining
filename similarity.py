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

docTermMatrix = []

# for singleDoc in documents:
#   for words in singleDoc[1:2]:
#     for i in words.split(' '):
#       if i not in docTermMatrix:
#         docTermMatrix.append([i])

#   #Iterate through documents one by one 

for singleDocument in documents[0:1]:
  wordList = []
#   #Iterate through all words skip the first index of document
#   #since document has a size of 2
#   #Outline :    ['1', 'word1 word2 word3 word4 word5']
  for letters in singleDocument[1:]:
    #   # We are iterating through the index of words 
    #   # So now we have to create each entry based on the size of a specific document
    #   #Make a word list that will add words 
    #   #
    for i in letters.split(' '):
        wordList.append(i)

      
        # if i not in docTermMatrix:
        #   docTermMatrix.append([0])
        # else:
        #    docTermMatrix.append(1)


for singleDocument in documents
    
    

print(wordList[0])









# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> Add your Python code here


# Print the highest cosine similarity following the information below
# The most similar documents are document 10 and document 100 with cosine similarity = x
# --> Add your Python code here