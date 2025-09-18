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

# # 2
# We then use nested list comphrehension 
'''
  To build a matrix we have to understand that we must have one big list that for every row has a list with its own count of words 
  DocMatrix = [ [doc1] ,  [doc2] ,  [doc3]  ,  [doc4] ]
'''

for _ in documents:

  docTermMatrix.append([0] * len(wordList))


print("PART 2 done")

#---------------------------------------------------------------------------------------------------------------------------

#     #           STEP 3

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


      
        


      




# for singleDoc in range(0, len(documents)):
# #NESTED LIST COMPREHENSION

#   #Appending a list inside a list
#   docTermMatrix.append([1 if i in wordList else 0 for single in documents for word in single[1:] for i in word.split(' ')])

print("Part 3 of Main codebase")
print()





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
# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> Add your Python code here


# Print the highest cosine similarity following the information below
# The most similar documents are document 10 and document 100 with cosine similarity = x
# --> Add your Python code here



simlarities = cosine_similarity(docTermMatrix)
doc1 = 0
doc2 =0
max_sim = 0
for i in range(len(simlarities)):
  for j in range(len(simlarities)):
    if i != j:
      if simlarities[i][j] > max_sim:
        max_sim = simlarities[i][j]
        doc1,doc2 = i,j







print(simlarities[55][66])
print(f'The most similar documents are {doc1+ 1} and {doc2+ 1} with cosine simliarity {simlarities[doc1][doc2]}.')











