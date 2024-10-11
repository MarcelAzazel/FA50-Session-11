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
reference = [-3,-2,-1,0,1,2,3]
print(sd(reference))
print(sd([-2, 1, 1, 3, 3, 4, 4]))

print(mean(reference))
print(mean([-2, 1, 1, 3, 3, 4, 4]))

print(range__(reference))
print(range__([-2, 1, 1, 3, 3, 4, 4]))