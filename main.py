
def cm_inch():
    print("-"*10)
    print("Wzór:\n1 centymetr: 1cm\n1 cal: 1in")
    var = input('Podaj wartosc: ')
    var_set = var[-2:]
    try:
        var_nbr = float(var[:-2])
    except:
        result = "Nieprawidlowa wartosc"
    else:
        if var_set == 'cm':
            result = round((var_nbr * 0.394), 3)
            result = str(result) + " in"
        elif var_set == 'in':
            result = round((var_nbr * 2.45), 3)
            result = str(result) + " cm"
        else:
            result = "Nieznana miara, podaj wartosc wg wzoru"
    return print(result)

def menu():
    print("1. Obliczanie cal - centymetr\n2. Obliczanie przekatnej prostokonta")
    set_menu = input("Wybierz opcje: ")
    if set_menu == '1':
        cm_inch()
    elif set_menu == '2':
        a = int(input("Podaj bok a: "))
        b = int(input("Podaj bok b: "))
        print((a+b)**(1/2))
    else:
        menu()

if __name__ == "__main__":
    menu()
