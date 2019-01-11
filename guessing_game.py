secret = 10
for x in range(5):
    guess = int(input("Ugani skrito stevilko med 0 in 30"))
    if secret == guess:
        print("cestitam ugotovili ste stevilo!")
        print(x)
        break
    elif secret > guess:
        print("Poskusi vecje stevilo")
        print(x)
    elif secret < guess:
        print("Poskusi manjse stevilo")
        print(x)
    else:
        print("vnesi veljavno stevilo")