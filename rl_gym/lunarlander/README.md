# Lunar Lander Customized

This is a customized version of the standard lunar lander described in the OpenAI Gym. 
Our aim is to show how side channel rewards can be given to the modelt to perform better.

Here we train it on 2 different environments, one that only takes into consideration the movement of the rover and another that takes into account the fuel consumption.

## Important variables to note

 - target_episode: This defines the episode after which we switch to the new environment
 - env: The initial environment
 - env_2: The new environment
 - outdir: This defines the location where the result is to be stored, give a new location each time you run to prevent it from overwriting the previous values

## Note

You can uncomment the env.render() and env_2.render() at lines 187 and 191.
This will allow us to see each episode as they are happening but it may delay the training by a few seconds in each episode(Time needed to actually play the video).