import threading
import ScrapeUVAPS


username = input('Enter Computing ID Username: ')
password = input('Enter Computing ID Password: ')

threads = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(threads)):
    t = threading.Thread(target=ScrapeUVAPS.UVAPSComputerIDS, args=(username, password, i))
    threads.append(t)
    t.start()

#TODO: Gather names from classes
