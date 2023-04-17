import os

InterDir = ""
Reducers = 0

def partition(intermediate, index):
    mapper_dir = 'datafiles/intermediate/mapper'+str(index)
    if not os.path.exists(mapper_dir):
        os.makedirs(mapper_dir)

    for inter in intermediate:
        string = str(inter)
        partition = len(string[2:-5])%Reducers
        InterDir = mapper_dir+'/Inter'+str(partition+1)+'.txt'

        with open(InterDir, "+a") as f:
            f.write(str(inter))
            f.write("\n")


def wordCount(InputDir, index):
    global InterDir 
    intermediate = []

    with open(InputDir, "r") as f:
        content = f.read()

    listOfWords = content.split()
    for word in listOfWords:
        intermediate.append((word, 1))

    partition(intermediate, index)


def invertedIndex(InputDir, index):
    global InterDir 
    intermediate = []

    with open(InputDir, "r") as f:
        content = f.read()

    listOfWords = content.split()
    for word in listOfWords:
        intermediate.append((word, index))

    partition(intermediate, index)


def naturalJoin(InputDir, index):
    InputDir1 = InputDir + '_table1.txt'
    InputDir2 = InputDir + '_table2.txt'
    values_tab1 = []
    values_tab2 = []
    columns = []

    with open(InputDir1, "r") as f:
        for i, line in enumerate(f):
            content = line.strip()
            if i == 0:
                columns.append(content.split(", "))
            else:
                values_tab1.append(content.split(", "))

    with open(InputDir2, "r") as f:
        for i, line in enumerate(f):
            content = line.strip()
            if i == 0:
                columns.append(content.split(", "))
            else:
                values_tab2.append(content.split(", "))

    common_element = list(set(columns[0]).intersection(set(columns[1])))

    ind_tb1 = columns[0].index(common_element[0])
    ind_tb2 = columns[1].index(common_element[0])

    pairs1 = {}
    pairs2 = {} 

    for i in range(len(values_tab1)):
        if values_tab1[i][ind_tb1] not in pairs1.keys():
            intermed = []
        else:
            intermed = pairs1[values_tab1[i][ind_tb1]]

        for j in range(len(values_tab1[i])):
            if j != ind_tb1:
                intermed.append(('T1', values_tab1[i][j]))

        pairs1[values_tab1[i][ind_tb1]] = intermed

    for i in range(len(values_tab2)):
        if values_tab2[i][ind_tb2] not in pairs2.keys():
            intermed = []
        else:
            intermed = pairs2[values_tab2[i][ind_tb2]]
        
        for j in range(len(values_tab2[i])):
            if j != ind_tb2:
                intermed.append(('T1', values_tab2[i][j]))

        pairs2[values_tab2[i][ind_tb2]] = intermed

    partition(pairs1, pairs2, index)


def startMapper(InputDir, RequestType, index, Reducer):
    global Reducers
    Reducers = Reducer

    if RequestType == 1:
        wordCount(InputDir, index)
    elif RequestType == 2:
        invertedIndex(InputDir, index)
    else:
        naturalJoin(InputDir, index)