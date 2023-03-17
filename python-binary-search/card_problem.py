def locate_card(cards, query):
    position = 0            # Create position variable with value 0

    while True:             # Set up a loop for repetition
        if cards[position] == query:        # Check if element at current position matches the query
            return position                 # Answer found, return and exit
        position += 1                       # If it doesn't match, increment the position

        if position == len(cards):          # If we have reached the end of the list, return -1 and exit the loop
            return -1
