# The logical qubit is encoded equally across all 7 physical qubits, but the stabilizer measurements are what reveal the code's structure.

The logical qubit is encoded **equally** across all 7 physical qubits, but the stabilizer measurements are what reveal the code's structure.

Here is the breakdown of why the protection is equal, but the stabilizer checks appear to have "holes."

---

## 1. The Principle of Equal Protection

The single logical qubit ($K=1$) in the $\text{[[7, 1, 3]]}$ Steane code is encoded by making all 7 physical qubits highly **entangled**. The logical state is a superposition of codewords (sets of 7-bit strings) in the code space.

$$
|\psi_L\rangle = \alpha|0_L\rangle + \beta|1_L\rangle
$$

* **Symmetry is Key:** For the code to have an error-correcting distance of $d=3$ (meaning it can correct any *single* error), the logical information **must be distributed symmetrically** across all 7 qubits. If Qubit 3 held more information than Qubit 0, an error on Qubit 3 would be more destructive, breaking the code's ability to reliably correct any single error.
* **The Weight of Logical Operators:** The smallest (lowest weight) operator that can change the logical state ($\mathbf{X}_L$ or $\mathbf{Z}_L$) without violating any stabilizer must involve at least **three** physical qubits. This minimum weight of 3 applies equally to all 7 physical qubits. This is the definition of the code distance $d=3$.

**Conclusion:** The quantum information is equally and symmetrically protected by the entire 7-qubit system. No single qubit is more or less important to the protected state.

## 2. Stabilizer Checks and Sparsity

The stabilizer generators are simply the **tools** we use to measure the health of the entanglement. They don't reflect the distribution of the protected information, but rather the minimal set of checks needed to detect all 21 possible single-qubit errors (7 locations $\times$ 3 error types).

### Why the 'I' Operators Exist

The 'I' (Identity) operator in the stabilizer string (e.g., $S_{Z1} = \mathbf{Z I Z I Z I I}$) means the stabilizer measurement **does not touch** the physical qubit at that position.

| Stabilizer | Pauli String | Qubits Checked | Qubits Ignored ('I') |
| :--- | :--- | :--- | :--- |
| **$S_{Z1}$** | $\mathbf{Z I Z I Z I I}$ | Q0, Q2, Q4 | Q1, Q3, Q5, Q6 |

The stabilizers are sparse (contain many 'I' operators) because we only need a specific **subset** of qubits for each check to generate the unique 3-bit syndrome.

If $S_{Z1}$ measured all 7 qubits, its result would be less informative because it wouldn't help localize the error to a smaller group of qubits. The sparse nature ensures that:

1.  **Locality:** The resulting syndrome pattern can uniquely identify the location of the error.
2.  **Commutation:** All six stabilizer generators must commute with each other to be measured simultaneously without collapsing the logical state. This requirement imposes constraints on which operators can be used, often leading to sparse definitions.

---

## Analogy: A Diamond in a Vault

Imagine the logical qubit is a valuable **diamond** hidden inside a **vault** with seven separate locks (the 7 physical qubits).

* **Equal Protection:** The diamond is equally protected by all 7 locks. If any one lock is faulty, the diamond is still safe (correctable).
* **Stabilizers are Sensors:** The 6 stabilizer measurements are like different **motion sensors** placed inside the vault.
    * Sensor 1 might check locks 1, 3, and 5.
    * Sensor 2 might check locks 2, 3, and 6.
* **Sparsity:** The sensors don't check every lock because we need a **unique pattern** of tripped sensors to figure out *exactly which single lock* was tampered with.

If the diamond were only protected by the locks explicitly mentioned in the sensor definitions, the vault would be easily breached by tampering with the unmonitored locks!