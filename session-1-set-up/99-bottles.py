print("How many beers on the wall?\n")

def sing_bottles():
    bottles = 99
    while bottles > 0:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer")
        bottles -= 1
        print(f"Knock one down, pass it around, {bottles} bottles of beer on the wall.\n")

    print("No more bottles, you alcoholic 😬")

sing_bottles()
