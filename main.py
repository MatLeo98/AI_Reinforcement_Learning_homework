from algorithm import policy
from utilities import path_for_beater, path_for_oven

start_position = (1, 5, 0)
end_position = (0, 7, 1)

# Starts the training and save the best policy
p = policy(start_position, end_position)

# Prints the path to reach the beater
path_for_beater(p)

# Prints the path to reach the oven
path_for_oven(p)
