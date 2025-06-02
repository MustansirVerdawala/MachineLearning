# Deep Reinforcement Learning Agent for Bullet Dodging

---

## Project Overview

This project implements a Deep Q-Learning (DQL) agent designed to autonomously dodge enemy bullets in a custom 2D game environment. Leveraging state-of-the-art deep reinforcement learning techniques with Python and TensorFlow, the agent learns optimal movement policies by interacting with the environment and receiving feedback based on survival and evasion success.

---

## Key Features

- **Deep Q-Learning Implementation:** Utilizes TensorFlow to build and train a neural network that approximates Q-values for state-action pairs, enabling the agent to make intelligent movement decisions.
- **2D Game Environment:** The agent operates within a real-time 2D Unity game developed by a collaborator, responding dynamically to incoming threats.
- **Cross-Platform Communication:** Implements a robust TCP socket connection facilitating real-time command transmission from the Python-based learning agent to the Unity game environment.
- **Collaborative Development:** Coordinated development efforts using GitHub for version control and code integration.
- **Performance Optimization:** The agent progressively improves its bullet-dodging policy through reward-based learning, achieving significant success in navigating complex attack patterns.

---

## Technical Details

- **Programming Languages & Frameworks:** Python 3.x, TensorFlow, Unity (C#)
- **Architecture:**
  - Neural network model for Q-value approximation
  - Experience replay buffer for stable training
  - Epsilon-greedy strategy for balancing exploration and exploitation
- **Communication:** TCP sockets used for seamless integration between the Python training environment and Unity game engine.
- **Training Process:** The agent observes the game state, selects actions, receives rewards, and updates its policy iteratively.

---

## Collaboration

- This project was developed collaboratively with Jacky Zhang, combining expertise in game development and deep reinforcement learning. GitHub was utilized for source control, branch management, and issue tracking throughout the project lifecycle.

## Results

- The DQL agent learned effective evasive maneuvers to avoid incoming enemy bullets.
- Demonstrated steady improvement in survival time and evasion success rate.
- Real-time interaction between Python agent and Unity game allowed for seamless training and testing cycles.
