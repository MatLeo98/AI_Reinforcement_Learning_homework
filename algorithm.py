from collections import defaultdict
from utilities import ROWS, COLS, EPSILON, ALPHA, GAMMA, boundary_wall, inner_walls, is_beater
import itertools
import random

states = list(itertools.product(ROWS, COLS, [0, 1]))  # 0: beater not yet collected, 1: beater collected
actions = ["U", "D", "L", "R"]
rewards = {"oven": 100, "beater": 50, "not_oven": -100, "wall": -200}
Q = defaultdict(lambda: defaultdict(float))

# Populate Q with zeros
for r in ROWS:
    for c in COLS:
        Q[r][c] = 0.0


def policy(sp, ep):
    print('The training is started...\n')
    for attempt in range(100000):  # Train the agent in the world with a large number of attempts
        print('\rAttempts: {}'.format(attempt), end='')
        s = sp
        e = ep
        p_path = [s]
        p_actions = []
        while s != e:
            a = next_action(s)
            next_s, reward = step(s, a)
            q_table_update(s, a, next_s, reward)
            p_path.append(next_s)
            p_actions.append(a)
            s = next_s
    p = list(itertools.zip_longest(p_path, p_actions, fillvalue=None))
    return p


def next_action(state):
    if random.uniform(0, 1) < EPSILON:
        return random.choice(actions)
    else:
        return max(actions, key=lambda action: Q[state][action])


def step(state, action):
    row, column, beater = state
    if (row, column, action) in inner_walls():
        return state, rewards['wall']

    # fare switch case
    if action == 'U':
        row -= 1
    elif action == 'D':
        row += 1
    elif action == 'L':
        column -= 1
    elif action == 'R':
        column += 1

    if (row, column) == (3, 4):
        if action == 'L':
            column -= 1
        if action == 'R':
            column += 1

    if boundary_wall(row, column):
        return state, rewards["wall"]

    if (row, column) == (0, 7):
        if beater == 1:
            return (row, column, beater), rewards["oven"]
        else:
            return (row, column, beater), rewards["not_oven"]

    if is_beater(row, column) and not beater:
        return (row, column, 1), rewards["beater"]
    else:
        return (row, column, beater), rewards["not_oven"]


def q_table_update(state, action, next_state, reward):
    old_value = Q[state][action]
    max_move = max(actions, key=lambda action: Q[next_state][action])
    new_q = Q[next_state][max_move]
    Q[state][action] = old_value + ALPHA * (reward + (GAMMA * new_q) - old_value)
