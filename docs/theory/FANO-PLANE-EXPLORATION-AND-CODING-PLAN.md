
# **Geometric Modeling and Dynamic Visualization of Finite Projective Geometry for Error Correction Codes**

## **I. The Algebraic Incarnation: PG(2, 2\) over $\mathbb{F}_2^3$**

The Fano plane, formally denoted $\text{PG}(2, 2)$, stands as the foundational example of a finite projective geometry and serves as the structural basis for several fundamental error correction codes, including the Hamming (7,4) code. To establish a robust computational model, it is necessary to utilize its algebraic construction over the finite field with two elements, $\mathbb{F}_2$.

### **I.1. Finite Projective Geometry Fundamentals and Incidence Structure**

The Fano plane is fundamentally characterized as the smallest possible finite projective plane, comprising seven points and seven lines.1 Combinatorially, it is defined as a unique $(7_3)$-configuration: a set of $n=7$ points and $n=7$ lines such that every line contains exactly three points, and every point is incident with exactly three lines.2 This minimal and unique structure guarantees that two key axioms of projective geometry are satisfied: any two distinct points lie on exactly one line, and, crucially for geometric structure, any two distinct lines intersect at exactly one point, implying the absence of parallel lines.3

The Fano plane possesses a profound combinatorial perfection. It is isomorphic to a Steiner triple system, specifically $S(2, 3, 7)$.5 In the context of Steiner systems, the set of points is the 7-element set $S$, and the blocks are the 7 lines (k-element subsets) such that every pair of points ($t=2$) is contained in exactly one line ($\lambda=1$).5 This perfect arrangement, where the minimum number of checks is required to uniquely relate all pairs of points, provides the necessary geometric underpinning for constructing a linear code that is also perfect—the Hamming (7,4) code.6

The construction of $\text{PG}(2, 2)$ over $\mathbb{F}_2$ immediately classifies it as a Desarguesian plane.1 This property confirms that the geometry originates from linear algebra over a field. Although the plane is too small to contain a non-degenerate Desargues configuration, its algebraic origin ensures that all geometric relationships, such as incidence and collinearity, can be precisely modeled using vector operations and matrix arithmetic over $\mathbb{F}_2$ (modulo 2 addition).1

### **I.2. Vector Space Representation and Point/Line Mapping**

The computational implementation of the Fano plane is based on the 3-dimensional vector space over $\mathbb{F}_2$, denoted $\mathbb{F}_2^3$. This space contains $2^3 = 8$ vectors. Projective geometry dictates that points correspond to 1-dimensional subspaces. Since $\mathbb{F}_2$ has only two elements, each 1-dimensional subspace is uniquely defined by a single non-zero vector, giving $2^3 - 1 = 7$ distinct points.7

The seven points of $\text{PG}(2, 2)$ are thus labeled using the seven non-zero ordered triples of binary digits: $\{001, 010, 011, 100, 101, 110, 111\}$.7 These vectors form the core data structure for the proposed code examples.

The lines of the Fano plane are derived from the 2-dimensional subspaces of $\mathbb{F}_2^3$. Geometrically, three points $p, q, r \in \mathbb{F}_2^3$ are collinear if and only if their vector sum is zero: $p+q+r = 0 \pmod 2$.7 This algebraic closure property translates the abstract incidence structure into an implementable rule of linear dependence.

The relationship between linear dependence and coding theory is immediate. The geometric condition $p+q+r=0$ defines a set of linearly dependent points. In the context of error correction, a valid codeword $c$ must be orthogonal to the rows of the parity-check matrix $H$, such that $H c^T = 0$. If a codeword $c$ has '1's only at the indices corresponding to a collinear set of points, the matrix multiplication $H c^T$ sums these column vectors (points) modulo 2\. If the points form a line, their sum is zero, confirming that the line itself corresponds to a valid codeword in the dual code. Therefore, the linear dependence required for geometric collinearity is the exact mathematical prerequisite for defining a linear block code, establishing a causal and profound link between the Fano geometry and linear error correction structures.

### **I.3. Computational Model: The Fano Incidence Matrix $H$**

The cornerstone of the computational model is the Fano incidence matrix, $H$, which serves as the parity-check matrix for the Hamming (7,4) code. This matrix is constructed by defining its columns to be the seven non-zero vectors of $\mathbb{F}_2^3$, typically ordered by their corresponding decimal value (1 to 7).

Table I details the correspondence between the vector labels (P1 through P7) and the columns of the canonical $3 \times 7$ parity check matrix $H$. The rows of $H$ (labeled $\ell_1, \ell_2, \ell_3$) represent three independent parity checks.

Table I. Canonical Fano Incidence Matrix $H$ (Parity Check for Hamming (7,4))

|  | P1 (001) | P2 (010) | P3 (011) | P4 (100) | P5 (101) | P6 (110) | P7 (111) | Fano Line Support (Indices) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| $\ell_1$ (Check 1\) | 1 | 0 | 0 | 1 | 0 | 1 | 1 | {1, 4, 6, 7} |
| $\ell_2$ (Check 2\) | 0 | 1 | 0 | 1 | 1 | 0 | 1 | {2, 4, 5, 7} |
| $\ell_3$ (Check 3\) | 0 | 0 | 1 | 0 | 1 | 1 | 1 | {3, 5, 6, 7} |

The implementation of the Fano plane geometry requires constructing this matrix $H$ (typically using an array structure, such as NumPy in Python) and defining modulo 2 arithmetic for all vector and matrix manipulations. The '1' entries in a row $\ell_i$ indicate the set of indices of the four points incident with that particular parity check. This specific representation of $H$ is consistent with the definition of the Hamming code.9

## **II. Computational Visualization and Symmetry (Animation Precursor)**

The visualization of the Fano plane must resolve the inherent conflict between its abstract, highly symmetric algebraic structure and its necessary representation in the Euclidean plane ($\mathbb{R}^2$), where one line must be curved.1 The animation plan requires a coordinate basis and a method to dynamically demonstrate the geometry's deep symmetry.

### **II.1. Establishing Euclidean Coordinates for the Standard Model**

The standard visualization model draws the Fano plane points corresponding to the vertices, midpoints, and centroid of an equilateral triangle.1 These Euclidean coordinates, while sacrificing the visual straightness of all seven lines, provide a fixed geometric template for the animation.

A key step in the code example plan involves linking the algebraic vector indices (P1-P7) to specific Euclidean coordinates. Assuming an equilateral triangle centered at the origin with scale $R$:

Table II. Fano Vector to Euclidean Coordinate Mapping

| Index i | Vector vi​∈F23​ | Euclidean Role | Euclidean Coordinates (x,y) |
| :---- | :---- | :---- | :---- |
| P7 | 111 | Center (Centroid) | $(0.0, 0.0)$ |
| P4 | 100 | Vertex V1 | $(R, 0)$ |
| P6 | 110 | Vertex V2 | $(-R/2, R\sqrt{3}/2)$ |
| P5 | 101 | Vertex V3 | $(-R/2, -R\sqrt{3}/2)$ |
| P1 | 001 | Midpoint M1 | $(R/2, -R\sqrt{3}/6)$ |
| P2 | 010 | Midpoint M2 | $(-R/2, R\sqrt{3}/6)$ |
| P3 | 011 | Midpoint M3 (Circle Intersection) | $(0, R\sqrt{3}/3)$ |

The seven lines are visualized as the three straight edges, the three straight altitude lines (or symmetry axes), and the one circular line passing through the midpoints {P1, P2, P3}.1

### **II.2. The Automorphism Group $\text{PGL}(3, 2)$ and Dynamic Symmetry**

The abstract Fano plane is highly symmetric, acting transitively on its points and lines, meaning any point is indistinguishable from any other point, and any line is indistinguishable from any other line.1 The group of symmetries (automorphisms) is the projective general linear group $\text{PGL}(3, 2)$, which is isomorphic to the general linear group $\text{GL}(3, 2)$ over $\mathbb{F}_2$, and also to $\text{PSL}(2, 7)$.11 This group has a remarkably large order of $168$ ($2^3 \times 3 \times 7$).1

The code example must implement the generation and application of $3 \times 3$ matrices $A$ over $\mathbb{F}_2$. When applied to a point vector $v_i$, the transformation $v_i' = A v_i \pmod 2$ yields a new point vector $v_i'$. Since the operation is linear, it preserves collinearity, thereby defining an automorphism (a symmetry) of the Fano plane.

The central challenge in animating this geometry is overcoming the visual bias introduced by the Euclidean representation, where points like the centroid (P7) appear structurally unique, violating the fundamental transitivity property.14 Simply transforming the Euclidean coordinates affinely would maintain this bias.

The solution requires implementing a dynamic re-mapping technique based on the algebraic transformation:

1. A $3 \times 3$ matrix $A \in \text{GL}(3, 2)$ is selected (e.g., a generator for the group).  
2. $A$ is applied to the 7 abstract vector labels $v_i$, generating a permutation $\pi$ of the indices $\{1, \ldots, 7\}$.  
3. For the animation rendering, the plotting routine must use the permutation $\pi$ to assign the fixed Euclidean coordinates (Table II) to the permuted labels. For example, if the automorphism $A$ maps P7 (the centroid vector) to P4 (a vertex vector), the visualization must dynamically update so that the point now labeled P4 visually resides at the centroid location $(0, 0)$, while the point labeled P7 moves to the original location of P4.

This process ensures that the animation is mathematically faithful, demonstrating that the apparent geometric distinction between points and lines in the visualization is merely an artifact of the projection, and that the abstract incidence structure remains completely uniform under the action of the $PGL(3, 2)$ group. This dynamic permutation is a prerequisite for a sophisticated and educational animation.

## **III. Classical Coding Theory: The Hamming (7, 4\) Code**

The Fano plane structure is inextricably linked to the Hamming (7,4) code, $$, which adds three parity bits to four data bits to achieve single-error correction ($d=3$).6 The geometry provides a powerful visual framework for understanding the code's error detection and correction capabilities.

### **III.1. Geometric Code Definition and Encoding Implementation**

The Hamming (7,4) code $C$ is defined by the parity-check matrix $H$ (Table I). A 7-bit vector $c$ is a valid codeword if and only if $H c^T = 0 \pmod 2$. The code has $2^4 = 16$ codewords, derived from the 4 message bits.

The first code example in this module must implement the encoding function. The generator matrix $G$ is derived from the systematic form of $H$. If $H = \[A | I_3\]$, where $I_3$ is the $3 \times 3$ identity matrix (the columns P1, P2, P4 in $H$), then $G =$. The encoding is computed as $c = d G$, where $d$ is the 4-bit data vector.

In the geometric context, the set of indices $I = \{i \mid c_i=1\}$ for any valid codeword $c$ must satisfy the parity checks defined by the rows of $H$. While the lines of the Fano plane are 3-element subsets, the rows of $H$ (the parity checks) contain 4 '1's (as shown in Table I). The set of codewords $C$ is closely related to the Fano plane, as the codewords of weight 3 correspond to the cyclic translates of the difference set $\{0, 1, 3\}$ in $\mathbb{Z}/7\mathbb{Z}$.1

### **III.2. Syndrome Calculation and Geometric Error Isolation**

The ability of the Hamming code to correct a single error relies on the syndrome calculation $S = H r^T \pmod 2$, where $r$ is the received 7-bit word. The syndrome $S$ is a 3-bit vector in $\mathbb{F}_2^3$.15

The geometry provides a direct mapping for the syndrome resolution. There are $2^3 - 1 = 7$ possible non-zero syndromes.

1. The 7 non-zero syndrome vectors are precisely the 7 non-zero vectors of $\mathbb{F}_2^3$.  
2. These 7 vectors correspond exactly to the 7 columns of $H$, $H_1$ through $H_7$.9  
3. If a single error occurs at position $i$, the received word $r = c + e_i$, where $e_i$ is the error vector with a '1' only at position $i$.  
4. The syndrome calculation yields $S = H r^T = H (c^T + e_i^T) = H c^T + H e_i^T$. Since $c$ is a codeword, $H c^T = 0$. Thus, $S = H e_i^T$, which is simply the $i$-th column of $H$, $H_i$.9

This establishes a powerful relationship: the syndrome $S$ is mathematically equivalent to the coordinate vector $v_i$ of the Fano point $P_i$. The Fano plane visualization therefore acts as the immediate geometric lookup table for error correction. The code visually isolates the error location by determining which Fano point corresponds to the computed syndrome vector $S$.

### **III.3. Animated Error Correction I: Visualizing Syndrome Decoding**

The animation sequence must dynamically illustrate the decoding process by mapping the algebraic syndrome back onto the Fano plane geometry.

#### **Animated Sequence: Single Error Correction**

1. **Initial State:** Display a valid codeword $c$ (e.g., the all-zero vector, $0000000$) on the Fano plane, possibly by assigning states (0/1) to the 7 points.  
2. **Error Introduction:** Simulate transmission noise by introducing a single bit flip at a point $P_i$ (e.g., $r = 0001000$). The point $P_i$ should be visually highlighted (e.g., colored red).  
3. **Syndrome Calculation:** The decoder computes the syndrome $S = H r^T$.  
4. **Parity Check Activation:** For each row $\ell_j$ of $H$, determine if the check failed ($S_j = 1$). The visualization dynamically highlights the lines $\ell_j$ corresponding to failed checks (e.g., highlighted yellow).  
5. **Geometric Resolution:** The animated process shows that the highlighted lines intersect uniquely at the error point $P_i$. The syndrome vector $S$ is displayed algebraically, confirming that $S$ is the column vector corresponding to the coordinates of $P_i$. The animation concludes by correcting the bit at $P_i$.

#### **Advanced Animation: Visualizing the $d=3$ Limitation**

The Hamming code can only correct single errors; it cannot distinguish a single-bit error from a double-bit error.16 This limitation is also transparently represented by the Fano geometry.

1. **Weight-2 Error Introduction:** Introduce two errors at non-collinear points, say $P_i$ and $P_j$.  
2. **Syndrome Misinterpretation:** The resulting syndrome is $S = H_i + H_j$. Since $P_i$ and $P_j$ are distinct and non-zero, their sum $P_i + P_j$ must equal the coordinate vector of the third point on their unique line, $P_k$ (where $P_i + P_j + P_k = 0$, implying $P_i + P_j = P_k$).  
3. The animation will highlight the point $P_k$ (the third point on the line containing the two actual errors) as the *apparent* error location, based on the syndrome $S$.  
4. This visualization demonstrates the code failure: the syndrome points to a single, incorrect location $P_k$, proving that Hamming codes, while perfect for $d=3$, cannot reliably correct double errors.16 The visualization confirms that the sum of any two columns of $H$ (two single-error syndromes) equals a third column of $H$ (a third single-error syndrome), leading to decoding ambiguity.

## **IV. Quantum Error Correction: The Steane \[\] Code**

The Fano geometry provides the geometric structure for the Steane code, $\[\]$, which is the smallest representative of the family of quantum Hamming codes and is constructed using the Calderbank-Shor-Steane (CSS) formalism.18

### **IV.1. CSS Construction and Geometric Duality**

The Steane code is derived directly from the classical $$ Hamming code $C$ and its dual $C^\perp$. The Steane code encodes one logical qubit into seven physical qubits and maintains a minimum distance of $d=3$, allowing it to correct arbitrary single-qubit errors (Pauli errors $X, Y, Z$).18

Quantum error correction requires stabilization against both bit-flip errors ($X$) and phase-flip errors ($Z$). This necessitates defining two sets of checks.

The Fano plane structure facilitates this dual requirement because the geometry is self-dual: points and lines can be exchanged while maintaining the incidence rules.1 This geometric self-duality is mathematically reflected in the fact that the code uses the same underlying structure, $H$, for both sets of checks.

The Steane code's check matrix in the stabilizer formalism is given by a $6 \times 7$ matrix $M$:

$$M = \begin{bmatrix} H & 0 \\ 0 & H \end{bmatrix}$$

where $H$ is the $3 \times 7$ parity-check matrix (Table I).18 The top block $M_{Z} = \[H \ | \ 0\]$ defines the $Z$-type stabilizers (used to detect $X$ errors), and the bottom block $M_{X} = \[0 \ | \ H\]$ defines the $X$-type stabilizers (used to detect $Z$ errors).

### **IV.2. Geometric Definition of Quantum Stabilizers**

The Steane code has six independent stabilizer generators: three $Z$-type ($S_{Z1}, S_{Z2}, S_{Z3}$) and three $X$-type ($S_{X1}, S_{X2}, S_{X3}$).20 These stabilizers are derived directly from the rows of the Fano incidence matrix $H$. Since each row of $H$ has a Hamming weight of 4, all stabilizer generators are weight-4 Pauli operators.19

The code example plan must implement these operators by mapping the Fano lines (the rows of $H$) to the support indices of the Pauli operators.

Table III. Steane Stabilizers and Fano Lines Correspondence

| Generator Index i | Check Matrix Row | Fano Line Support (Indices) | Z-Stabilizer SZi​​ (Detects X errors) | X-Stabilizer SXi​​ (Detects Z errors) |
| :---- | :---- | :---- | :---- | :---- |
| 1 | $H_1$ | $\{1, 4, 6, 7\}$ | $Z_1 Z_4 Z_6 Z_7$ | $X_1 X_4 X_6 X_7$ |
| 2 | $H_2$ | $\{2, 4, 5, 7\}$ | $Z_2 Z_4 Z_5 Z_7$ | $X_2 X_4 X_5 X_7$ |
| 3 | $H_3$ | $\{3, 5, 6, 7\}$ | $Z_3 Z_5 Z_6 Z_7$ | $X_3 X_5 X_6 X_7$ |

In a quantum computation environment, these operators are implemented as measurement circuits that determine the eigenvalue ($\pm 1$) of the stabilizer on the quantum state, yielding the syndrome bits.

### **IV.3. Animated Quantum Syndrome Calculation**

The geometric visualization must now connect the Fano incidence structure to the fundamental quantum concept of Pauli operator commutation. An error $E$ is detected if it anticommutes with a stabilizer $S$ (i.e., $E S = -S E$, resulting in a syndrome bit of 1).

The profound connection here is that the Fano plane geometry functions as the error commutation graph for the Steane code. An $X$ error on qubit $i$ anticommutes with the $Z$-stabilizer $S_{Z, j}$ if and only if the coefficient $H_{j, i}=1$. Geometrically, this means the error is detected if the point $P_i$ is incident with the line $\ell_j$ that defines the stabilizer $S_{Z, j}$.

#### **Animated Sequence: Quantum Error Detection**

1. **X Error Simulation:** Introduce an $X_i$ error at qubit $i$. The visualization highlights $P_i$.  
2. **Syndrome Check (Z-Stabilizers):** The code computes the $Z$-syndrome by checking which $S_{Z, j}$ anticommute with $X_i$.  
3. **Geometric Detection:** For every $S_{Z, j}$ that anticommutes (syndrome bit 1), the corresponding Fano line $\ell_j$ is highlighted (e.g., blue).  
4. **Error Correction:** The intersection of the blue lines uniquely identifies $P_i$, revealing the physical location of the $X$ error.  
5. **Z Error Simulation:** Similarly, introduce a $Z_i$ error at qubit $i$.  
6. **Syndrome Check (X-Stabilizers):** The code computes the $X$-syndrome by checking which $S_{X, j}$ anticommute with $Z_i$.  
7. **Geometric Detection:** For every $S_{X, j}$ that anticommutes, the corresponding Fano line $\ell_j$ is highlighted (e.g., green).  
8. **Duality Emphasis:** The animation visually confirms that the same set of Fano lines $\{\ell_1, \ell_2, \ell_3\}$ are employed for both $X$ and $Z$ error detection, emphasizing the inherent $X \leftrightarrow Z$ symmetry that defines the Steane code as a highly balanced CSS structure.

## **V. Synthesis and Advanced Animation Concepts**

The ultimate goal of this project is to create a dynamic tool that seamlessly bridges abstract algebra, finite geometry, and physical coding concepts.

### **V.1. Implementing the Dynamic Visualization Pipeline**

Code Example VI requires the integration of all previously defined components into a layered visualization pipeline. This pipeline must manage three distinct layers:

1. **Geometric Base Layer:** The fixed, underlying Fano plane structure (7 points, 7 lines).  
2. **Algebraic State Layer:** The vector labels $v_i$ and the current incidence matrix $H$.  
3. **Dynamic Error/Syndrome Layer:** The visual indicators (color changes, line highlighting) driven by the syndrome computation $S = H r^T$ or the commutation analysis $E S = \pm S E$.

The core constraint of this pipeline is to strictly maintain the mathematical fidelity of $\mathbb{F}_2$ arithmetic (matrix multiplication and vector addition modulo 2\) while translating the resulting algebraic permutations into smooth Euclidean animations (e.g., using libraries like Manim 22).

### **V.2. The Power of Rotation: Demonstrating Transitivity and Equivalence**

A critical element of the advanced animation is demonstrating the transitivity of the Fano plane under the action of its automorphism group, $PGL(3, 2)$. As established in Section II.2, the code must implement the dynamic re-mapping of Euclidean coordinates based on the algebraic transformation $A v_i$.

The animation sequence should involve a 'rotation' or 're-shuffling' where the point visually occupying the unique "centroid" position (P7) is algebraically mapped to one of the "midpoint" positions (P1, P2, P3), and vice versa. Simultaneously, the single circular line must be mapped to one of the straight lines. When the geometry re-renders based on the new permutation, the visual distinction must disappear, reinforcing that all 7 points and 7 lines are geometrically equivalent. This visual proof through motion justifies the uniform applicability of the syndrome checks across all 7 qubits, confirming that the Fano structure is truly highly symmetric, regardless of how it is drawn.

### **V.3. Visualizing Undetectable Errors and Logical Operators**

The final and most sophisticated animation segment involves visualizing the failure mode of the code, specifically the errors that are undetectable because they map to the all-zero syndrome, $S=0$.

#### **Classical Undetectability**

A weight-3 error $e$ is undetectable if $H e^T = 0$. This occurs when the indices $i, j, k$ where $e_i=e_j=e_k=1$ correspond to a set of points that are collinear (i.e., they form a line $\ell$).7 The animation should contrast the previously corrected single error with this scenario: when a weight-3 error on a line $\ell$ is introduced, the syndrome calculation yields $S=0$, and no lines are highlighted, visually demonstrating that the decoder mistakenly concludes "no error".17

#### **Quantum Logical Operators**

The logical operators $X_L$ and $Z_L$ of the Steane code must commute with all six stabilizers (i.e., they yield a zero syndrome for both $X$ and $Z$ checks), yet they remain detectable only by measuring the logical qubit itself. The Steane code has logical operators of minimal weight $d=3$.

The visualization must interpret these logical operators geometrically. A logical operator, say $X_L$, involves a subset of three qubits, $\{i, j, k\}$. Since $H X_L^T = 0$, this subset of three points must satisfy the linear dependence constraints required of the code space. Critically, these points $\{P_i, P_j, P_k\}$ are *non-collinear*. If they were collinear, they would form a line in the Fano geometry, and thus a codeword in $C^\perp$, which would result in a weight-3 *stabilizer* rather than a logical operator. The fact that the physical errors associated with $X_L$ and $Z_L$ are weight-3, satisfy $H e^T=0$, but *do not* form a line visually confirms their role as undetectable operators that define the boundaries of the encoded space.

This geometric interpretation demonstrates a generalized principle: the construction of robust error correction codes, including Finite Geometry Low-Density Parity-Check (FG-LDPC) codes, relies on carefully selecting subsets of points and lines from $\text{PG}(k, q)$ to ensure desirable distance properties.4 The Fano plane, as $\text{PG}(2, 2)$, provides the smallest and most illustrative instance of this fundamental algebraic relationship between geometry and coding theory.

## **VI. Conclusion**

The preceding plan details a robust, expert-level set of code examples designed to facilitate the animation of the Fano plane and elucidate its profound connections to the Hamming (7,4) and Steane $\[\]$ error correction codes.

The central recommendation for implementation is the strict adherence to the algebraic construction of $\text{PG}(2, 2)$ over $\mathbb{F}_2^3$. Utilizing the seven non-zero vectors as point labels and the incidence matrix $H$ as the core data structure ensures mathematical rigor. By modeling $H$ as the parity check matrix, the code establishes a direct, verifiable link between the geometry and the classical syndrome decoding mechanism.

For the quantum regime, the Fano incidence structure directly defines the six $X$ and $Z$ stabilizer generators of the Steane code, allowing the geometry to be visualized as the intrinsic error commutation graph. The success of the animation hinges on the sophisticated use of the $PGL(3, 2)$ automorphism group to dynamically permute point labels and associated Euclidean coordinates, thereby visually proving the high symmetry and uniformity of the structure, which is a key physical characteristic ensuring the code’s effectiveness.

The ultimate achievement of this project is the creation of a dynamic visualization tool that transforms abstract combinatorial properties—such as the definition of a perfect code or the composition of a logical operator—into intuitive geometric movements, providing a definitive visual aid for advanced study in finite fields and quantum information science.

#### **Works cited**

1. Fano plane - Wikipedia, accessed on November 25, 2025, [https://en.wikipedia.org/wiki/Fano_plane](https://en.wikipedia.org/wiki/Fano_plane)  
2. accessed on November 25, 2025, [https://en.wikipedia.org/wiki/Fano_plane\#:\~:text=The%20Fano%20plane%20is%20an%20example%20of%20an%20(n3,is%20the%20smallest%20such%20configuration.](https://en.wikipedia.org/wiki/Fano_plane#:~:text=The%20Fano%20plane%20is%20an%20example%20of%20an%20\(n3,is%20the%20smallest%20such%20configuration.)  
3. 2 Projective planes, accessed on November 25, 2025, [https://webspace.maths.qmul.ac.uk/p.j.cameron/pps/pps2.pdf](https://webspace.maths.qmul.ac.uk/p.j.cameron/pps/pps2.pdf)  
4. The Fano Plane, PG (2 , 2\) , is the simplest example of a finite projective plane., accessed on November 25, 2025, [https://www.researchgate.net/figure/The-Fano-Plane-P-G-2-2-is-the-simplest-example-of-a-finite-projective-plane_fig1_228102997](https://www.researchgate.net/figure/The-Fano-Plane-P-G-2-2-is-the-simplest-example-of-a-finite-projective-plane_fig1_228102997)  
5. Steiner system - Wikipedia, accessed on November 25, 2025, [https://en.wikipedia.org/wiki/Steiner_system](https://en.wikipedia.org/wiki/Steiner_system)  
6. Hamming code - Wikipedia, accessed on November 25, 2025, [https://en.wikipedia.org/wiki/Hamming_code](https://en.wikipedia.org/wiki/Hamming_code)  
7. Fano plane | EPFL Graph Search, accessed on November 25, 2025, [https://graphsearch.epfl.ch/en/concept/390404](https://graphsearch.epfl.ch/en/concept/390404)  
8. accessed on November 25, 2025, [https://en.wikipedia.org/wiki/Fano_plane\#:\~:text=Using%20the%20standard%20construction%20of,101%2C%20110%2C%20and%20111.](https://en.wikipedia.org/wiki/Fano_plane#:~:text=Using%20the%20standard%20construction%20of,101%2C%20110%2C%20and%20111.)  
9. Error Correcting Codes according to Hamming - MS Researchers, accessed on November 25, 2025, [https://researchers.ms.unimelb.edu.au/\~nganter@unimelb/LinAlg16/HammingCode.pdf](https://researchers.ms.unimelb.edu.au/~nganter@unimelb/LinAlg16/HammingCode.pdf)  
10. Incidence-matrix projective code | Error Correction Zoo, accessed on November 25, 2025, [https://errorcorrectionzoo.org/c/incidence_matrix](https://errorcorrectionzoo.org/c/incidence_matrix)  
11. accessed on November 25, 2025, [http://finitegeometry.org/sc/8/plane.html\#:\~:text=The%20Fano%20Plane%20Revisualized\&text=see%20it%20as%20the%20group%20of%20symmetries%20of%20something.%22\&text=Every%20permutation%20of%20the%20plane's,GL(3%2C2).](http://finitegeometry.org/sc/8/plane.html#:~:text=The%20Fano%20Plane%20Revisualized&text=see%20it%20as%20the%20group%20of%20symmetries%20of%20something.%22&text=Every%20permutation%20of%20the%20plane's,GL\(3%2C2\).)  
12. The exceptional isomorphism between PGL(3,2) and PSL(2,7): geometric origin?, accessed on November 25, 2025, [https://mathoverflow.net/questions/256598/the-exceptional-isomorphism-between-pgl3-2-and-psl2-7-geometric-origin](https://mathoverflow.net/questions/256598/the-exceptional-isomorphism-between-pgl3-2-and-psl2-7-geometric-origin)  
13. The Fano Plane Revisualized - Finite Geometry, accessed on November 25, 2025, [http://finitegeometry.org/sc/8/plane.html](http://finitegeometry.org/sc/8/plane.html)  
14. About Fano plane symmetries - Math Stack Exchange, accessed on November 25, 2025, [https://math.stackexchange.com/questions/3796118/about-fano-plane-symmetries](https://math.stackexchange.com/questions/3796118/about-fano-plane-symmetries)  
15. Hamming (7,4) code with soft and hard decoding - DSP LOG, accessed on November 25, 2025, [https://dsplog.com/2012/03/15/hamming-code-soft-hard-decode/](https://dsplog.com/2012/03/15/hamming-code-soft-hard-decode/)  
16. 14.1 The Hamming code | Introduction to Quantum Information Science - Qubit Guide, accessed on November 25, 2025, [https://qubit.guide/14.1-the-hamming-code](https://qubit.guide/14.1-the-hamming-code)  
17. Hamming(7,4) - Wikipedia, accessed on November 25, 2025, [https://en.wikipedia.org/wiki/Hamming(7,4)](https://en.wikipedia.org/wiki/Hamming\(7,4\))  
18. Steane code - Wikipedia, accessed on November 25, 2025, [https://en.wikipedia.org/wiki/Steane_code](https://en.wikipedia.org/wiki/Steane_code)  
19. The \[\[7, 1, 3\]\] Steane code is the smallest representative of the... | Download Scientific Diagram - ResearchGate, accessed on November 25, 2025, [https://www.researchgate.net/figure/The-7-1-3-Steane-code-is-the-smallest-representative-of-the-family-of-2D_fig5_393889360](https://www.researchgate.net/figure/The-7-1-3-Steane-code-is-the-smallest-representative-of-the-family-of-2D_fig5_393889360)  
20. QEC: Steane Seven-Qubit Code - Qniverse, accessed on November 25, 2025, [https://qniverse.in/docs/qec-steane-seven-qubit-code/](https://qniverse.in/docs/qec-steane-seven-qubit-code/)  
21. \(\[\[7,1,3\]\]\) Steane code | Error Correction Zoo, accessed on November 25, 2025, [https://errorcorrectionzoo.org/c/steane](https://errorcorrectionzoo.org/c/steane)  
22. Fano Plane: The World's Smallest Projective Geometry - YouTube, accessed on November 25, 2025, [https://www.youtube.com/shorts/oJvjbFicOtM](https://www.youtube.com/shorts/oJvjbFicOtM)  
23. Steiner systems and projective planes | Combinatorics Class Notes - Fiveable, accessed on November 25, 2025, [https://fiveable.me/combinatorics/unit-13/steiner-systems-projective-planes/study-guide/94Souzqt7UjFBVjP](https://fiveable.me/combinatorics/unit-13/steiner-systems-projective-planes/study-guide/94Souzqt7UjFBVjP)