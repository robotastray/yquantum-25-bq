import os
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_state_city
import matplotlib.pyplot as plt

P1 = "../qasm/P1_little_peak.qasm"
P2 = "../qasm/P2_swift_rise.qasm"
P3 = "../qasm/P3__sharp_peak.qasm"
P4 = "../qasm/P4_golden_mountain.qasm"
P5 = "../qasm/P5_granite_summit.qasm"
P6 = "../qasm/P6_titan_pinnacle.qasm"

# Change this to desired circuit
CURRENT_CIRCUIT = P2

# Get circuit
file_path = os.path.join(os.path.dirname(__file__), CURRENT_CIRCUIT)
circ = QuantumCircuit.from_qasm_file(file_path)
circ.measure_all()

circ.draw('mpl')

###############################################################################


# Transpile
simulator = AerSimulator()
circ = transpile(circ, simulator)

# Run
result = simulator.run(circ).result()
counts = result.get_counts(circ)

# plot_histogram(counts, title='circuit counts')

# Sort by number of counts
sorted_probs = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

# Print the top 10 most probable bitstrings
top_10 = list(sorted_probs.items())[:10]
for bitstring, prob in top_10:
    print(f"{bitstring}: {prob}")
