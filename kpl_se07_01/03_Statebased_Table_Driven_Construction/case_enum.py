from enum import Enum

class JenisKelamin(Enum):
    LAKI_LAKI = 1
    PEREMPUAN = 1

print(JenisKelamin.Laki_Laki) ## Value of Enum => JenisKelamin.Laki_Laki
print(JenisKelamin.Laki_Laki.value) ## Value dari Laki_Laki => 1
print(JenisKelamin.Laki_Laki.name) ## Nama Enum => Laki_Laki

# Dart Programming
# enum Status {Online, Offline, Busy}