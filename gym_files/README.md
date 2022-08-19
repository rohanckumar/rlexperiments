# Where It All Goes

## __init__.py_env

Rename to __init__.py and save in ~/anaconda3/envs/spinningup/lib/python3.6/site-packages/gym/envs


## __init__.py_box2d

Rename to __init__.py and save in ~/anaconda3/envs/spinningup/lib/python3.6/site-packages/gym/envs/box2d

## lunar_lander.py

Save in ~/anaconda3/envs/spinningup/lib/python3.6/site-packages/gym/envs/box2d

# Experimenting with extremely high step count

    Go to ~/anaconda3/envs/spinningup/lib/python3.6/site-packages/gym/envs/box2d/lunar_lander.py file

    Adjust values in shaping to remove rewards given for one leg touching the ground(Last 2 elements of the equation)