import random
import numpy as np
from collections import deque
from keras.models import Sequential  # type: ignore
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout, BatchNormalization # type: ignore
from keras.optimizers import Adam # type: ignore

filters = 32

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=500)
        self.gamma = 0.9  # discount rate
        self.epsilon = 1  # exploration rate
        self.epsilon_min = 0.05
        self.epsilon_decay = 0.998
        self.learning_rate = 0.001
        self.model = self._build_model()
        self.target_model = self._build_model()
        self.update_target_model()

    def _build_model(self):
        # Neural Net for Deep-Q learning Model
        model = Sequential()
        model.add(Conv2D(filters, (8, 8), strides=4, activation='relu', input_shape=(512, 512, 4)))
        model.add(Conv2D(filters * 2, (4, 4), strides=2, activation='relu'))
        model.add(Conv2D(filters * 2, (3, 3), strides=1, activation='relu'))
        model.add(Flatten())  # Flatten the output from the convolutional layers
        model.add(Dense(128, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))
        return model

    def update_target_model(self):
        # Copy weights from model to target_model
        self.target_model.set_weights(self.model.get_weights())

    def memorize(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        state = np.reshape(state, (1, *self.state_size))  # Ensure state is in batch format (1, 512, 512, 4)
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state, verbose=0)
        return np.argmax(act_values[0])  # Returns action
    
    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            state = np.reshape(state, (1, *self.state_size))  # Reshape to (1, 512, 512, 4)
            next_state = np.reshape(next_state, (1, *self.state_size))  # Reshape to (1, 512, 512, 4)
            
            target = self.model.predict(state, verbose=0)
            if done:
                target[0][action] = reward
            else:
                t = self.target_model.predict(next_state, verbose=0)[0]
                target[0][action] = reward + self.gamma * np.amax(t)
            
            self.model.fit(state, target, epochs=1, verbose=0)
        
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)
