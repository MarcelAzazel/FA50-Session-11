def mean(database):
    totalsum = 0
    for i in database:
        totalsum += i
    return totalsum/len(database)

def sd(database):
    totalsum = 0
    average = mean(database)
    for i in database:
        totalsum += (i - average)**2
    return (totalsum/len(database))**0.5

def range__(database):
    database.sort()
    return database[-1] - database[0]

def median(database):
    database.sort()
    if len(database) % 2 == 0:
        median = (database[len(database)//2] + database[(len(database)//2) + 1])/2
    else:
        median = database[(len(database)//2) + 1]
    return median

sample = [-3,-2,-2,-2,-1,0,1,2,3,4]

reference = [-3,-2,-1,0,1,2,3]
for i in range(-3,4):
    for j in range(-3,4):
        for k in range(-3,4):
            for l in range(-3,4):
                for m in range(-3,4):
                    for n in range(-3,4):
                        for o in range(-3,4):
                            list = [i+1,j+1,k+1,l+1,m+1,n+1,o+1]
                            if sd(list) == sd(reference) and range__(list) == range__(reference) and mean(list) != mean(reference):
                                question1 = "Question 1: ", list, " and ", reference
                            elif sd(list) != sd(reference) and range__(list) == range__(reference) and mean(list) == mean(reference):
                                question2 = "Question 2: ", list, " and ", reference
                            elif sd(list) == sd(reference) and range__(list) != range__(reference) and mean(list) == mean(reference):
                                question3 = "Question 3: ", list, " and ", reference

print(question1)
print(question2)
print(question3)