
def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b

counter = 0
for item in lucas():
    if counter == 50:
        break
    print (item)
    counter = counter + 1


lu_se = lucas()
print (dir(lu_se))
