from qiskit import QuantumCircuit, Aer, execute

def recursive_circuit(qc, depth):
    if depth == 0:
        # Base case: apply a single X gate
        qc.x(0)
    else:
        # Recursive case: apply a controlled recursive_circuit
        qc.h(0)
        qc.cx(0, 1)
        recursive_circuit(qc, depth - 1)
        qc.cx(0, 1)
        qc.h(0)

# Create a quantum circuit
qc = QuantumCircuit(2)

# Call the recursive_circuit function
recursive_circuit(qc, 2)

# Measure the qubits
qc.measure_all()

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1)
result = job.result()
counts = result.get_counts(qc)

print(qc)
print("Measurement outcome:", list(counts.keys())[0])
qc.draw()
