# NEAT Race: NeuroEvolution of Augmenting Topologies for Autonomous Racing Agents

---

## Overview

**NEAT Race** is a cutting-edge implementation of the NEAT (NeuroEvolution of Augmenting Topologies) algorithm applied to autonomous racing agents within a simulated environment. This project demonstrates the power of neuroevolution to evolve both the structure and weights of neural networks, enabling agents to learn to navigate complex race tracks autonomously through evolutionary processes.

---

## Key Features

- **NEAT Algorithm Implementation:** Full custom implementation of NEAT, including speciation, fitness sharing, mutation (both structural and parametric), and crossover.
- **Evolving Neural Network Topologies:** Unlike fixed-architecture neural networks, the topology dynamically evolves, allowing the discovery of optimal network structures.
- **Autonomous Racing Simulation:** Agents controlled by evolved neural networks learn to navigate race tracks by processing sensor inputs and outputting steering and acceleration commands.
- **Genetic Diversity Preservation:** Speciation protects innovative structures by grouping similar networks, ensuring a balanced evolutionary search.
- **Configurable Parameters:** Extensive parameterization for population size, mutation rates, crossover probability, speciation thresholds, and more, enabling fine-tuning and experimentation.
- **Visualization & Monitoring:** Real-time visualization of agent performance, track navigation, and evolutionary progress metrics.
- **Robust Fitness Function:** Custom fitness evaluation based on distance traveled, time efficiency, collision avoidance, and track adherence.

---

Technical Highlights

- **Dynamic Topology Evolution:** New neurons and connections are added through mutations, allowing network complexity to grow naturally with task demands.
- **Speciation & Fitness Sharing:** Innovative genomes are protected in niches to prevent premature convergence and encourage exploration.
- **Multi-sensor Input Processing:** Agents receive distance sensor inputs around the car perimeter, enabling complex environment perception.
- **Efficient Crossover:** Offspring networks combine genes from parents while maintaining valid structures.
- **Performance Logging:** Detailed logs record fitness progression, species diversity, and network topologies over generations.

Results & Benchmarks

- Agents successfully learn to navigate complex race tracks with sharp turns and obstacles.
- Progressive improvement in lap times and collision avoidance observed over generations.
- Visualizations show diverse network architectures evolving to optimize sensor interpretation and control outputs.
