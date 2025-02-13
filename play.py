from DQNAgent import DQNAgent
from interface import interface
import numpy as np    
# from time import sleep 

state_size = [512, 512, 4] 
action_size = 9
actions={0:'a', 1:'w,a', 2:'w', 3:'w,d', 4:"d", 5:"s,d", 6:'s', 7:'s,a'}
    
interface=interface()

agent = DQNAgent(state_size, action_size)

agent.load("TrainedModel.weights.h5")
print('Agent Loaded')

done = False 

interface.initialize()
print('Environment Initalized')
    
state, health, timeAlive, pScore, cEnemyDist, velocity=interface.fetchInput()
    
state = np.reshape(np.array(state), state_size)
done=False

while True:
    # sleep(2.5-process_time()+start)
    # start=process_time()
    action = agent.act(state)
    if action<8:
        interface.keyPress(actions[action])
    # interface.keyPress(actions[1])
    next_state, newHealth, _, _, _, _= interface.fetchInput()

    if newHealth<=0:
        done=True

    next_state = np.reshape(np.array(next_state), state_size)
    state = next_state
    
    if done:
        #print("score: {}" .format(pScore))
        break