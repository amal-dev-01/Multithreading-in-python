from threading import Thread

class A(Thread):
    def run(self):
        for i in range(26):
            print(i, end=" ")

class B(Thread):
    def run(self):
        for i in range(26, 51):
            print(i, end=" ")

a = A()
a.start()
b = B()
b.start()

