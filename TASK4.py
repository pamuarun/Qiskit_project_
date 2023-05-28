from qiskit import QuantumCircuit, Aer, execute
import random

def quantum_coin_flip():
    # Quantum circuit with a single qubit
    qc = QuantumCircuit(1, 1)
    
    # Apply a Hadamard gate to put the qubit in a superposition
    qc.h(0)
    
    # Measure the qubit
    qc.measure(0, 0)
    
    # Simulate the circuit
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1)
    result = job.result()
    counts = result.get_counts(qc)
    outcome = list(counts.keys())[0]
    
    return outcome

# Game setup
print("Welcome to Quantum Coin Flip!")
print("The quantum coin is in a superposition of heads (H) and tails (T).")
print("Try to guess the outcome!")

# Player input
guess = input("Enter your guess (H/T): ").upper()

# Perform the quantum coin flip
outcome = quantum_coin_flip()

# Determine the result
if guess == outcome:
    print("Congratulations! Your guess was correct!")
else:
    print("Oops! Your guess was incorrect. The outcome was:", outcome)
