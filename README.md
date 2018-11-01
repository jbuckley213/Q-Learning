# Taxi Game Q-Learning

Overview
=============
A project that trains a taxi to pick up a passenger and drop off to a location using a type of reinforcment learning called Q learning. 

Dependencies
============

* Numpy (http://www.numpy.org/)
* Gym   (https://gym.openai.com)

Using pip to install any missing dependencies

Game Rules
============
The game is from open AI gym. The game has 6 actions which are move north, south, east and west, and "pick up" and "drop off". The rewards are -1 for each action, +20 for delivering passeneger and -10 for illegal "pick up" and "drop off". Rendering blue: passenger, megenta: destination, yellow: empty taxi, green: full taxi, other letter: locations.

Q Learning
============
The Bellman equation is used to update Q to learn how to play the taxi game. 
Q(s, a):= Q(s, a) + lr*[R[s,a] + gamma*max[s',a']-Q(s,a)] where s is state, a is action, lr is learning rate, R is reward, gamma is the discount rate, s' is new state, a' next action.

The epsilon rate is the explore and exploit rate. As epsilon decrement the model tends to exploit the highest reward for the current state rather than exploring random actions. 

Results
===========
After preforming for 100 episodes the model obtained an average score of 8.72. This is a positive score as the average number of actions per episode is 12.64. There are no illegal "pick ups" or "drop offs" according to the rewards array. This is a satisfactory result but further investigation is needed whether the game can be played more efficiently and achieve a higher score. 

