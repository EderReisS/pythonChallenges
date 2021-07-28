
if __name__ == '__main__':
    n = int(input("digite um numero: ").strip())

    if n % 2 != 0:
        print("Weird")
    else:
        if n in range(2, 6):
            print("Not Weird")
        elif n in range(6, 21):
            print("Weird")
        elif n >= 21:
            print("Not Weird")