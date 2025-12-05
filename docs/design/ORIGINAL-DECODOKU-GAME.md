# The Original Decodoku Game

## Overview

[Decodoku](https://en.wikipedia.org/wiki/Decodoku) is a pioneering quantum error correction game created by Dr. James Wootton, a quantum physicist at the University of Basel, Switzerland. The project represents one of the first serious attempts to use gaming as a platform for both education and research in quantum computing.

## The Name: Decodoku

The name "**Decodoku**" is a clever portmanteau that combines:

- **Decode** - referring to the decoding of quantum errors in error correction
- **Sudoku** - the famous Japanese number puzzle game

The formula is simple: **Decoding + Sudoku = Decodoku**

In time-honored quantum computing tradition, we've replaced the "u" with a "q" because **it rhymes**! This playful linguistic twist reflects both the scientific rigor and the approachable, fun nature of the project. The name perfectly captures the essence of making quantum error correction as accessible and engaging as a Sudoku puzzle.

## Creator: Dr. James Wootton

Dr. James Wootton is a quantum physicist at the University of Basel, funded by the [NCCR QSIT](https://nccr-qsit.ethz.ch/technology-transfer/qstarter/current-projects/quantum-error-correction--the-game1.html) (National Centre of Competence in Research - Quantum Science and Technology). He is passionate about using games for education in quantum computing and beyond.

### Wootton's Philosophy on Games and Quantum Education

James Wootton has a unique vision for how games can democratize quantum computing education and research. His philosophy can be summarized in several key principles:

#### 1. Making the Public into Scientists

As Wootton explains in his writings, Decodoku is about **letting the public become scientists themselves**. Rather than simply educating people about quantum computing, the project enables anyone to actively contribute to cutting-edge research. By playing a game no more complicated than 2048 or Threes, players could help design the error correction systems for real quantum computers.

#### 2. Demystifying Quantum Computing

Wootton recognizes that quantum computing can seem like an "arcane art," much as normal programming once did. He believes that [games can "illustrate the algorithm and programming principles involved"](https://decodoku.medium.com/games-computers-and-quantum-84bfdd2c0fe0), making quantum concepts accessible to everyone.

#### 3. Two-Way Street: Games ↔ Quantum

Wootton frames his work around two complementary questions:

- **"What can games do for quantum computing?"** - Focus on education and research contribution
- **"What can quantum computing do for games?"** - Exploring quantum advantages in game mechanics

#### 4. Quantum Games as Educational Tools

According to Wootton, [game mechanics could be based on important quantum phenomena](https://decodoku.medium.com/why-we-need-to-make-quantum-games-6f8c7bc4ace7), allowing players a starting point to learn about the physics behind quantum computers. Games provide an intuitive, hands-on way to understand abstract quantum concepts.

## The Game

### Purpose and Research Goals

[Decodoku seeks to let users get hands-on with cutting-edge quantum research](https://arxiv.org/abs/1712.09649) through a set of simple puzzle games. The design is explicitly based on the problem of decoding **qudit variants of surface codes**, presented such that it can be tackled by players with no prior knowledge of quantum information theory.

Crucially, **methods devised by the players to solve the puzzles can directly be incorporated into decoding algorithms** for real quantum computation. This is true citizen science - the gameplay directly contributes to advancing quantum computing technology.

### Game Mechanics

The game presents quantum error correction challenges in a format similar to casual mobile puzzle games:

- **Grid-based puzzles** with numbers
- Gameplay style similar to **2048, Threes!, or Sudoku**
- Players solve puzzles by identifying and correcting error patterns
- No prior quantum physics knowledge required

Though the apps may look like simple games to casual users, they are actually **a starter kit for quantum error correction research**. The game translates the complex mathematical problem of quantum error correction into an intuitive visual puzzle.

### Platforms and Availability

Decodoku has been released on multiple platforms:

- [Web version](https://decodoku.itch.io/decodoku) (itch.io)
- [iOS App Store](https://apps.apple.com/us/app/decodoku/id1093080064)
- [GitHub repository](https://github.com/decodoku) with source code

## Research Impact

### Scientific Publication

Dr. Wootton published his findings in an [arXiv paper in December 2017](https://arxiv.org/abs/1712.09649) titled "Getting the public involved in Quantum Error Correction." The paper provides:

- A brief overview of novel decoding methods devised by players
- A postmortem analysis of Decodoku versions 1.0-4.1
- Evidence that crowdsourced gaming can contribute to quantum research

### Player Contributions

The game demonstrated the power of human intuition in solving quantum problems:

- **Human players outperformed the researcher**: [One high scorer achieved a score around four times Dr. Wootton's own](https://decodoku.medium.com/what-the-public-taught-me-about-quantum-error-correction-37e8641476ae)
- Players consistently got over 800 points while Wootton struggled to get over 200
- Top players provided explanations of their methods and recorded their gameplay
- These human-developed strategies were then [distilled into improved decoding algorithms](https://decodoku.medium.com/what-the-public-taught-me-about-quantum-error-correction-37e8641476ae)

This proved that the general public, through gameplay, could discover strategies that expert researchers might miss.

## The Qudit Surface Code Connection

Decodoku is based on **qudit variants of surface codes**, a leading approach to quantum error correction:

- **Qudits** (quantum digits) generalize qubits to higher dimensions (d > 2)
- **Surface codes** arrange qudits on a 2D lattice
- The original Decodoku used d=10 qudits, making the puzzle based on base-10 numbers
- Error patterns create "syndromes" that players must decode to find the original errors

This connection to real quantum error correction research makes every game session a potential contribution to quantum computing development.

## Technical Implementation

### Code Repository

The original Decodoku code is available on GitHub:

**Repository**: [https://github.com/quantumjim/decodoku](https://github.com/quantumjim/decodoku)

This repository includes:
- Source code for the game
- Implementation of qudit surface codes
- Decoder algorithms
- Game mechanics

### Building on Decodoku

The code in **this repository** (codoq-quantum-game) builds on the foundation established by James Wootton's original work. We acknowledge and celebrate this heritage by:

- Following the spirit of making quantum error correction accessible through games
- Extending the concept to other quantum codes (Steane, Reed-Muller)
- Focusing on educational value and geometric intuition
- Maintaining the open-source, collaborative ethos

## Evolution: From Decodoku to Codo-Q

### What's Different?

While inspired by the original Decodoku, this project (Codo-Q) takes a different approach:

| Aspect | Original Decodoku | Codo-Q (This Project) |
|--------|-------------------|----------------------|
| **Codes** | Qudit surface codes (d=10) | Steane [[7,1,3]], Reed-Muller [[15,1,3]] |
| **Geometry** | 2D lattice/grid | Fano plane (2D), Tetrahedron (3D) |
| **System** | Qudits (d=10) | Qubits (d=2) |
| **Focus** | Research contribution | Education and visualization |
| **Platform** | Mobile apps, web | Jupyter notebooks, Python |
| **Target Audience** | General public | Students and learners |

### The "Q" in Codo-Q

Following Decodoku's tradition of replacing "u" with "q" (because it rhymes!), we named this project **Codo-Q** (Code + Q) to emphasize:

- The **quantum** nature of error correction
- The focus on **qubits** (d=2) rather than qudits
- Our playful homage to the original name

## Legacy and Influence

### Impact on Quantum Gaming

Decodoku pioneered the field of [quantum gaming for research and education](https://citizensciencegames.com/game-cause-decodoku/). It demonstrated that:

1. Complex quantum concepts can be made accessible through games
2. Non-experts can contribute meaningfully to quantum research
3. Games provide intuition that complements traditional education
4. Citizen science can advance quantum computing

### Inspiration for Future Projects

The success of Decodoku has inspired numerous follow-up projects:

- Educational quantum games at universities
- [Other quantum error correction games](https://github.com/sneakyweasel/genetic-quantum-correction)
- Integration of quantum concepts into game design courses
- Quantum hackathons and game jams

## Why Games Matter for Quantum Education

Drawing from Wootton's philosophy and the Decodoku experience, games are crucial for quantum education because:

### 1. Intuition Over Mathematics

Quantum error correction involves complex linear algebra and probability theory. Games let players develop **intuitive understanding** before diving into the math.

### 2. Learning by Doing

Rather than passively reading about quantum concepts, players **actively solve quantum problems**, leading to deeper understanding and retention.

### 3. Immediate Feedback

Games provide instant feedback on strategy effectiveness, allowing rapid iteration and learning - much faster than traditional research methods.

### 4. Accessibility

Games remove barriers to entry. Anyone with a smartphone or web browser can start exploring quantum computing, regardless of their educational background.

### 5. Motivation and Engagement

Game mechanics (scores, levels, challenges) provide motivation to continue learning and improving, making the educational experience enjoyable.

### 6. Pattern Recognition

Humans excel at visual pattern recognition. Games that translate quantum problems into visual puzzles leverage this strength, often leading to insights that algorithmic approaches miss.

## Connecting to This Project

### Educational Philosophy

Like the original Decodoku, this project (Codo-Q) embraces the philosophy that:

- Quantum error correction should be accessible to all
- Games and interactive visualizations enhance understanding
- Geometric intuition complements mathematical rigor
- Open-source collaboration advances the field

### Building on the Foundation

We acknowledge our debt to James Wootton's pioneering work by:

1. **Maintaining the spirit** of accessible quantum education
2. **Extending the concept** to additional quantum codes with rich geometric structure
3. **Emphasizing visualization** through Fano planes and tetrahedra
4. **Providing educational materials** (notebooks, documentation) for learners
5. **Open-sourcing everything** to enable further innovation

### Different Approach, Same Goal

While Decodoku focused on qudit surface codes and research contribution, Codo-Q focuses on:

- **Qubit stabilizer codes** (Steane, Reed-Muller)
- **Geometric understanding** (projective geometry, polytopes)
- **Educational progression** (from simple to complex)
- **Jupyter-based learning** (interactive notebooks)

Both projects share the ultimate goal: **making quantum error correction understandable, accessible, and fun**.

## Resources and Links

### Original Decodoku

- [Decodoku on Wikipedia](https://en.wikipedia.org/wiki/Decodoku)
- [Play Decodoku (Web)](https://decodoku.itch.io/decodoku)
- [Decodoku iOS App](https://apps.apple.com/us/app/decodoku/id1093080064)
- [GitHub Repository](https://github.com/quantumjim/decodoku)
- [ArXiv Paper: "Getting the public involved in Quantum Error Correction"](https://arxiv.org/abs/1712.09649)

### James Wootton's Writing

- [Games, Computers and Quantum](https://decodoku.medium.com/games-computers-and-quantum-84bfdd2c0fe0)
- [Why we need to make quantum games](https://decodoku.medium.com/why-we-need-to-make-quantum-games-6f8c7bc4ace7)
- [Decodoku in 2017](https://decodoku.medium.com/decodoku-in-2017-e68e63a6d09c)
- [What the public taught me about quantum error correction](https://decodoku.medium.com/what-the-public-taught-me-about-quantum-error-correction-37e8641476ae)
- [The History of Games for Quantum Computers](https://decodoku.medium.com/the-history-of-games-for-quantum-computers-a1de98859b5a)
- [Dr James Wootton on Medium](https://decodoku.medium.com/)

### Interviews and Coverage

- [Interview with Swiss Game Developers Association](https://www.sgda.ch/decodoku-interview-james-wootton/)
- [Citizen Science Games feature](https://citizensciencegames.com/game-cause-decodoku/)
- [Pocket Gamer coverage](https://www.pocketgamer.com/decodoku/decodoku-is-a-new-puzzle-game-with-a-scientific-twist/)
- [University of Basel article](https://www.unibas.ch/en/News-Events/News/Uni-Research/A-playful-approach-to-quantum-computing.html)
- [Quantum Era Podcast transcript](https://podcast.newquantumera.com/51/transcript)

### Related Projects

- [NCCR QSIT page](https://nccr-qsit.ethz.ch/technology-transfer/qstarter/current-projects/quantum-error-correction--the-game1.html)
- [Decodoku GitHub Organization](https://github.com/decodoku)
- [Genetic Algorithm approach to Decodoku](https://github.com/sneakyweasel/genetic-quantum-correction)

## Acknowledgments

This project (Codo-Q: Quantum Error Correction Games) is built on the foundation established by Dr. James Wootton's pioneering Decodoku work. We are grateful for:

- The inspiration to make quantum error correction accessible through games
- The open-source code shared at [github.com/quantumjim/decodoku](https://github.com/quantumjim/decodoku)
- The demonstration that games can contribute to serious quantum research
- The philosophy that quantum computing education should be playful and engaging

**Thank you, James Wootton, for showing us the way!** 🎮⚛️

---

*This document pays tribute to the original Decodoku game and its creator while explaining how our project builds upon and extends that pioneering work in quantum gaming education.*

## Sources

- [Decodoku - Wikipedia](https://en.wikipedia.org/wiki/Decodoku)
- [ArXiv: Getting the public involved in Quantum Error Correction](https://arxiv.org/abs/1712.09649)
- [Decodoku on itch.io](https://decodoku.itch.io/decodoku)
- [Decodoku iOS App](https://apps.apple.com/us/app/decodoku/id1093080064)
- [GitHub: quantumjim/decodoku](https://github.com/quantumjim/decodoku)
- [Citizen Science Games: Decodoku](https://citizensciencegames.com/game-cause-decodoku/)
- [SGDA Interview with James Wootton](https://www.sgda.ch/decodoku-interview-james-wootton/)
- [Medium: Games, Computers and Quantum](https://decodoku.medium.com/games-computers-and-quantum-84bfdd2c0fe0)
- [Medium: Why we need to make quantum games](https://decodoku.medium.com/why-we-need-to-make-quantum-games-6f8c7bc4ace7)
- [Medium: Distilling the genius of human players](https://decodoku.medium.com/what-the-public-taught-me-about-quantum-error-correction-37e8641476ae)
