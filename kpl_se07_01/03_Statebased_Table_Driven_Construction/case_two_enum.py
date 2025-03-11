from enum import Enum

class JenisKelamin(Enum):
    PRIA = 1
    WANITA = 2

patients = []

def add_patient(name: str, gender: JenisKelamin):
    if not isinstance(gender, int):
        raise ValueError("Jenis Kelamin Harunya adalah Pria atau Wanita")
    patients.append({"name": name, "gender": gender.name})

add_patient("Andi", JenisKelamin.Pria)
add_patient("Siti", JenisKelamin.Wanita)
add_patient("Felina", "Transgender")

for patient in patients:
    print(f"{patient['name']} adalah {patient['gender'].name}")