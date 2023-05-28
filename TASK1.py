from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def build_oracle(string):
    num_qubits = len(string)
    oracle_circuit = QuantumCircuit(num_qubits)
    
    # Apply phase inversion to the target state
    oracle_circuit.x([i for i, bit in enumerate(reversed(string)) if bit == '1'])
    oracle_circuit.cz(0, num_qubits - 1)  # Controlled-Z gate between the first and last qubits
    oracle_circuit.x([i for i, bit in enumerate(reversed(string)) if bit == '1'])    
    
    # Convert the oracle to a gate
    oracle_gate = oracle_circuit.to_gate()
    oracle_gate.name = "Oracle"
    
    return oracle_gate

# Example usage
target_string = '01101'
oracle = build_oracle(target_string)

# Create a QuantumCircuit with the oracle
num_qubits = len(target_string)
qreg = QuantumRegister(num_qubits)
creg = ClassicalRegister(num_qubits)
circuit = QuantumCircuit(qreg, creg)
circuit.append(oracle, qreg)
circuit.measure(qreg, creg)

print(circuit)
circuit.draw()
