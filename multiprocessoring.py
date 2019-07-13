import os
import time
from multiprocessing import Process, current_process


def square(numbers):
    for number in numbers:
        time.sleep(0.5)
        result = number * number
        print(f'The number {number} squares to {result}')

if __name__ == '__main__':
    processes = []
    numbers = range(100)

    for i in range(50):
        process = Process(target=square, args=(numbers,))
        processes.append(process)

        # Processes are spawned by creating a Process object
        # then calling its start() method.
        process.start()

    for process in processes:
        process.join()
        
    print('Multiprocessing complete')

# def square(number):
#     result = number * number
#     process_id = os.getpid()
#     process_name = current_process().name
#     print(f'Process ID: {process_id}')
#     print(f'Process Name: {process_name}')
#     print(f'The number {number} squares to {result}')

# if __name__ == '__main__':
#     print(os.cpu_count())
#     processes = []
#     numbers = [1, 2, 3, 4]

#     for number in numbers:
#         process = Process(target=square, args=(number,))
#         processes.append(process)

#         # Processes are spawned by creating a Process object
#         # then calling its start() method.
#         process.start()