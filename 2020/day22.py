from collections import deque

# f = open('testin.txt')
f = open('day22in.txt')
lines = [line.strip() for line in f.readlines()]

i = lines.index('')

deck1 = deque(map(int, lines[1:i]))
deck2 = deque(map(int, lines[i+2:]))

# print("Deck 1:", deck1)
# print("Deck 2:", deck2)

while(len(deck1) != 0 and len(deck2) != 0):
    c1 = deck1.popleft()
    c2 = deck2.popleft()

    if c1 > c2:
        deck1.append(c1)
        deck1.append(c2)
    else:
        deck2.append(c2)
        deck2.append(c1)


    # print("Next round:")
    # print("Deck 1:", deck1)
    # print("Deck 2:", deck2)

def score(deck):
    return sum([i*j for i,j in zip(deck, reversed(range(1,len(deck) + 1)))])

print('Ans 1: ', score(deck1) + score(deck2))


# Part 2

def state_string(deck1, deck2):
    return str(deck1) + str(deck2)

def recursive_combat(deck1, deck2, depth):
    """
    If depth > 0, returns subgame winner (1 or 2)
    If depth == 0, returns winning player's score
    """
    memory = []

    while len(deck1) != 0 and len(deck2) != 0:
        # Beginning of round

        # Check if config was previously encountered
        state_str = state_string(deck1, deck2)
        if state_str in memory:
            # print('Detected round repetition!')
            return 1
        else:
            memory.append(state_str)

        c1 = deck1.popleft()
        c2 = deck2.popleft()

        # Determine round winner
        round_winner = 0

        if len(deck1) >= c1 and len(deck2) >= c2:
            # Launch recursive combat to determine round winner
            subdeck1 = deque(list(deck1)[0:c1])
            subdeck2 = deque(list(deck2)[0:c2])
            # print(f'Deck1: {deck1}, Deck2: {deck2}')
            # print(f'C1: {c1}, C2: {c2}')
            # print(f'Launching recursive_combat({subdeck1}, {subdeck2}, {depth+1}) to determine round-winner')        
            round_winner = recursive_combat(subdeck1, subdeck2, depth+1)

        else:
            round_winner = 1 if c1 > c2 else 2

        if round_winner == 1:
            deck1.append(c1)
            deck1.append(c2)
        else:
            deck2.append(c2)
            deck2.append(c1)

    # end of subgame

    # return condition
    if depth > 0:
        # This is a subgame. Return the winner (player with all cards)
        return 1 if len(deck1) != 0 else 2 
    if depth == 0:
        # print('Deck1: ', deck1)
        # print('Deck2: ', deck2)
        # This is the main game. Return winner's score
        return score(deck1) + score(deck2)


# reload
i = lines.index('')
deck1 = deque(map(int, lines[1:i]))
deck2 = deque(map(int, lines[i+2:]))

print('Ans 2:', recursive_combat(deck1, deck2, 0))
