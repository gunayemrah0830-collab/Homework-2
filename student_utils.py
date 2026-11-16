#TAPŞIRIQ 1

#funksiya 1

def calculate_average(scores):
    """Balların ortalamasını hesablayır."""
    return sum(scores) / len(scores)

scores = [78,91,85,67,95,88]
print(calculate_average(scores))



#funksiya 2

def get_highest_score(scores):
    """Ən yüksək balı qaytarır."""
    return max(scores)

scores = [78,91,85,67,95,88]
print(get_highest_score(scores))



#funksiya 3

def get_lowest_score(scores):
    """Ən aşağı balı qaytarır."""
    return min(scores)
scores = [78,91,85,67,95,88]
print(get_lowest_score(scores))






#TAPŞIRIQ 2
def proses_telebeleri(telebe_siyahisi):
    """Tələbələrin adlarını və sayını göstərir."""

    print("Tələbələr:")

    for telebe in telebe_siyahisi:
        print(telebe)

    print("Tələbələrin ümumi sayı:", len(telebe_siyahisi))

telebe_siyahisi = ["Ali", "Leyla", "Kamran", "Aysel"]
print(proses_telebeleri(telebe_siyahisi))






#TAPŞIRIQ 3
def qeydiyyatdan_kecenler(*telebeler):
    """İstənilən sayda tələbəni qeydiyyata alır."""

    print("Qeydiyyatdan keçmiş tələbələr:")

    for telebe in telebeler:
        print(telebe)

    print("Cəmi:", len(telebeler))
telebeler = ["Ali", "Leyla", "Kamran", "Aysel"]
print(qeydiyyatdan_kecenler(*telebeler))
