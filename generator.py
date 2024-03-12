def generator(v=0):
    yield 1
    print('Continuando...')
    yield 2
    print('Mais uma...')
    yield 3
    print('Vou terminar')
    return 'ACABOU'

gen = generator(v=0)
for pausas in gen:
    print(pausas)

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        
        if n >= maximum:
            return
        
gen = generator(maximum=100)
for n in gen:
    print(n)

def gen1():
    print("Começou Gen1")
    yield 1
    yield 2
    yield 3
    print("Acabou Gen1")

def gen2():
    print("Começou Gen2")
    yield from gen1()
    yield 4
    yield 5
    yield 6
    print("Acabou Gen2")

def gen3():
    print("Começou Gen3")
    yield 10
    yield 20
    yield 30
    print("Acabou Gen3")


g1 = gen1()
g2 = gen2()
g3 = gen3()
for pausas in g1:
    print(pausas)
for pausas in g2:
    print(pausas)
for pausas in g3:
    print(pausas)
gen = generator(maximum=1000)
for n in gen:
    print(n)
