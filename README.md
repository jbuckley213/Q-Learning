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
The Q learning algorithim is used to learn to play the taxi game. Q(s, a):= Q(s, a) + lr*[R[s,a] + gamma*max[s',a']-Q(s,a)] where s is state, a is action, lr is learning rate, R is reward, gamma is the discount rate, s' is new state, a' next action.  

