import random
import time
from MasterClass import masterClass

#class for measuring time taken for sorting 
class count:
    start = 0
    end = 0
    
    #trigger start timer
    def startTimer(self):
        self.start = time.time()

    #trigger stop timer
    def stopTimer(self):
        self.end = time.time()

    #get start varaible value 
    def get_start(self):
        return self.start

    #get end varaible value
    def get_end(self):
        return self.end

    #calculate time taken 
    def get_timeTaken(self):
        return self.get_end() - self.get_start()

    #reset start and end varaibles
    def reset(self):
        self.set_start(0.0)
        self.set_end(0.0)

    #set start varaible to a specified value
    def set_start(self, val):
        self.start = val

     #set end varaible to a specified value
    def set_end(self, val):
        self.end = val

    #trigger sorting algorithm process and record time taken
    def type(self, algo, list, listnum):
        algotype = ""               #string varaible to output on terminal 
        self.startTimer()           #start timer

        if algo == 1:
            algotype = "Selection Sort "
            masterClass.selectionSort(list, len(list) - 1, 0)
            writeTofile("list_" + str(listnum) + "_sorted-" + algotype + ".txt", list)

        if algo == 2:
            algotype = "Merge Sort "
            sortedList = masterClass.mergeSort(list)
            writeTofile("list_" + str(listnum) + "_sorted-" + algotype + ".txt", sortedList)

        if algo == 3:
            algotype = "Quick Sort "
            masterClass.quickSort(list, 0, len(list) -1)
            writeTofile("list_" + str(listnum) + "_sorted-" + algotype + ".txt", list)

        self.stopTimer()                            #stop timer
        runtime = self.get_timeTaken()              #calculate runtime
        print(algotype + " : " + str(runtime))      #output runtime 

#in built function in python random library that returns a list of random numbers within a given range with no duplicates
def randlist_(length, min, max):
    return random.sample(range(min, max), length)

#function to generate ranom numbers within a given range with no duplicates
def randlist(length, min, max):
    list = []
    for i in range(length):
        found = False
        #while loop to keep generating random numbers if the same number is already on the list
        while found == False:

            #random number
            num = random.randint(min, max)

            #varaible to break out of the while loop
            found2 = True

            #for loop to iterate through the list
            for j in range(len(list)):
                #statment to check if number generated is in the list
                if list[j] == num:
                    found2 = False
            #if number is already there, keep goin
            if found2 == False:
                found = False
            #if number is not there, break out of while loop
            else:
                found = True
        #append number to list
        list.append(num)
    return list

#function to write content to a text file
def writeTofile(filename, list):
        #open file in wirting mode
        file = open(filename, "w") 
        for i in list:
            file.write(str(i) + "\n")
        file.close()


#generating lists
list_1 = randlist_(10000 , 1000000, 9999999)   #list for 10,000
list_2 = randlist_(100000 , 1000000, 9999999)   #list for 100,000
list_3 = randlist_(1000000   , 1000000, 9999999)   #list for 1,000,000   

#test lists 
#list_1 = randlist_(5 , 1, 20)   
#list_2 = randlist_(10 , 1, 20)   
#list_3 = randlist_(15 , 1, 20)   

#writing lists to text files
writeTofile("list_1_unsorted.txt", list_1)
writeTofile("list_2_unsorted.txt", list_2)
writeTofile("list_3_unsorted.txt", list_3)

# three empty temporary arrays to store array of random values before sorting to show sorting algorithms work indiviually
temp1 = []
temp2 = []
temp3 = []

#adding values to temporary array from random array
for i in list_1:
    temp1.append(i)
    temp2.append(i)
    temp3.append(i)

#list 1 on all sorting algorithms
print("list 1: ")
timer = count()

#selection sort
timer.type(1, temp1, 1)
timer.reset()

#merge sort
timer.type(2, temp2, 1)
timer.reset()

#quick sort
timer.type(3, temp3, 1)
timer.reset()

print()
#emptying all lists 
temp1 = []
temp2 = []
temp3 = []

#adding values to temporary array from random array
for i in list_2:
    temp1.append(i)
    temp2.append(i)
    temp3.append(i)

#list 1 on all sorting algorithms
print("list 2: ")

#selection sort
#timer.type(1, temp1, 2)
#timer.reset()

#merge sort
timer.type(2, temp2, 2)
timer.reset()

#quick sort
timer.type(3, temp3, 2)
timer.reset()

print()
#emptying all lists
temp1 = []
temp2 = []
temp3 = []

#adding values to temporary array from random array
for i in list_3:
    temp1.append(i)
    temp2.append(i)
    temp3.append(i)

#list 1 on all sorting algorithms
print("list 3: ")

#selection sort
#timer.type(1, temp1, 3)
#timer.reset()

#merge sort
timer.type(2, temp2, 3)
timer.reset()

#quick sort
timer.type(3, temp3, 3)
timer.reset()



