# 6 Stabilizers Detect a Single Qubit Error Only

When we measure all six stabilizers in the Steane code, the measurement detects **a single error of any type** (X, Z, or Y) that occurs on a single qubit. It does **not** detect one X error and one Z error simultaneously.

Here's why and how the syndrome works:

---

## The Six Stabilizers Detect One Single-Qubit Error

The Steane code is designed to correct any single error, regardless of whether that error is a bit flip (X), a phase flip (Z), or both (Y). The six stabilizers work together to generate a unique **syndrome** (a 6-bit pattern) for every one of the 21 possible single errors (7 physical qubits $\times$ 3 error types).

### 1. How the Syndrome Pinpoints the Error

The 6-bit syndrome is naturally divided into two independent parts:

| Syndrome Group | Stabilizer Type | What it Detects | Syndrome Size |
| :--- | :--- | :--- | :--- |
| **Bit-Flip Syndrome** | $\mathbf{S_Z}$ (3 stabilizers) | Detects **X and Y** errors. | 3 bits |
| **Phase-Flip Syndrome** | $\mathbf{S_X}$ (3 stabilizers) | Detects **Z and Y** errors. | 3 bits |

The combination of the two 3-bit results gives the full 6-bit syndrome, which identifies the error perfectly:

* **Case 1: Single X Error**
    * The **$\mathbf{S_Z}$** checks fail (read -1) at a location determined by the X-error's position (e.g., "101").
    * The **$\mathbf{S_X}$** checks *all pass* (read +1, or "000") because an X error commutes with X stabilizers.
    * *Resulting Syndrome:* A pattern like "**101** 000".

* **Case 2: Single Z Error**
    * The **$\mathbf{S_Z}$** checks *all pass* (read +1, or "000") because a Z error commutes with Z stabilizers.
    * The **$\mathbf{S_X}$** checks fail (read -1) at a location determined by the Z-error's position (e.g., "110").
    * *Resulting Syndrome:* A pattern like "000 **110**".

* **Case 3: Single Y Error**
    * A Y error is equivalent to an X error and a Z error happening at the **same location**.
    * **Both** the $\mathbf{S_Z}$ checks and the $\mathbf{S_X}$ checks fail, but they both point to the *same physical qubit*.
    * *Resulting Syndrome:* A pattern like "**101** **101**".

### 2. Why it Can't Correct Two Independent Errors

The code has a minimum distance of $d=3$. This means it can detect up to $d-1=2$ errors, and it can correct up to $t = \lfloor (d-1)/2 \rfloor = 1$ error.

If you had *two* independent errors—say, an X error on Qubit 0 and a Z error on Qubit 6:

1.  The X error generates an $S_Z$ syndrome pattern ($e_X$).
2.  The Z error generates an $S_X$ syndrome pattern ($e_Z$).

The total syndrome measured would be $e_X \ e_Z$. However, this **6-bit pattern would be the same as the syndrome for some single Y error** on a different qubit. The code cannot tell the difference between a single, complex error (Y) and two distinct, simpler errors (X + Z). This is called a **syndrome collision**, and it prevents reliable correction.

**Therefore, the 6 stabilizers are necessary to isolate one specific error event out of 21 possibilities, not to handle two simultaneous, independent events.**