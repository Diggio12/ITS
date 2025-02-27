x = int(input('inserire coordinate x: '))
y = int(input('inserire coordinate y: '))
coordinate:tuple = (x, y)

match coordinate:
    case (0, 0):
        print(f"Il punto {coordinate} si trova nell'origine")
    case (x, 0):
        print(f"Il punto {coordinate} si trova sull'asse X")
    case (0, y):
        print(f"Il punto {coordinate} si trova sull'asse Y")
    case coordinate if x > 0 and y > 0:
        print(f'Il punto {coordinate} è nel primo quadrante')
    case coordinate if x < 0 and y > 0:
        print(f'Il punto {coordinate} è nel secondo quadrante')
    case coordinate if x < 0 and y < 0:
        print(f'Il punto {coordinate} è nel terzo quadrante')
    case coordinate if x > 0 and y < 0:
        print(f'Il punto {coordinate} è nel quarto quadrante')