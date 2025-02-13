from DQNAgent import DQNAgent
from interface import interface
import numpy as np    
import matplotlib.pyplot as plt

Episodes = 2000

state_size = [512, 512, 4] 
action_size = 8
actions={0:'a', 1:'w,a', 2:'w', 3:'w,d', 4:"d", 5:"s,d", 6:'s', 7:'s,a'}

interface = interface()

agent = DQNAgent(state_size, action_size)

scores = []

#agent.load('TrainedModel.weights.h5')

print('Agent Initialized')
done = False 
batch_size = 50

interface.initialize()
print('Environment Initialized')

# Initialize plot
plt.ion()  # Turn on interactive mode for real-time plotting
fig, ax = plt.subplots()
x_values = []
y_values = []

for e in range(1, Episodes+1):
    print(f'Episode: {e}')
    
    interface.reset()
    
    state, health, timeAlive, pScore, cEnemyDist, velocity = interface.fetchInput()
        
    state = np.reshape(np.array(state), state_size)
    done = False
    reward = -1

    while True:
        action = agent.act(state)
        interface.keyPress(actions[action])

        next_state, newHealth, newTimeAlive, newPScore, newCEnemyDist, velocity = interface.fetchInput()

        if newHealth < 100:
            done = True
        else:
            if newHealth < health:
                reward -= 10* (health - newHealth)
            if velocity< 150:
                reward -= 5
            #if newPScore > pScore:
            #    reward += (newPScore - pScore)
            if (newCEnemyDist)>70:
                reward -= 1
            reward+=(newTimeAlive-timeAlive)
            
        health = newHealth
        timeAlive = newTimeAlive
        pScore = newPScore

        next_state = np.reshape(np.array(next_state), state_size)
        agent.memorize(state, action, reward, next_state, done)
        state = next_state
                
        if done:
            agent.update_target_model()
            print("episode: {}/{}, score: {}, e: {:.2f}"
                  .format(e, Episodes, pScore, agent.epsilon))
            
            _, health, _, _, _, _ = interface.fetchInput()
            
            while health>0:
                _, health, _, _, _, _ = interface.fetchInput()
                pass
            
            break
        
    scores.append(pScore)

    # Add episode number and score to plot
    x_values.append(e)
    y_values.append(pScore)

    ax.clear()  # Clear previous plot
    ax.plot(x_values, y_values, marker='o', color='b')  # Plot scores
    ax.set_title("Score Progression")
    ax.set_xlabel("Episodes")
    ax.set_ylabel("Score")
    plt.pause(0.1)  # Pause to update the plot
    plt.show()

    if len(agent.memory) > batch_size:
        print('Training')
        agent.replay(batch_size)
        print('Training Complete')

    plt.ioff()  # Turn off interactive plotting
    plt.show()  # Show the final plot after all episodes are complete

agent.save("TrainedModel.weights.h5")
