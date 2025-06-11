animale:str= input("inserire un animale ")

abitat:str=input(f"inserire l' abitat dell'animale {animale} ")

Mammiferi:list=["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
Rettili:list=["serpente", "lucertola", "tartaruga", "coccodrillo"]
Uccelli:list=["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
Pesci:list= ["squalo", "trota", "salmone", "carpa"]

match animale:
    case animale if animale in Mammiferi:
        print(f"{animale} appartiene alla categoria Mammiferi")
        animal_type="Mammiferi"
    case animale if animale in Rettili:
        print(f"{animale} appartiene alla categoria Rettili")
        animal_type="Rettili"
    case animale if animale in Uccelli:
        print(f"{animale} appartiene alla categoria Uccelli")
        animal_type="Uccelli"
    case animale if animale in Pesci:
        print(f"{animale} appartiene alla categoria Pesci")
        animal_type="Pesci"
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}!")
        animal_type="unknown"

info:dict={"animale":animale, "categoria":animal_type, "abitat":abitat,}

match info:
    case info if info["abitat"]=="terra" and info["animale"] in ["cane", "gatto", "cavallo", "elefante", "leone"]:
        print(f"{animale} è un mammifero terrestre")
    case info if info["abitat"]=="terra" and info["animale"] in ["serpente, lucertola"]:
        print(f"{animale} è un rettitle terrestre")
    case info if info["abitat"]=="terra" and info["animale"] in ["gallina", "tacchino"]:
        print(f"{animale} è un uccello terrestre")
    case info if info["abitat"]=="acqua" and info["animale"] in ["balena","delfino"]:
        print(f"{animale} è un mammifero acquatico")
    case info if info["abitat"]=="acqua" and info["animale"] in ["serpente", "tartaruga", "coccodrillo"]:
        print(f"{animale} è un rettile acquatico")
    case info if info["abitat"]=="acqua" and info["animale"] in ["cigno", "anatra"]:
        print(f"{animale} è un uccello acquatico")
    case info if info["abitat"]=="acqua" and info["animale"] in Pesci:
        print("tutti i pesci vivono in acqua")
    case info if info["abitat"]=="aria" and info["animale"] in ["aquila", "pappagallo", "gufo", "falco"]:
        print(f"{animale} è un uccello che vive in aria")

    case info if info["categoria"]=="unknown":
        print(f"non so dare informazioni sull'abitat {abitat}")

    case info if info["abitat"] not in ["aria","terra","acqua"]:
        print(f"non so dare informazioni sull'abitat {abitat}")

    case info if info["abitat"]=="terra" and info["animale"] in ["balena", "tartaruga" "delfino"] or Pesci or Uccelli:
        print(f"non ho mai visto un {animale} terrestre")
    case info if info["abitat"]=="acqua" and info["animale"] in ["cane", "gatto", "cavallo", "elefante", "leone", "lucertola", "gallina", "tacchino"]:
        print(f"non ho mai visto un {animale} acquatico")
    case info if info["abitat"]=="aria" and info["animale"] in Pesci or Mammiferi or Rettili:
        print(f"non ho mai visto un {animale} volante")