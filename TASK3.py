from qiskit import QuantumCircuit, Aer, execute

def build_oracle(input_string):
    n = len(input_string)
    qc = QuantumCircuit(n + 1)  # Add an ancilla qubit
    
    for i, bit in enumerate(input_string):
        if bit == '1':
            qc.cx(i, n)  # Controlled-X gate between each input qubit and the ancilla qubit
    
    return qc

# Example usage
input_string = '01101'
oracle_circuit = build_oracle(input_string)

# Count the number of gates in the circuit
gate_count = oracle_circuit.count_ops()

print(oracle_circuit)
print("Circuit size (number of gates):")
print(sum(gate_count.values()))
circuit.draw()
