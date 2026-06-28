def ambil_data():
    return ["Apel", "Jeruk", "Mangga", "Pisang"]

def filter_data(data):
    return [buah for buah in data if buah != "Pisang"]

data_mentah = ambil_data()
data_bersih = filter_data(data_mentah)
print(data_bersih)
