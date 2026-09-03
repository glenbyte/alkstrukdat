def piramida_angka(number):
    for i in range(1, number+1):
        print("  " *(number - i), end="")
        for r in range(1, i + 1):
            print(r, end=" ")
        
        for g in range(i - 1, 0 , -1):
            print(g, end=" ")
        print()
print("test case = 1)")
piramida_angka(1)
print("test case = 2)")
piramida_angka(2)
print("test case = 3)")
piramida_angka(3)
print("test case = 4)")
piramida_angka(4)
print("test case = 5)")
piramida_angka(5)
print("test case = 6)")
piramida_angka(6)
print("test case = 7)")
piramida_angka(7)
print("test case = 8)")
piramida_angka(8)
print("test case = 9)")