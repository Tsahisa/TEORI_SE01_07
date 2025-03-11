from enum import Enum

class studentStatusState(Enum):
    TERDAFTAR = "Terdaftar"
    CUTI = "Cuti"
    AKTIF = "Aktif"
    LULUS = "Lulus"

# Trigger input
class TriggerInputState(Enum):
    CETAK_KSM = "Cetak KSM"
    MENYELESAIKAN_CUTI = "Cuti telah berahir"
    MENGAJUKAN_CUTI = "Waktu untuk cuti"
    LULUS = "Lulus"

# Transition
state_transitions = {
    studentStatusState.TERDAFTAR: {
        TriggerInputState.CETAK_KSM: studentStatusState.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI: studentStatusState.CUTI
    },
    studentStatusState.CUTI: {
        TriggerInputState.MENYELESAIKAN_CUTI: studentStatusState.TERDAFTAR
    },
    studentStatusState.AKTIF: {
        TriggerInputState.LULUS: studentStatusState.LULUS,
        TriggerInputState.MENGAJUKAN_CUTI: studentStatusState.CUTI
    },
}

def change_state(current_state, trigger_input):
    cond_1 = current_state in state_transitions # Return True or False
    cond_2 = trigger_input in state_transitions [current_state] # Return True or False
    if cond_1 and cond_2:
        # TERDAFTAR, AKTIF, LULUS, CUTI
        return state_transitions[current_state][trigger_input]
    return "Transisi Tidak Valid"


current_state = studentStatusState.TERDAFTAR
trigger_input = TriggerInputState.LULUS

next_state = change_state(current_state, trigger_input)
print(next_state)