import bluequbit
from qiskit import QuantumCircuit

def find_heavy_bitstring(qasm_file, api_token, shots, bond_dimension, index):
    bq_client = bluequbit.init(api_token)
    qc = QuantumCircuit.from_qasm_file(qasm_file)
    qc.measure_all()
    device = "mps.cpu"
    options = {"mps_bond_dimension": bond_dimension}
    print(f"Submitting circuit P{index} with {shots} shots to {device}...")
    job_result = bq_client.run(qc, device=device, options=options, shots=shots)
    counts = job_result.get_counts()
    heavy_bitstring = max(counts, key=counts.get)
    print(f"P{index}_*.qasm Heavy bitstring: {heavy_bitstring} (count: {counts[heavy_bitstring]})")
    
    return heavy_bitstring