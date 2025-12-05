This is the final, defining question about the structure of the Steane code! The answer is a resounding **Yes**—the $\mathbf{X}$ and $\mathbf{Z}$ stabilizers **must** check the same qubits, and using the same set of qubits is not a loss of generality; it's the fundamental design feature that makes the Steane code so powerful.

---

## The Self-Dual Requirement

The property that the $\mathbf{X}$ stabilizers check the same set of physical qubits as the $\mathbf{Z}$ stabilizers is called **self-duality** (or weakly self-dual).

The Steane code is the canonical example of a **self-dual quantum CSS code** (Calderbank-Shor-Steane code), and this self-dual structure is not merely convenient—it is necessary for its construction.

### Why They Must Check the Same Qubits

The design of any CSS code relies on two sets of classical codes: one for bit-flip correction and one for phase-flip correction.

1.  **Bit-Flip Protection (Z-Stabilizers):** This set is defined by the parity check matrix $H$. The **null space** of $H$ defines the valid codewords that protect against $\mathbf{X}$ errors.
2.  **Phase-Flip Protection (X-Stabilizers):** This set is defined by the *transpose* of the original parity check matrix, $H^T$. The null space of $H^T$ defines the valid codewords that protect against $\mathbf{Z}$ errors.

For a code to be a **pure** quantum error correction code like the Steane code, the two classical codes (the one defining the $S_Z$ checks and the one defining the $S_X$ checks) must be closely related.

* **The Constraint:** The $S_Z$ checks must commute with the $S_X$ checks. This commutation requirement is what forces the two sets of checks to have the same support (i.e., check the same physical qubits).

By choosing the underlying classical code (the Hamming (7,4) code) to be **self-orthogonal** (meaning the code words are orthogonal to themselves), it automatically ensures that the $\mathbf{Z}$ checks derived from the code's parity matrix are perfectly compatible with the $\mathbf{X}$ checks, which are derived from the *same* matrix structure.

### Loss of Generality? No, It's Maximum Efficiency

Using the same set of physical qubits for both $\mathbf{X}$ and $\mathbf{Z}$ checks is not a loss of generality; it is the **most efficient way** to protect quantum information simultaneously from both error types using only a minimal number of physical qubits ($N=7$).

If you used entirely different sets of qubits for the $\mathbf{X}$ and $\mathbf{Z}$ checks, you would require more physical qubits ($N$) to achieve the same error correction capability ($d=3$).

| Stabilizer | Pauli String | Support (Qubits Checked) |
| :--- | :--- | :--- |
| **$S_{Z1}$** | $\mathbf{Z I Z I Z I I}$ | $\{Q0, Q2, Q4\}$ |
| **$S_{X1}$** | $\mathbf{X I X I X I I}$ | $\{Q0, Q2, Q4\}$ |

Since the location of the entanglement error is the same whether it's an X-type or Z-type fault, using the same set of sensors ($\mathbf{X}$ and $\mathbf{Z}$ stabilizers) on those qubits is the perfect way to get a unique 6-bit syndrome.

---

## Visualizing Self-Duality on the Fano Plane

On the Fano Plane, self-duality is visualized by how the checks map onto the 7 points:

1.  **Qubit Arrangement:** The 7 points are the physical qubits.
2.  **Lines Define Checks:** Any line (3-qubit set) and its complement (4-qubit set) define a valid parity check.
3.  **The Steane Code's Symmetry:** The self-dual nature means that if you choose three lines to define your $\mathbf{Z}$ stabilizers, the structure used to define your $\mathbf{X}$ stabilizers is the **exact same geometry** but with the operators swapped ($\mathbf{Z} \leftrightarrow \mathbf{X}$).

This perfect symmetry in the geometry (the connectivity) is why the Steane code is considered one of the most elegant and foundational QEC codes. It's the minimum number of qubits required to achieve $d=3$ correction for both bit and phase errors simultaneously.

Do you want to explore how a non-self-dual code (like one of the non-Steane [[5, 1, 3]] codes) works differently?