input_number = int(input("Masukkan angka: "))
if input_number > 0:
    for i in range(1, input_number + 1):
        cube = i ** 3
        print(f"Angka saat ini adalah : {i} dan kubusnya adalah {cube}")
    else:
        print("Masukkan bilangan bulat positif.")