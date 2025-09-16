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
import time
documents = []

#reading the documents in a csv file
with open('cleaned_documents.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         documents.append (row)

#Building the document-term matrix by using binary encoding.
#You must identify each distinct word in the collection using the white space as your character delimiter.


#Hold the matrix of all binary classification
docTermMatrix = []

#This holds all distinct words found in the documents for columns based on each row 
wordList = []



#------------------------------------------------------------------------------------

#     #           STEP 1
# #goes through a single doc
for singleDoc in documents:
  #Make a new word list for every document to then make it the space we need for columns for each document
  
  #document [1, [ words here ] ] we skip past the number of document since the count of rows can be done with python 
  for words in singleDoc[1:]:

    # We grab words here from the long string and extract each while taking out spaces
    for i in words.split(' '):

      #checks if word is already apart from wordLisr
      if i not in wordList:
        wordList.append(i)



print("Part one done")

#OUR MATRIX WE make the same amount of Docuemnts with equal amount of indexes

for _ in documents:

  docTermMatrix.append([0] * len(wordList))



#---------------------------------------------------------------------------------------------------------------------------

#     #           STEP 2


'''
Doctermmatrix has same amount of documents to counteract errors in cosine similarity

    FIRST ITERATION OF BINARY CLASSIFICATION ALGO

    1.Use document to iterate through all docs

    2.then we need to iterate through a doc one by one 


'''

#FIRST ITERATION


#DOCUMENT TERM WORD MATRIX 

    #COLUMN   WORD1 WORD2 WORD3 WORD4 WORD5 WORD6
#ROW

#DOC1         1       0

#DOC2

#DOC3

#DOC4

#DOC5

#     DOCUMENTS USING RANGE TO ACCESS DOCUMENtMATRIX by row 
for i in range(len(documents)):
  dummy = documents[i]
  #try to iterate through by Columns 
  # we use enumerate for word List to go through list 
  for index, words in enumerate(wordList):

    for term in dummy[1:]:
      if words in term:
        docTermMatrix[i][index] = 1


      
        


      
print(docTermMatrix[0])



# for singleDoc in range(0, len(documents)):
# #NESTED LIST COMPREHENSION

#   #Appending a list inside a list
#   docTermMatrix.append([1 if i in wordList else 0 for single in documents for word in single[1:] for i in word.split(' ')])

print("Part 2 of Main codebase")

#Test Outputs



fin = cosine_similarity(docTermMatrix)



print(fin)

# for i in docTermMatrix:

#   print(i)
#   print()
#   print(len(i))
# test = docTermMatrix[1]
# print(f'{" ".join(wordList[:7])}')

# for i in test[:7]:
#   print(i, " ")
  






#EXAMPLE FOR NESTED COMPREHENSION
# strings = [ ['foo', 'bar'], ['baz', 'taz'], ['w', 'koko'] ]
# test = [ (letter, idx) for idx, lst in enumerate(strings) for word in lst if len(word)>2 for letter in word]

# print(test)


#STEPS

# # 1
# We split our documents from its number and grab the number of documents we have 
    # We have 401 documents in cleaned_documents.csv ( column seperated Values)
'''
  We have to understand that in this process we look at all the words in the documents 
  This helps us gather all distinct words that helps us add as a column 
  For example,
        Lets say we have the word budget its going to look at every row if it has budget and will make it a 1 if it appears regardless how many times
'''

# # 2
# We then use nested list comphrehension 
'''
  To build a matrix we have to understand that we must have one big list that for every row has a list with its own count of words 
  DocMatrix = [ [doc1] ,  [doc2] ,  [doc3]  ,  [doc4] ]
'''

# # 3
# We have to then go through all all documents and understand what the outputs looks like
'''
  In our output we have to understand if our current Hard coded baby algo works 
    To test,
      I will start with document 1 and look at the number of 1's it shows if it shows a single zero that means i have a bug somewhere 
      since it has only gathered words from document 1
'''


# # 4
# Use COSINE SIMILARITIES 

'''
Look at Scikit learn library to uderstand how to make sure every document is counted 

COSINE SIMIALIRTY IS DEFINED :
  1. TWO document Vectors ( d1,  d2 )
  2. then,   cos( d1  , d2  ) = ( d1 * d2 ) //  ||d1|| ||d2||
  3. (  d1  * d2  ) indicates dot product
  4. ||d|| length of vector d
  5. Python Library defines the use of COSINE_SIMILARITY ( X, Y ) 
    needs to have 2d array
  NOTE:
    We have to see how to find the most common similarities by each document

'''
start_time = time.time()
print(time.time()- start_time)

# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> Add your Python code here


# Print the highest cosine similarity following the information below
# The most similar documents are document 10 and document 100 with cosine similarity = x
# --> Add your Python code here