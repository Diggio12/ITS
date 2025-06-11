def ciclo_a() -> list[int]:
    a = []
    for i in range(2, 14+1, 2):
        a.append(i)

    print(a)

def ciclo_b() -> list[int]:
    b = []
    for i in range(1, 13 + 1, 3):
        b.append(i)

    print(b)

def ciclo_c() -> list[int]:
    c = []
    for i in range (30,  0 - 1, -5):
        c.append(i)

    print(c)

def ciclo_d() -> list[int]:
    d = []
    for i in range(5, 45 + 1, 10):
        d.append(i)

    print(d)


ciclo_a()
ciclo_b()
ciclo_c()
ciclo_d()