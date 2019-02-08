from multiprocessing import Pool
import time

idan = [] #list for "loop"

def idan_tes(test):

    test = test*2
    time.sleep(5)
    print(test, "Process %s"  )





def loopy(): #insert to "idan list"
    for i in range(0,9999):
        idan.append(i)



def pool_handler(max):
    loopy()
    p = Pool(max) #limit thread
    p.map(idan_tes, idan)#runnug function base on the list


if __name__ == '__main__': #start point
    maxpro = 5 #limited thread
    pool_handler(maxpro) #start processing
