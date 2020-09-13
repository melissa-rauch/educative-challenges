from queue import Queue

def find_bin(n):
    """Given a postive integer 'n' generate binary numbers from 1 to n in 
    the form of a string using a queue.
    1.Start with Enqueuing 1
    2.Dequeue a number from queue
    3.append 0 to it and enqueue it back to queue.
    4.Perform step 2 but with appending 1 to the
    origional number and enqueue back to queue.

    Queue takes integer values so before enqueueing it make
    sure to convert String to integer. Size of Queue should
    be 1 more than number because for a single number we're
    enqueing two variations of it , one with appended 0
    while other with 1 being appended.

    Doctest:
    >>> find_bin(3)
    ['1', '10', '11']
    """
    # create and empty list to hold found binary numbers
    found_binary = []
    # initialize the queue
    queue = Queue()
    #begin by enqueueing 1, sine we're starting at 1 and going to n
    queue.enqueue(1)
    for i in range(n):
        found_binary.append(str(queue.dequeue()))
        print(found_binary)
        string_1 = found_binary[i] + "0"
        print("string1: ", string_1)
        string_2 = found_binary[i] + "1"
        print("string2: ", string_2)
        queue.enqueue(string_1)
        queue.enqueue(string_2)

    return found_binary
        
