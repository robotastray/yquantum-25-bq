import os
import sys
from dotenv import load_dotenv
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

from qiskit.visualization import plot_histogram, plot_state_city
import matplotlib.pyplot as plt
import bluequbit
from qiskit import QuantumCircuit

# Add src directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from bitstring.findbitstring import find_heavy_bitstring


# Load environment
load_dotenv()
P1 = "./qasm/P1_little_peak.qasm"
P2 = "./qasm/P2_swift_rise.qasm"
P3 = "./qasm/P3__sharp_peak.qasm"
P4 = "./qasm/P4_golden_mountain.qasm"
P5 = "./qasm/P5_granite_summit.qasm"
P6 = "./qasm/P6_titan_pinnacle.qasm"

# Please fill the .env with the required environmental variable such as API token.
API_TOKEN = os.getenv('API_TOKEN') # "0JWXHYYvo8GlBfZXiImW2JAutuPYFiBD"  # Replace with your BlueQubit API token
SHOTS = int(os.getenv('SHOTS')) # 1000
BOND_DIMENSION = int(os.getenv('BOND_DIMENSION')) # 16


# Change this to desired circuit
CURRENT_CIRCUITS = [P1,P2,P3,P4,P5,P6]
i = 0
# Get circuit
for CURRENT_CIRCUIT in CURRENT_CIRCUITS:
    i +=1 #index
    ###############################################################################

    if CURRENT_CIRCUIT == P1 or CURRENT_CIRCUIT == P2 or CURRENT_CIRCUIT == P3:
        result = find_heavy_bitstring(CURRENT_CIRCUIT, API_TOKEN, SHOTS, BOND_DIMENSION, i)
    else:
        print(f"For P{i} it's Work in Progress")
        pass

