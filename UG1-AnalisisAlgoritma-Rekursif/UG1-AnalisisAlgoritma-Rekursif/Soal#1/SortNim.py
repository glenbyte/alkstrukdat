def InsertRecursive(sorted_array, current_value, current_length):
    # TODO 1: Implementasikan base case, logika komparasi pengurutan sesuai NIM, 
    # dan pemanggilan rekursi fungsi insert.
    if current_length == 0:
        return[current_value]
    
    if sorted_array[current_length -1 ] < current_value:
        return InsertRecursive(
            sorted_array, current_value, current_length - 1
        ) + [sorted_array[current_length - 1]]
    else:
        return sorted_array[:current_length] + [current_value] + sorted_array[current_length:]
    
def RecursiveFilterSort(data_array, current_length):
    # TODO 2: Implementasikan base case, pemecahan rekursif, dan filter kondisional 
    # untuk memanggil fungsi InsertRecursive sesuai paritas NIM.
    if current_length == 0:
        return[]
    nilai = data_array[current_length - 1]
    sorted_part = RecursiveFilterSort(data_array, current_length - 1)
    if nilai % 2 == 0:
        return InsertRecursive(sorted_part, nilai, len(sorted_part))
    else:
        return sorted_part
# Ganti Dengan NIM Anda
# Contoh, NIM_MAHASISWA = "71230994" -> nanti outputnya [4, 2, 0] 
NIM_MAHASISWA = "71251190"

if NIM_MAHASISWA != "":
    raw_data = [int(digit) for digit in NIM_MAHASISWA]
    data_length = len(raw_data)
    
    final_result = RecursiveFilterSort(raw_data, data_length)

    # TODO 3: cetak hasil akhir sesuai format yang diminta.
    digit_terakhir = int(NIM_MAHASISWA[-1])
    if digit_terakhir % 2 != 0:
        print("Digit terakhir NIM GANJIL → Filter angka GANJIL, urut ASCENDING")
    else:
        print("Digit terakhir NIM GENAP → Filter angka GENAP, urut DESCENDING")
    print(f"NIM     : {NIM_MAHASISWA}")
    print(f"Array awal : {raw_data}")
    print(f"Hasil akhir: {final_result}")