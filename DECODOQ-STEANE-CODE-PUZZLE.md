# **Decodok-Q: Steane Code Puzzle ("Syndrome Shifter")**

This document outlines the design and mechanics for a puzzle game based on the quantum error correction (QEC) structure of the Steane code, denoted as \[\[7, 1, 3\]\].

## **1\. Code Foundation: Steane \[\[7, 1, 3\]\]**

The Steane code uses 7 physical qubits to protect 1 logical qubit and is capable of correcting any single-qubit error (X, Y, or Z). The game is a **decoding puzzle** where the player must identify and correct a hidden single error based on the resulting syndrome.

The code's structure is defined by the geometry of the Fano Plane. This geometric structure, which consists of 7 points (qubits) and 7 lines (sets of checks), underlies the definition of the stabilizers.

## **2\. Game Setup: The Register and Checks**

The game board consists of two main areas: the Physical Register and the Stabilizer Readouts.

### **A. The Physical Register (7 Qubits)**

* **Elements:** Seven circles/shapes representing the physical qubits (Q0 to Q6).  
* **Arrangement:** The qubits are kept in a fixed, neutral arrangement (e.g., a simple column). Their proximity does not mathematically affect the code's definition but is important for stable visualization.  
* **State:** Each qubit carries a hidden error state ('I', 'X', 'Y', or 'Z').

### **B. The Stabilizer Readouts (6 Checks)**

The Steane code is defined by 6 independent stabilizer generators, grouped by the type of error they detect:

* **3 Z-Stabilizers (**$S\_Z$**):** Detect X and Y errors (bit flips). They follow the mathematical structure of a classical Hamming (7,4) code.  
  * $S\_{Z1} \= Z\_0 Z\_2 Z\_4 Z\_6$ (Example based on a common basis)  
* **3 X-Stabilizers (**$S\_X$**):** Detect Z and Y errors (phase flips). They mirror the structure of the Z-stabilizers.  
  * $S\_{X1} \= X\_0 X\_2 X\_4 X\_6$ (Example based on a common basis)

**Syndrome Display:** Each stabilizer has a readout indicating its measurement outcome:

* **\+1 (Green/Satisfied):** The check passes; no error detected by this stabilizer.  
* **\-1 (Red/Violated):** The check fails; a syndrome event has occurred, indicating an error is present within the qubits measured by this stabilizer.

## **3\. Core Gameplay Loop**

1. **Error Injection (Puzzle Setup):** The game randomly injects exactly **one** Pauli error ('X', 'Y', or 'Z') onto one of the 7 qubits (Q0-Q6).  
2. **Syndrome Presentation (Hint):** The 6 stabilizer readouts immediately update, presenting the player with the 6-bit syndrome pattern of \+1s and \-1s.  
3. **Player Action (Decoding):** The player must analyze the syndrome and deduce:  
   * The location of the error (Q0-Q6).  
   * The type of the error (X, Y, or Z).  
4. **Correction:** The player inputs a correction operation (a 7-qubit Pauli string, e.g., "IYIIIII" to correct a Y error on Q1).  
5. **Feedback:** The game applies the correction to the hidden error state and updates the 6 stabilizer readouts instantly.  
6. **Winning Condition:** The player wins when all 6 stabilizer readouts are \+1 (zero syndrome).

## **4\. Player Interaction and Visualization**

### **A. Stabilizer Probing (The "Joystick")**

The player can select any of the six stabilizer readouts to "probe" it. This triggers a visualization that helps break down the Fano Plane geometry:

* **Visual Feedback:** Animated lines connect the selected stabilizer to the exact 4 qubits it measures.  
* **Dynamic Focus:** The connecting lines pulse or glow brightly, showing the "line" geometry on the fixed qubit register without causing the registers to move. This maintains UI stability while providing geometric clues.

### **B. Pattern Matching**

The puzzle relies on the player learning the 6 unique 6-bit syndrome patterns that correspond to the 7 possible locations for each of the 3 error types (21 total correctable syndromes).

* **X-error:** Only flips the Z-stabilizer group ($S\_Z$).  
* **Z-error:** Only flips the X-stabilizer group ($S\_X$).  
* **Y-error:** Flips both the Z- and X-stabilizer groups.

## **5\. Engine Architecture**

The game utilizes a modular Python framework (QEC\_Framework.py) with dedicated classes for QubitRegister and Stabilizer, allowing for easy extension to other QEC codes like the Surface Code.