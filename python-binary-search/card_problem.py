def locate_card(cards, query):
    position = 0            # Create position variable with value 0

    while position < len(cards):             # Set up a loop for repetition
        if cards[position] == query:        # Check if element at current position matches the query
            return position                 # Answer found, return and exit
        position += 1                       # If it doesn't match, increment the position
    return -1                           # If we have reached the end of the list, return -1 and exit the loop



deck = [13, 24, 54, 3, 6, 1, 8, 53, 12, 32, 5]

print(locate_card(deck, 2))