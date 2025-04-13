import os
import sys
from dotenv import load_dotenv

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
# Define output file (overwrite mode)
output_file = "output.txt"

# Open file in write mode to clear previous content
with open(output_file, "w") as f:
    f.write("=== BlueQubit Challenge Output ===\n")
# Get circuit
for i, CURRENT_CIRCUIT in enumerate(CURRENT_CIRCUITS, start=1):
    output = f"Processing circuit P{i}: {CURRENT_CIRCUIT}\n"
    ###############################################################################
    if CURRENT_CIRCUIT in [P1, P2, P3]:
        result = find_heavy_bitstring(CURRENT_CIRCUIT, API_TOKEN, SHOTS, BOND_DIMENSION, i)
        output += f"Result: {result}\n"
    else:
        output += f"For P{i}, it's a Work in Progress\n"
        pass
    print(output, end="")  # Print to terminal
    with open(output_file, "a") as f:  # Append to file
        f.write(output)


