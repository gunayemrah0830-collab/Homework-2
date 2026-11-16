from student_utils import (
    calculate_average,
    get_highest_score,
    get_lowest_score,
    proses_telebeleri,
    qeydiyyatdan_kecenler
)

scores = [78, 91, 85, 67, 95, 88]

print("Orta bal:", calculate_average(scores))

print("En yuksek bal:", get_highest_score(scores))

print("En asagi bal:", get_lowest_score(scores))


telebe_siyahisi = ["Ali", "Leyla", "Kamran", "Aysel"]

proses_telebeleri(telebe_siyahisi)


telebeler = ["Ali", "Leyla", "Kamran"]

qeydiyyatdan_kecenler(*telebeler)