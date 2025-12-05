# Gottesman Protocol game. 

This is a single HTML file containing the `Three.js` 3D engine, the 4D math to generate the 600-cell, and the game logic for the stabilizer code simulation.

### The Implementation Plan
1.  **4D Engine:** I will implement a custom 4D-to-3D projection system. This calculates the 120 vertices of the 600-cell in 4D space and projects them down to 3D based on a 4D camera position.
2.  **Visuals:**
    * **Qubits (Vertices):** Rendered as glowing nodes. Blue = Healthy, Red = Error.
    * **Stabilizers (Cells):** I won't render all 600 tetrahedra as it would be opaque. Instead, I will only render "Active Syndromes"—stabilizers that detect an error—as glowing wireframe shapes connecting the affected qubits.
3.  **Controls:**
    * **Mouse:** Rotates the 3D view (Standard Orbit).
    * **Sliders:** Rotate the object in 4D planes (XW, YW, ZW), creating the "morphing" shadow effect.
4.  **Game Loop:**
    * **Inject Noise:** Randomly flips qubits.
    * **Calculate Syndromes:** Checks parity of tetrahedra.
    * **Player Fix:** Click nodes to flip them back.

## `gottesmann-game.html`.  
See [`gottesmann-game.html`](../../frontend/games/gottesmann-game.html)