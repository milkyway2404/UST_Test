def program2():
    class CircularQueue():

        # constructor
        def __init__(self, size): # initializing the class
            self.size = size

            # initializing queue
            self.queue = [None for i in range(size)]
            self.front = self.rear = -1

        def enqueue(self, data):
            # condition if queue is full
            if ((self.rear + 1) % self.size == self.front):
                print(" Queue is Full\n")
            # condition for empty queue
            elif (self.front == -1):
                self.front = 0
                self.rear = 0
                self.queue[self.rear] = data
            else:
                # next position of rear
                self.rear = (self.rear + 1) % self.size
                self.queue[self.rear] = data

        def dequeue(self):
            if (self.front == -1): # condition for empty queue
                print ("Queue is Empty\n")
            # condition for only one element
            elif (self.front == self.rear):
                temp = self.queue[self.front]
                self.front = -1
                self.rear = -1
                return temp
            else:
                temp = self.queue[self.front]
                self.front = (self.front + 1) % self.size
                return temp

        def display(self):
            # condition for empty queue
            if(self.front == -1):
                print ("Queue is Empty")

            elif (self.rear >= self.front):
                print("Elements in the circular queue are:",
                                                  end = " ")
                for i in range(self.front, self.rear + 1):
                    print(self.queue[i], end = " ")
                print ()

            else:
                print ("Elements in Circular Queue are:",
                                               end = " ")
                for i in range(self.front, self.size):
                    print(self.queue[i], end = " ")
                for i in range(0, self.rear + 1):
                    print(self.queue[i], end = " ")
                print ()

            if ((self.rear + 1) % self.size == self.front):
                print("Queue is Full")

    # Driver Code
    queue_dict = {0: 10, 1: 25, 2: 56, 3: 70, 4: 85}

    size = len(queue_dict.keys())

    ob = CircularQueue(size)
    ob.enqueue(queue_dict.get(0))
    ob.enqueue(queue_dict.get(1))
    ob.enqueue(queue_dict.get(2))
    ob.enqueue(queue_dict.get(3))
    ob.enqueue(queue_dict.get(4))
    ob.enqueue(queue_dict.get(5))
    ob.display()
    queue_dict[5] = 44
    print ("Deleted value = ", ob.dequeue())
    print ("Deleted value = ", ob.dequeue())
    ob.display()
    ob.enqueue(queue_dict.get(5))
    ob.display()
