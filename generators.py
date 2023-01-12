# start with creating a simple generator with returns 1 to 4 and print the output

def gen1():
    yield 1
    yield 2
    yield 3
    yield 4

print (gen1())

for i in gen1():
    print(i)


def gen2(n):
    counter = 0
    while(counter<n):
        yield counter
        counter +=1

print (gen2(20))
for i in gen2(20):
    print (i)
    