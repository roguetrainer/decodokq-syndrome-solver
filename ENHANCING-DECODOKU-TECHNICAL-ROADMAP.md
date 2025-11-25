
# **Enhancing Decodoku: A Technical Roadmap for Expanding Error Correction Codes and Gamified QEC Research**
The Decodoku project currently offers a unique citizen science platform dedicated to exploring decoding strategies for highly specialized qudit variants of surface codes.1 While this foundational work addresses complex challenges in high-dimensional quantum systems ($\mathbb{Z}_d$, where $d>2$), a comprehensive expansion requires architectural changes to integrate standard qubit codes (e.g., those operating in $\mathbb{Z}_2$) and introduce dynamic gameplay reflective of current quantum error correction (QEC) research bottlenecks, such as multi-round syndrome extraction and optimization for biased noise.3 This report details the necessary structural refactoring, the integration of specific quantum and classical error correction codes, and a suite of innovative gameplay mechanics to fulfill these objectives.

## **Section 1: Architectural Foundation and Code Modularity**

### **1.1. Decodoku’s Current Qudit Architecture and Limitations**

The existing Decodoku codebase is explicitly designed around the problem of decoding qudit variants of surface codes.2 The architecture utilizes a grid layout where small squares represent qudits—quantum systems capable of taking more than two values, often $d=10$ in the original formulation.1 The core puzzle mechanic centers on satisfying parity checks (stabilizer measurements) defined over large interlocking plaquettes, where the resulting check quantity depends on the states of the surrounding qudits.2 The rules for these squares demand that the qudits follow a specific modular arithmetic, such as requiring the sum of the numbers around a square to be a multiple of $d=2$ (for qubits) or $d=10$ (for qudits).5

This specialized implementation, designed to generate data and heuristics for complex qudit decoding algorithms 2, imposes severe architectural constraints when attempting to integrate standard qubit-based QEC codes, which operate exclusively within the binary field $\mathbb{Z}_2$. The primary limitation is the proprietary handling of $\mathbb{Z}_d$ arithmetic, which is distinct from the Pauli group algebra fundamental to standard stabilizer codes. To support a wider family of codes, the codebase must transition to a generalized framework that can handle both the higher-dimensional arithmetic (for the existing qudit codes) and the foundational binary arithmetic (for qubit codes).

### **1.2. Establishing a Generalized Stabilizer Code Framework (CSS Abstraction)**

The most effective pathway for integrating diverse codes is through the abstraction of the stabilizer formalism. Most prominent quantum codes, including the Toric Code, Surface Code, and Color Codes, are Calderbank-Shor-Steane (CSS) codes.6 Stabilizer codes, in general, allow for a direct mapping of many classical methods into the quantum spectrum, making them highly useful for defining game mechanics.8

To achieve this generalization, the architecture requires a refactoring wherein core components are abstracted using standardized data structures. This necessitates developing an abstract base class, CodeDefinition, which can manage all code-specific parameters.9 This class must parameterize the code's topology (e.g., planar, toroidal), the field dimension ($d$), and the set of stabilizer generators ($S$).9

The existing $\mathbb{Z}d$ addition parity checks in the StabilizerCheck module must be replaced by a generalized function that understands both group multiplication for Pauli operators (for $d=2$) and modular addition (for $d\>2$).5 For qubit codes, the stabilizer generators $Si$ are Pauli products (e.g., $Z otimes I otimes Z$).9 The check function must be able to perform commutation tests to determine the syndrome, effectively checking if an applied error operator ($E$) commutes with the stabilizer ($Si$): $Si E \= pm E Si$. The sign $(pm 1)$ determines the syndrome bit. This transition is essential for providing universal support for arbitrary stabilizer codes, including both quantum CSS codes and their classical linear code ancestors.10

### **1.3. Implementing a Flexible Graph Topology Module**

The implementation of topological codes beyond the basic planar grid requires decoupling the code definition from a fixed Cartesian geometry. Codes like the Toric Code and Color Code rely on specific, non-trivial graph structures.11

The Toric Code, for instance, is defined on a lattice that forms a torus, requiring periodic boundary conditions where vertices and edges on opposing sides are identified.12 The Color Code is defined on graphs that are triangulations of surfaces and must satisfy specific coloring properties (often 3-colorable).11 These complex geometries cannot be efficiently modeled using a rigid grid system.

A general graph data structure (nodes, edges, plaquettes/faces) is required to represent the connectivity of physical qubits (edges or vertices) and the support of the stabilizer generators (plaquettes or vertices).13 This abstraction enables the Toric Code to implement its "Pac-Man" wrap-around geometry 12 and allows the Color Code to be implemented on lattices such as the 6.6.6 or 4.8.8 lattices.14 This modification provides the necessary structural foundation for supporting a comprehensive library of quantum codes.

The architectural recommendations for this structural change are summarized in the following table:

Table 1: Recommendations for Code Base Extension Modularity

| Component | Current Function (Qudit Surface Code) | Required Modification/Extension | Implementation Goal |
| :---- | :---- | :---- | :---- |
| CodeDefinition Class | Hard-coded rules for Qudit Surface Code geometry and $\mathbb{Z}{10}$ checks 1 | Abstract Base Class defining topology (Graph), dimension (d), and StabilizerSet (generators $S$).9 | Universal support for arbitrary stabilizer codes. |
| StabilizerCheck Module | $\mathbb{Z}d$ addition parity checks | Generalized parity check function that takes basis ($X/Z$) and field size ($d$), performing group multiplication/commutation checks.9 | Support both CECCs (linear codes) 10 and QECCs (CSS codes).8 |
| NoiseModel Module | Random error injection (static) | Dynamic, time-dependent, and biased error generation (e.g., $pZ gg pX$).4 | Enable Multi-Round and Biased Noise Modes. |

## **Section 2: Advanced Topological Quantum Error Correction Codes**

Topological codes are highly attractive for gamification due to their inherent visual structure and reliance on simple, local checks.2 Implementing the Toric Code and the Color Code significantly increases the complexity and scientific relevance of the decoding puzzles.

### **2.1. The Toric Code: Homology and Toroidal Topology**

The Toric Code, Kitaev's landmark construction, is a topological code often categorized as a closed-surface variant of the surface code.6 It is defined on an $L times L$ grid whose edges are identified, forming the topology of a torus.12 A code of size $L times L$ uses $2L^2$ physical qubits (placed on the edges) to encode $k=2$ logical qubits.15 The distance of the code, $d$, is $L$, meaning that errors shorter than $L$ edges must be correctable.15

#### **Gameplay: Pac-Man Boundaries and Loops**

To accurately represent the Toric Code, the game environment must enforce the periodic boundary conditions.12 This translates into "Pac-Man" geometry: when a path of errors or a player-applied correction operation disappears off the right side of the screen, it must reappear on the left side at the same vertical position, and similarly for the top and bottom edges.12

#### **The Dual Logical Challenge**

A key characteristic of the Toric Code is the encoding of two logical qubits ($k=2$).15 Logical errors in the Toric Code correspond to non-trivial loops that wrap around the torus.12 Since the torus has two non-contractible cycles (one red loop extending left-to-right and one blue loop extending top-to-bottom) 12, the game must visually track two independent pairs of logical operators ($X1, Z1$ and $X2, Z2$).

This transition from the standard planar surface code ($k=1$) to the Toric Code ($k=2$) is not merely a change in boundary condition; it introduces a crucial complexity leap in the decoding problem.16 The player must ensure that their correction path (a chain of Pauli operations) cancels the error syndrome without creating a logical error on *either* logical qubit. An error chain that would be a boundary in the planar code might become a non-trivial cycle in the toroidal geometry.13 This requires the player to understand homology—the principle that two distinct physical error chains are equivalent if they differ only by a stabilizer (a cycle that is a boundary of a region).13 The puzzle demands players simultaneously manage two coupled logical information channels, highlighting the significant trade-off between maximizing the encoded logical information ($k$) and maintaining code reliability.

### **2.2. The Color Code Family: Graph Coloring as Stabilization**

Color codes are a robust family of topological CSS codes defined on specific $d$-colorable graphs, often originating from triangulations of 2D or 3D manifolds.7 Two-dimensional color codes are typically defined on 3-colorable lattices, such as the 6.6.6 or 4.8.8 lattices.11

#### **Puzzle Mechanic: Constraint Satisfaction and Graph Theory**

Gamifying the Color Code requires translating the structural constraints of the 3-colorable graph into a visual puzzle. The qubits are placed on the simplices (nodes or edges), and the stabilizers are supported on suitable neighboring simplices.11 The puzzle can visualize the coloring constraint: a syndrome occurs when the quantum state violates the local coloring rule defined by the stabilizers. The player's objective becomes a constraint satisfaction problem, similar to abstract graph coloring puzzles.17 The visual interface would dynamically highlight sections of the graph that violate the 3-coloring rule, simplifying the complex mathematical definition of the stabilizer group into a visually accessible logical problem.

#### **Advanced Objective: Transversal Gate Solutions**

The Color Code provides a unique opportunity to gamify a concept beyond simple error correction: **Fault-Tolerant Logical Operations**. The 2D color code is notable because it admits transversal gates, such as the CNOT gate.7 A transversal gate is one that acts on the logical state by applying a simple tensor product of unitary operations to each physical qubit independently, thereby propagating noise minimally—a highly desirable property for Fault-Tolerant Quantum Computation (FTQC).19

The game objective can be structured such that the final successful puzzle state is not merely a zero-syndrome state, but a correct logical state achieved via a predetermined sequence of moves that correspond to a transversal logical gate.19 This requires the player to structure their correction strategies around operations that maintain the fault-tolerant nature of the code structure. This design decision elevates the scientific utility of the game by forcing players to engage with the principles of fault-tolerant architecture, directly linking the puzzle solution set to fundamental constraints in quantum hardware design.

## **Section 3: Non-Topological and Classical Error Correction Codes**

To broaden the educational scope and illustrate the origins of modern QEC, the introduction of non-topological codes, both quantum and classical, is necessary.

### **3.1. Shor’s 9-Qubit Code: Sequential Diagnosis**

Shor's 9-qubit code, $\[\]$, is a foundational non-topological QECC that uses nine physical qubits to encode one logical qubit.20 Its structure implicitly relies on concatenation, nesting a phase-flip code within three 3-qubit bit-flip repetition codes.21

#### **Gameplay: Multi-Stage Decoding**

A defining characteristic of Shor's code is the requirement for sequential diagnosis and correction due to the non-commuting nature of $X$ and $Z$ errors ($XZ=-ZX$).21 The procedure first detects and corrects bit-flip ($X$) errors, followed by detection and correction of phase-flip ($Z$) errors.21

This sequential requirement maps naturally onto a **multi-stage puzzle mechanic**.22 Stage 1 would present the syndrome measurements for the X-type checks, forcing the player to locate which of the three 3-qubit blocks contains the error.20 Stage 2, unlocked upon successful identification, allows the player to perform the Z correction required to finalize the decoding process. This tiered interface models the reality of syndrome measurement circuits in QEC systems.23 The structure highlights the hierarchical nature of error protection, analogous to concatenated codes which use simpler inner codes to protect information before processing by a more complex outer code.24

### **3.2. Didactic Module: Linear Block Codes (Hamming)**

To serve as an accessible introductory module, classical linear block codes must be integrated. Hamming codes, specifically the $$ code, are perfect codes used for single-error correcting and double-error detecting (SECDED).10

#### **Mechanic: Syndrome Decoding Visualization**

This module would provide a pedagogical foundation for the stabilizer concept utilized in all quantum CSS codes.8 The game presents a 7-bit received codeword, visualizing the calculation of the 3-bit error syndrome using the parity check matrix ($H$).10 The visual interface would show how three overlapping checks (based on the rows of $H$) determine the syndrome. If the received word is not a valid codeword, the resulting syndrome (a non-zero 3-bit string) uniquely identifies the location of the single error bit.27 This direct mapping from syndrome calculation to unique error location provides an unambiguous and mathematically elegant introduction to the principle of syndrome decoding—a process essential for all stabilizer codes.10

### **3.3. Feasibility Note on Reed-Solomon (RS) Codes**

Reed-Solomon (RS) codes are powerful classical codes primarily used for correcting burst errors, relying on polynomial arithmetic over Galois fields ($GF(q)$).28 Their decoding process typically involves calculating determinants and complex mathematical steps.29

While the complexity of Galois field arithmetic makes a direct visual translation challenging for a general audience, an advanced numerical puzzle variant could be constructed. This puzzle would focus on the code's core principle: representing the message as a polynomial of degree less than $k$ and using $n$ transmitted values (the codeword).28 The player's task would be to reconstruct the original polynomial (message) by interpolating the $k$ original points despite the corruption of $t=(n-k)/2$ errors.28 This would create a high-level numerical challenge requiring strategic placement of points to solve the system of linear equations.29

## **Section 4: Innovation in Dynamic and Strategic Game Play**

The greatest opportunities for advancing Decodoku lie in moving beyond static, single-snapshot puzzles to dynamic, temporal, and strategic gameplay that mirrors the computational challenges of practical QEC decoding.

### **4.1. Multi-Round Decoding: The Temporal Dimension in QEC**

#### **Scientific Rationale**

Practical fault-tolerant quantum computation relies on repeatedly measuring the syndrome checks to track errors over time.3 This process, called multiround syndrome extraction, is necessitated because errors can occur not only on the data qubits but also during the complex measurement circuit itself (measurement errors).23 Decoders must analyze this syndrome history across multiple time steps to infer the most probable underlying error path.3

#### **Mechanic: Syndrome History Puzzles**

The game must introduce a temporal dimension, transforming the 2D grid puzzle into a 3D space-time decoding challenge. The player is presented with a sequence of syndrome maps, one for each time step ($t1, t2, dots, tN$).23 The player's task is to filter this history, distinguishing which syndrome events were caused by a stable data error (a long-lived defect) versus a transient measurement error (a single-round flip of the syndrome bit).

This temporal inference is achieved by mapping the error correction problem onto a graph where nodes represent syndrome events across space and time. The goal is to find the minimum-weight path (error chain) connecting these syndrome events through the 3D lattice. This fundamentally extends the classical "LightsOut" puzzle analogy.8 In a standard QEC interpretation of LightsOut, applying an operation (toggling a switch) flips the state of neighboring lights (syndromes). In the dynamic extension, an operation applied at time $ti$ affects the syndromes observed at time $t{i+1}$, forcing players to incorporate latency and causality into their solution strategy. Analyzing player performance in this mode provides invaluable behavioral data for training advanced AI decoders.3

### **4.2. Competitive and Adversarial Game Theory**

The use of game theory introduces strategic interaction, providing a novel methodology for exploring the limits of quantum codes.30 Error correction mechanisms themselves are viewed in game theory as vital for maintaining stable cooperative behaviors by allowing players to recognize and amend mistakes.31

#### **Adversarial Mode (Player vs. Decoder)**

This mode directly translates the scientific challenge of determining a code's minimum distance ($d$) into a competitive game. Player A (the Adversary) is granted a limited budget of errors and attempts to introduce an error chain that causes a logical fault (e.g., a non-contractible loop in the Toric Code).15 Player B (the Decoder) must correct the resulting syndrome before a time limit is reached.32

This setup creates a powerful min-max optimization loop. The adversarial player is motivated to find the weakest point in the code's geometry—the smallest number of errors that leads to logical failure. Collecting this data, representing human-intuited, low-weight logical operators, is critical for validating the theoretical distance of small-scale quantum codes.30 This provides a practical, gamified tool for code discovery and optimization, supplementing complex reinforcement learning techniques used to find better quantum low-density parity-check (qLDPC) codes.33

#### **Competitive Race**

A simpler competitive mode involves two players racing to solve the same error pattern, with tiered rewards based on speed, accuracy, and efficiency (e.g., minimal resource usage).32 This fosters the spontaneous development of community-driven heuristics that can be logged and analyzed by researchers, fulfilling the original citizen science mandate.1

### **4.3. Modeling Biased Noise and Strategic Resource Allocation**

#### **Scientific Rationale**

Real-world quantum hardware often operates under highly anisotropic or "biased" noise, where one type of error (e.g., phase flips, $Z$ errors) occurs much more frequently than others (bit flips, $X$ errors).4 Effective QEC implementation requires decoding strategies tailored to this physical error profile to minimize resource overhead.4 For instance, rotated surface codes are often preferred in certain architectures due to their better performance under typical biased noise.4

#### **Mechanic: Weighted Cost Function**

To gamify this reality, the NoiseModel must be extended to allow configuration of noise bias ($pZ gg pX$).4 Critically, the correction operations applied by the player must be assigned a non-uniform cost metric. If the channel is $Z$-biased, the player might face a disproportionately high penalty (or cost) for applying $X$ corrections versus $Z$ corrections, reflecting the physical resources required.

The player's objective then shifts from finding the physically shortest path (minimum Hamming weight of the correction operator) to finding the **minimum weighted cost path**. This strategic requirement forces the player to minimize the use of high-cost operations, optimizing their strategy to align with the constraints imposed by the noisy quantum hardware. This directly models the efforts in quantum engineering to reduce the overhead necessary for effective fault tolerance.4

### **4.4. Nested and Hierarchical Puzzles (Concatenation)**

The principle of concatenation—building complex, reliable codes from simpler component codes—is fundamental to reducing decoding complexity.24 This structural elegance can be translated into hierarchical gameplay.36

#### **Mechanic: Puzzle Within a Puzzle**

By designing modules that reflect concatenation, the game creates a "puzzle within a puzzle." For instance, a logical qubit could be protected by an outer code (like Shor's structure) 21, where each physical qubit in the outer code is itself protected by an inner code (like a Hamming code).24

The player must first solve the local correction puzzle corresponding to the inner code (e.g., correcting the single error in a 7-bit Hamming block).10 The successful solution of this local puzzle then outputs the syndrome information needed to diagnose and correct the higher-level logical error associated with the outer code.37 This hierarchical approach not only provides a natural progression of difficulty but also allows players to visualize how modularity and nesting reduce the overall decoding challenge, providing an intuitive understanding of the efficiency gains offered by codes such as Shor's and general concatenated schemes.35

## **Section 5: Technical Implementation Roadmap and Conclusion**

### **5.1. Code Architecture Refinement Summary**

The proposed extensions necessitate rigorous structural refinement of the Decodoku codebase. The creation of a universal CodeDefinition class and a generalized StabilizerCheck module, as outlined in Table 1, is mandatory for managing heterogeneous codes (qudits, Toric, Color, Hamming).

A critical step is formalizing the **Stabilizer Duality**. All stabilizer codes can be viewed as an instance of the generalized LightsOut problem, where applying a correction operator (a switch) affects the surrounding syndrome values (lights).8 Implementing this duality explicitly in the code allows for easy translation between an applied correction operation and the resulting syndrome change, which is essential for rapid testing and game logic verification across diverse code types. Furthermore, integrating classical linear block codes (Section 3.2) requires specialized functions for linear algebra over the finite field $\mathbb{F}2$ (binary arithmetic) 10, which should be housed in a separate, didactic code library.

### **5.2. UI/UX Strategies for Complex Visualizations**

Complex error correction mechanisms demand advanced user interface strategies to remain intuitive:

1. **Toric Code and Homology:** Logical operators (errors that wrap the torus) must be visually distinct from correctable error boundaries. The UI should use prominent visual loops (e.g., red and blue winding paths) to demonstrate the non-trivial nature of logical errors.12  
2. **Multi-Round Visualization:** Tracking syndrome history requires a layered or temporal UI element. A time-slider or a stack of 2D grid representations, showing the syndrome map at each step $t=1$ to $t=N$, is necessary for players to analyze the space-time syndrome chain and perform temporal inference.23  
3. **Color Code Constraints:** The puzzle must leverage visual perception principles.18 The UI should dynamically highlight connected nodes (qubits) that violate the 3-coloring rule imposed by the stabilizers, ensuring that the puzzle relies on accessible visual constraint satisfaction rather than complex group theory.17  
4. **Biased Noise Cost:** The interface must clearly communicate the weighted cost associated with each correction move type (X vs. Z), visually reinforcing the concept of resource allocation and overhead minimization against a biased noise profile.4

### **5.3. Future Research Directions via Gamified Data Collection**

Expanding Decodoku creates a versatile research tool that fulfills and extends the original citizen science mission.1 The new gameplay modes allow researchers to extract computationally hard-to-find data points:

1. **Logical Operator Discovery:** The adversarial mode (Section 4.2) generates a dataset of human-optimal, low-weight logical error chains. This data is invaluable for validating the minimum distance ($d$) of newly designed or small-scale codes and for informing the construction of efficient qLDPC codes.30  
2. **AI Decoder Training Data:** Human performance data in the Dynamic Decoding mode (Section 4.1)—specifically, how players filter measurement noise and infer errors over time—can provide sophisticated temporal heuristics that can be used to train and refine machine learning models used for practical QEC decoding.3  
3. **Code Optimization Strategies:** Data gathered from the Biased Noise puzzles provides direct evidence of human efficiency in strategic resource allocation under hardware-specific constraints. This information helps benchmark the robustness of different decoding algorithms against realistic anisotropic noise channels.4

## **Conclusions and Recommendations**

The expansion of the Decodoku codebase beyond its original specialized qudit surface code implementation presents a profound opportunity to create a comprehensive, scientifically rigorous educational and research platform.

The architectural recommendations prioritize modularity through the implementation of a generalized CSS framework and a flexible graph topology module. This refactoring is essential to accommodate advanced quantum codes, specifically the Toric Code (introducing toroidal geometry and dual logical information tracking) and the Color Code (introducing transversal gates and graph coloring constraints).

The proposed innovations in gameplay—Multi-Round Dynamic Decoding, Adversarial Game Theory, and Biased Noise modeling—transform the platform from a static puzzle generator into a dynamic simulation environment that mirrors the most pressing computational challenges in experimental QEC decoding. By strategically mapping these research bottlenecks onto intuitive game mechanics, the Decodoku project can continue its mission, leveraging human intuition to solve problems of high complexity, accelerating the development of efficient quantum decoding heuristics, and providing a powerful, accessible educational tool for the entire quantum computing community.

**Actionable Recommendations:**

1. **Prioritize Modular Re-Architecture:** Immediately implement the CodeDefinition and StabilizerCheck abstractions to ensure the codebase can universally handle both $\mathbb{Z}d$ qudit codes and $\mathbb{Z}2$ qubit codes.  
2. **Implement Toric Code First:** Given its foundational status and visual analogy (Pac-Man geometry) 12, the Toric Code provides the simplest path to introduce topological complexity ($k=2$ logical qubits) and periodic boundary conditions.15  
3. **Develop Dynamic Decoding Module:** Launch the Multi-Round Decoding mode as a high-priority research feature. The data collected on human temporal inference is highly valuable for advanced AI decoder development.3  
4. **Integrate Didactic Modules:** Embed the Hamming code module as the foundational learning level to ensure accessibility for players new to linear codes and syndrome decoding.10

#### **Works cited**

1. The Science Behind the Games, accessed on November 24, 2025, [http://decodoku.blogspot.com/2016/03/quantum-error-correction-game.html](http://decodoku.blogspot.com/2016/03/quantum-error-correction-game.html)  
2. arXiv:1712.09649v1 \[quant-ph\] 27 Dec 2017, accessed on November 24, 2025, [https://arxiv.org/pdf/1712.09649](https://arxiv.org/pdf/1712.09649)  
3. NVIDIA and QuEra Decode Quantum Errors with AI | NVIDIA Technical Blog, accessed on November 24, 2025, [https://developer.nvidia.com/blog/nvidia-and-quera-decode-quantum-errors-with-ai/](https://developer.nvidia.com/blog/nvidia-and-quera-decode-quantum-errors-with-ai/)  
4. Q-Pandora Unboxed: Characterizing Resilience of Quantum Error Correction Codes Under Biased Noise \- MDPI, accessed on November 24, 2025, [https://www.mdpi.com/2076-3417/15/8/4555](https://www.mdpi.com/2076-3417/15/8/4555)  
5. 14 \- Qudit Codes \- Decodoku: Gaming for science\!, accessed on November 24, 2025, [http://decodoku.blogspot.com/2016/07/14-qudit-codes.html](http://decodoku.blogspot.com/2016/07/14-qudit-codes.html)  
6. Kitaev surface code \- Error Correction Zoo, accessed on November 24, 2025, [https://errorcorrectionzoo.org/c/surface](https://errorcorrectionzoo.org/c/surface)  
7. Quantum codes with transversal gates | Error Correction Zoo, accessed on November 24, 2025, [https://errorcorrectionzoo.org/list/quantumtransversal](https://errorcorrectionzoo.org/list/quantum_transversal)  
8. Review on the decoding algorithms for surface codes \- arXiv, accessed on November 24, 2025, [https://arxiv.org/html/2307.14989v4](https://arxiv.org/html/2307.14989v4)  
9. Stabilizer codes for quantum error correction | PennyLane Demos, accessed on November 24, 2025, [https://pennylane.ai/qml/demos/tutorialstabilizercodes](https://pennylane.ai/qml/demos/tutorial_stabilizer_codes)  
10. Linear code \- Wikipedia, accessed on November 24, 2025, [https://en.wikipedia.org/wiki/Linearcode](https://en.wikipedia.org/wiki/Linear_code)  
11. Color code | Error Correction Zoo, accessed on November 24, 2025, [https://errorcorrectionzoo.org/c/color](https://errorcorrectionzoo.org/c/color)  
12. Lecture 12: The Toric Code \- People @EECS, accessed on November 24, 2025, [https://people.eecs.berkeley.edu/\~jswright/quantumcodingtheory24/scribe%20notes/lecture12.pdf](https://people.eecs.berkeley.edu/~jswright/quantumcodingtheory24/scribe%20notes/lecture12.pdf)  
13. Lecture 12: Topological Codes 1 Recap: Toric Code \- People @EECS, accessed on November 24, 2025, [https://people.eecs.berkeley.edu/\~jswright/quantumcodingtheory24/scribe%20notes/lecture13.pdf](https://people.eecs.berkeley.edu/~jswright/quantumcodingtheory24/scribe%20notes/lecture13.pdf)  
14. Toric Code Visualizer, accessed on November 24, 2025, [https://gui.quantumcodes.io/2d](https://gui.quantumcodes.io/2d)  
15. Toric code | IBM Quantum Learning, accessed on November 24, 2025, [https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/quantum-code-constructions/toric-code](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/quantum-code-constructions/toric-code)  
16. The planar surface code vs the toric code \- Quantum Computing Stack Exchange, accessed on November 24, 2025, [https://quantumcomputing.stackexchange.com/questions/33834/the-planar-surface-code-vs-the-toric-code](https://quantumcomputing.stackexchange.com/questions/33834/the-planar-surface-code-vs-the-toric-code)  
17. Graph Theory: Puzzles and Games \- The University of Edinburgh Open Educational Resources, accessed on November 24, 2025, [https://open.ed.ac.uk/graph-theory-puzzles-and-games/](https://open.ed.ac.uk/graph-theory-puzzles-and-games/)  
18. Color Code Skill-Building Puzzle Game Ages 5+, accessed on November 24, 2025, [https://smarttoysandgames.com/products/smartgames-color-code-skill-building-puzzle-game-ages-5-adult](https://smarttoysandgames.com/products/smartgames-color-code-skill-building-puzzle-game-ages-5-adult)  
19. Transversal Surface-Code Game Powered by Neutral Atoms \- arXiv, accessed on November 24, 2025, [https://arxiv.org/html/2506.18979v1](https://arxiv.org/html/2506.18979v1)  
20. QEC : Shor's Nine-Qubit Code \- Qniverse, accessed on November 24, 2025, [https://qniverse.in/docs/qec-shors-nine-qubit-code/](https://qniverse.in/docs/qec-shors-nine-qubit-code/)  
21. The 9-qubit Shor code | IBM Quantum Learning, accessed on November 24, 2025, [https://quantum.cloud.ibm.com/learning/courses/foundations-of-quantum-error-correction/correcting-quantum-errors/shor-code](https://quantum.cloud.ibm.com/learning/courses/foundations-of-quantum-error-correction/correcting-quantum-errors/shor-code)  
22. Strategic LLM Decoding through Bayesian Games \- OpenReview, accessed on November 24, 2025, [https://openreview.net/forum?id=K6ZWCpGrGG](https://openreview.net/forum?id=K6ZWCpGrGG)  
23. Motivation for simulating multiround syndrome extraction circuits for quantum error correction code, accessed on November 24, 2025, [https://quantumcomputing.stackexchange.com/questions/38470/motivation-for-simulating-multiround-syndrome-extraction-circuits-for-quantum-er](https://quantumcomputing.stackexchange.com/questions/38470/motivation-for-simulating-multiround-syndrome-extraction-circuits-for-quantum-er)  
24. Concatenated error correction code \- Wikipedia, accessed on November 24, 2025, [https://en.wikipedia.org/wiki/Concatenatederrorcorrectioncode](https://en.wikipedia.org/wiki/Concatenated_error_correction_code)  
25. Looking for riddles related to error correcting codes. Here's one I know: : r/mathriddles, accessed on November 24, 2025, [https://www.reddit.com/r/mathriddles/comments/10e8or0/lookingforriddlesrelatedtoerrorcorrecting/](https://www.reddit.com/r/mathriddles/comments/10e8or0/looking_for_riddles_related_to_error_correcting/)  
26. Hamming code \- Wikipedia, accessed on November 24, 2025, [https://en.wikipedia.org/wiki/Hammingcode](https://en.wikipedia.org/wiki/Hamming_code)  
27. Hats and Hamming Codes \- Point at Infinity, accessed on November 24, 2025, [https://pointatinfinityblog.wordpress.com/2016/09/08/hats-and-hamming-codes/](https://pointatinfinityblog.wordpress.com/2016/09/08/hats-and-hamming-codes/)  
28. Reed–Solomon error correction \- Wikipedia, accessed on November 24, 2025, [https://en.wikipedia.org/wiki/Reed%E2%80%93Solomonerrorcorrection](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction)  
29. A Simplified Step-by-Step Decoding Algorithm for Parallel Decoding of Reed–Solomon Codes | IEEE Journals & Magazine | IEEE Xplore, accessed on November 24, 2025, [https://ieeexplore.ieee.org/document/4237464/](https://ieeexplore.ieee.org/document/4237464/)  
30. Game-Theoretic Discovery of Quantum Error-Correcting Codes Through Nash Equilibria, accessed on November 24, 2025, [https://arxiv.org/html/2510.15223v1](https://arxiv.org/html/2510.15223v1)  
31. Error correction mechanisms \- (Game Theory) \- Vocab, Definition, Explanations | Fiveable, accessed on November 24, 2025, [https://fiveable.me/key-terms/game-theory/error-correction-mechanisms](https://fiveable.me/key-terms/game-theory/error-correction-mechanisms)  
32. Error Correction Games for Writing \- Ken Lackman, accessed on November 24, 2025, [https://www.kenlackman.com/files/WritingErrorsBook10A4.pdf](https://www.kenlackman.com/files/WritingErrorsBook10A4.pdf)  
33. Discovering highly efficient low-weight quantum error-correcting codes with reinforcement learning \- arXiv, accessed on November 24, 2025, [https://arxiv.org/html/2502.14372v1](https://arxiv.org/html/2502.14372v1)  
34. Time limit on puzzle games: yea or nay? \- Game Development Stack Exchange, accessed on November 24, 2025, [https://gamedev.stackexchange.com/questions/17100/time-limit-on-puzzle-games-yea-or-nay](https://gamedev.stackexchange.com/questions/17100/time-limit-on-puzzle-games-yea-or-nay)  
35. Concatenated codes \- Scholarpedia, accessed on November 24, 2025, [http://www.scholarpedia.org/article/Concatenatedcodes](http://www.scholarpedia.org/article/Concatenated_codes)  
36. Safe and Nested Subgame Solving for Imperfect-Information Games \- NIPS papers, accessed on November 24, 2025, [https://papers.nips.cc/paper/6671-safe-and-nested-subgame-solving-for-imperfect-information-games](https://papers.nips.cc/paper/6671-safe-and-nested-subgame-solving-for-imperfect-information-games)  
37. \[1707.02026\] A Nested Attention Neural Hybrid Model for Grammatical Error Correction, accessed on November 24, 2025, [https://arxiv.org/abs/1707.02026](https://arxiv.org/abs/1707.02026)  
38. Color Code Visual Perception Stack & Solve Game \- Toys"R"Us, accessed on November 24, 2025, [https://www.toysrus.com/products/color-code](https://www.toysrus.com/products/color-code)