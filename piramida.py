def piramida_angka(number):
    for i in range(1, number+1):
        print("  " *(number - i), end="")
        for r in range(1, i + 1):
            print(r, end=" ")
        
        for g in range(i - 1, 0 , -1):
            print(g, end=" ")
        print()
piramida_angka(3)
