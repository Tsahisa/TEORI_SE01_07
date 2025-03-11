from enum import Enum

class State(Enum):
    IDLE = "Idle"
    MENUNGGU_PRODUK = "MenungguProduk"
    MENGELUARKAN_PRODUK = "MengeluarkanProduk"
    SELESAI = "Selesai"

class VendingMachineFSM:
    def __init__(self):
        self.state = State.IDLE
        print(f"State awal: {self.state.value}")
        self.transitions = {
            State.IDLE: {"Masukkan Uang": State.MENUNGGU_PRODUK},
            State.MENUNGGU_PRODUK: {"Pilih Produk": State.MENGELUARKAN_PRODUK, "Reset": State.IDLE},
            State.MENGELUARKAN_PRODUK: {"Keluarkan Produk": State.SELESAI},
            State.SELESAI: {"Reset": State.IDLE}
        }
    
    def trigger(self, action):
        if action in self.transitions.get(self.state, {}):
            self.state = self.transitions[self.state][action]
            print(f"State berubah menjadi: {self.state.value}")
        else:
            print(f"Aksi '{action}' tidak valid dari state '{self.state.value}'")

# Contoh penggunaan
fsm = VendingMachineFSM()
fsm.trigger("Masukkan Uang")  # Idle -> MenungguProduk
fsm.trigger("Pilih Produk")   # MenungguProduk -> MengeluarkanProduk
fsm.trigger("Keluarkan Produk")  # MengeluarkanProduk -> Selesai
fsm.trigger("Reset")          # Selesai -> Idle
