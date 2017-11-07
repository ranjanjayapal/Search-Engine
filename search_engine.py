# import occ_list.py into this file to use the dictionary stored there
from occ_list import *
# specify a variable _end to mark the end of a trie
_end = '_end_'

# function to form a trie structure for all the words in the dictionary
def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = occ_lst.keys().index(word)
    return root

# function to check if a word entered by the user is actually present in the trie.
# if it is present return the external node containing the index of the word in occ_lst
def ext_node_of_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return False
    else:
        if _end in current_dict:
            return current_dict[_end]
        else:
            return False

# retrieve all the keys from occ_lst
keys = occ_lst.keys()
# make a trie of all the words present in the document
rt = make_trie(keys)
chck = 'Y'
# check if the user wants to do a search or not
while chck != 'N' and chck != 'n':
    # check if the user entered anything other than a 'y' or 'Y'
    while chck != 'Y' and chck != 'y':
        chck = raw_input('Do you want to make another query? (Y/N)')
        if chck == 'N' or chck == 'n':
            break
    # request for a keyword from the document
    str = raw_input('Enter the keyword to search for a document: ')
    # since this search engine elables multiple keyword search we need to split it based on space
    str = str.split()
    for i in str:
        # retrieve the external node containing the index of the word in the occ_lst
        ret = ext_node_of_trie(rt, i)
        # if word cannot be found in the document
        if ret is False:
            print "\n\"" + i + "\" is not present in any of the document"
            continue
        # get the key from occ_lst based on the index retrieved from trie
        key = occ_lst.keys()[ret]
        # get the value of the key which gives the document numbers that the word is present in
        value = occ_lst[key]
        # print out all the documents that each word is present in
        print "\n\"" + i + "\" is present in the following documents: "
        for j in value:
            print doc_lst[j]
    print ""
    # check if the user wants to make another query
    chck = raw_input('Do you want to make another query? (Y/N)')
print "Thank you for your search"
