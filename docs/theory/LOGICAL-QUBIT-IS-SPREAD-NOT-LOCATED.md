# **The logical qubit is spread across all 7 physical qubits.**

The specific $H$ matrix you provided defines the null space (the set of valid codewords) for the classical Hamming (7,4) code. However, when we use this matrix to define the **Steane code** ($\text{[[7, 1, 3]]}$), the interpretation changes completely.

Here is a breakdown of the difference:

---

## 1. Classical Hamming (7,4): Encoding 4 Independent Bits

In the classical case, the $H$ matrix is used to define which 3 bits are parity checks and which 4 bits are data:

* **Logical Bits:** Four of the physical positions are chosen to hold the actual data bits ($d_1, d_2, d_3, d_4$). These are the **information-carrying qubits/bits**.
* **Parity Bits:** The remaining three positions hold the calculated redundancy bits ($p_1, p_2, p_3$).
* **Decoupling:** You can mathematically isolate the four data bits, read them, and the data is preserved.

The classical code explicitly defines a clear path between the 4 logical bits and the 4 physical positions that hold them.

---

## 2. Quantum Steane Code ($\text{[[7, 1, 3]]}$): Spreading 1 Entangled Qubit

For a quantum error correcting code, the goal is to protect a superposition ($\alpha|0\rangle + \beta|1\rangle$) without disturbing it. Because of the No-Cloning Theorem and the fragility of quantum states, you cannot simply assign the logical qubit to a physical position.

Instead, the single **logical qubit** ($K=1$) is encoded into a massively entangled state spread across all 7 physical qubits. The code space is spanned by two basis states, $|0_L\rangle$ and $|1_L\rangle$:

$$
|\psi_L\rangle = \alpha|0_L\rangle + \beta|1_L\rangle
$$

The logical states $|0_L\rangle$ and $|1_L\rangle$ are highly complex entangled superpositions of the 7 physical qubits, such as:

$$
|0_L\rangle = \frac{1}{\sqrt{8}}\sum_{x \in C_{0}} |x\rangle \quad (\text{Sum over all codewords } x \text{ with even parity})
$$


### Why the Logical Qubit Spreads

1.  **Entanglement is the Key:** The logical qubit doesn't exist at any single physical location. It exists *only* in the correlations (entanglement) between the 7 physical qubits.
2.  **Symmetry for Protection:** By spreading the information across all 7 qubits symmetrically, a single error (e.g., Q3 flips) only corrupts a small part of the correlation, allowing the remaining entanglement structure to preserve the information.
3.  **Measurement Constraint:** The six **stabilizers** ($S_X$ and $S_Z$) derived from the $H$ matrix structure are now measured to find the **syndrome** (the error location) without ever touching or collapsing the protected $\alpha$ and $\beta$ coefficients of the logical state.

**In summary, the transition from classical to quantum makes the information intangible.** It moves from occupying specific physical registers to being defined by the *relationships* (entanglement) between all 7 physical registers.

This means that every single physical qubit in the Steane code is essential to maintaining the integrity of the single logical qubit.