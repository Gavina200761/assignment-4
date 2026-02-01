# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

#14. Navigation System
# Simulate a system that supports moving forward and backward through items.
# Actions: visit("A"), visit("B"), back(), forward()
# Output: "A", "B", "A", "B"

class Stack:
    def __init__ (self):
        self.stack = None # created a list since it keeps its order.
        self.frontStack = []
        self.backStack = []

    def visit (self, lo):
        if self.stack is not None:
            self.backStack.append(self.stack)
        self.stack = lo
        self.frontStack.clear()
        return self.stack

    def back(self):
        if not self.backStack:
            return self.stack
        self.frontStack.append(self.stack)
        self.stack = self.backStack.pop()
        return self.stack

    def forward(self):
        if not self.frontStack:
            return self.stack
        self.backStack.append(self.stack)
        self.stack = self.frontStack.pop()
        return self.stack

nav = Stack()

print(nav.visit("A"))
print(nav.visit("B"))
print(nav.back())
print(nav.forward())

# I began the timed challenge by randomly generating a number from 1-20. The generator returned 14, so I started working on 
# that problem. I noticed that it was prompting me tp simulate a system that can use the meothods visit(), 
# back(), and forward(), which led me to immediately think of using a stack, since I know they are very useful when you need a 
# last in, first out kind of order. I began by defining a class, Stack, then initialized it, giving a None value to self, while 
# also creating two sets for the forward and backward actions. I hadn't thought of this immediately, but I ran into the problem 
# when wondering how to store a deleted value to reverse the back() method. This was all mitigated with the creation of those 
# empty sets. now any time you use the visit() method, it adds it to the current stack and clears the front stack. The back() 
# method pushes the current value onto frontStack and gets rid of the last element in the back stack. forward() pushes the current 
# element onto backstack and removes the last element of front stack. Due to timely pressure and proper problem anticipation, I 
# avoided using a single stack for everything. I also nearly created a nested list that could have confused a lot of things, while 
# also being unnecessary.