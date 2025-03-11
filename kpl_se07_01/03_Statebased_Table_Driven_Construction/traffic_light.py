import time
from enum import Enum

# Automata state
class trafficLightstate(Enum):
    MERAH = "Merah"
    KUNING = "Kuning"
    HIJAU = "Hijau"

# Automata state transitions
state_transitions = {
    trafficLightstate.MERAH: trafficLightstate.KUNING,
    trafficLightstate.KUNING: trafficLightstate.HIJAU,
    trafficLightstate.HIJAU: trafficLightstate.MERAH
}

state_duration = {
    trafficLightstate.MERAH: 5,
    trafficLightstate.KUNING: 2,
    trafficLightstate.HIJAU: 3
}

def traffic_light():
    current_state = trafficLightstate.MERAH
    while True:
        print(f"Lampu: {current_state.value}")
        time.sleep(state_duration[current_state])
        current_state = state_transitions[current_state]

if __name__== "__main__":
    traffic_light()