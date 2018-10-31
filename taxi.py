import numpy as np
import gym
import random

env = gym.make("Taxi-v2")
env.render()

action_size = env.action_space.n
print(action_size)

state_size = env.observation_space.n
print(state_size)

qtable = np.zeros((state_size, action_size))
print(qtable)

total_episodes = 50000
total_test_episodes = 100
max_steps = 99

learning_rate = 0.7
gamma = 0.618

epsilon = 1.0
max_epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.01

for episode in range(total_episodes):
    state = env.reset()
    step = 0
    done = False
    
    for step in range(max_steps):
        
        exp_exp_tradeoff = random.uniform(0,1)
        # take max Q value if random number is less than epilson
        if exp_exp_tradeoff > epsilon:              
            action = np.argmax(qtable[state,:])           
         
        else:
            action = env.action_space.sample()
        
        # Update from game
        new_state, reward, done, info = env.step(action)           
        
        #Update Q(s, a):= Q(s, a) + lr*[R[s,a] + gamma*max[s',a']-Q(s,a)]
        qtable[state, action] = qtable[state, action] + learning_rate*(reward 
                                    + gamma*np.max(qtable[new_state, :])-qtable[state, action])
        
        state = new_state
        
        if done == True:
            break
            
    episode += 1
    
    # Decaying epilson so to exploit rather than explore      
    epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode) 
env.reset()
rewards = []

# Play game
for episode in range(total_test_episodes):
    state = env.reset()
    step = 0
    done = False
    total_rewards = 0
    print("**************************************")
    print("Episode", episode)
    
    for step in range(max_steps):
        env.render()
        
        action = np.argmax(qtable[state,:])
        
        new_state, reward, done, info = env.step(action)
        
        total_rewards += reward
        
        if done:
            rewards.append(total_rewards)
            print("Score", total_rewards)
            break
        state = new_state
env.close()
print("Score over time: " + str(sum(rewards)/total_test_episodes))
