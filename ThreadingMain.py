'''
Christopher Geier Presents:

Threading options to use ScrapeUVAPS
'''
import threading
import ScrapeUVAPS
import multiprocessing
from multiprocessing.pool import ThreadPool
import time

username = input('Enter Computing ID Username: ')
password = input('Enter Computing ID Password: ')

letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(letterList)):
    ScrapeUVAPS.UVAPSComputerIDS(username, password, letterList[i])

# threadsae = ['a', 'b', 'c', 'd', 'e']
# threadsfj = ['f', 'g', 'h', 'i', 'j']
# threadsko = ['k', 'l', 'm', 'n', 'o']
# threadspt = ['p', 'q', 'r', 's', 't']
# threadsuz = ['u', 'v', 'w', 'x', 'y', 'z']

# threads = ['a', 'b']

# pool = ThreadPool(processes=1)
# for i in range(len(threads)):
#     async_result = pool.apply_async(ScrapeUVAPS.UVAPSComputerIDS, (username, password, threads[i])) # tuple of args for foo
# return_val = async_result.get()

# do some other stuff in the main process

# jobs = []
# for i in range(len(threadsae)):
#     t = threading.Thread(target=ScrapeUVAPS.UVAPSComputerIDS, args=(username, password, threadsae[i]))
#     jobs.append(t)
#     t.start()
# for j in jobs:
#     j.join()
# jobs = []
# for i in range(len(threadsfj)):
#     t = threading.Thread(target=ScrapeUVAPS.UVAPSComputerIDS, args=(username, password, threadsfj[i]))
#     threadsfj.append(t)
#     t.start()
#     t.join()
# for j in jobs:
#     j.join()
# jobs = []
# for i in range(len(threadsko)):
#     t = threading.Thread(target=ScrapeUVAPS.UVAPSComputerIDS, args=(username, password, threadsko[i]))
#     threadsko.append(t)
#     t.start()
#     t.join()
# for j in jobs:
#     j.join()
# jobs = []
# for i in range(len(threadspt)):
#     t = threading.Thread(target=ScrapeUVAPS.UVAPSComputerIDS, args=(username, password, threadspt[i]))
#     threadspt.append(t)
#     t.start()
#     t.join()
# for j in jobs:
#     j.join()
# jobs = []
# for i in range(len(threadsuz)):
#     t = threading.Thread(target=ScrapeUVAPS.UVAPSComputerIDS, args=(username, password, threadsuz[i]))
#     threadsuz.append(t)
#     t.start()
#     t.join()
# for j in jobs:
#     j.join()

# for j in jobs:
#     j.

#compids = open('intermediate_file','w')

#ScrapeUVAPS.UVAPSProfileInfo(username, password, compids)

#TODO: Gather names from classes
