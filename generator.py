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
        
gen = generator(maximum=1000)
for n in gen:
    print(n)
