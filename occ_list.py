
doc_lst = dict()
# Index all the documents
doc_lst[1] = "dataset"
doc_lst[2] = "dataset1"
doc_lst[3] = "dataset2"
# Set up a dictionary for the occurrence list
occ_lst = dict()
# Create file handler so to read the documents and store the key, value pair for each word
fhand = open('dataset', 'r')
for line in fhand:
    line = line.strip()
    words = line.split()
    for word in words:
        if word not in occ_lst:
            occ_lst[word] = [1]
fhand1 = open('dataset1', 'r')
for line in fhand1:
    line = line.strip()
    words = line.split()
    for word in words:
        if word not in occ_lst:
            occ_lst[word] = [2]
        else:
            occ_lst[word].append(2)
fhand2 = open('dataset2', 'r')
for line in fhand2:
    line = line.strip()
    words = line.split()
    for word in words:
        if word not in occ_lst:
            occ_lst[word] = [3]
        else:
            occ_lst[word].append(3)
# print the occurrence list created above
print "----------------------------------------------"
print "Occurrence list: "
print "---------------"
for i in occ_lst:
    print i + ":", occ_lst[i]
print "----------------------------------------------"
