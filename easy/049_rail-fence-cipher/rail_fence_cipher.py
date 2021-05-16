from collections import deque


def encode(message: str, rails: int):
    encoded_matrix = [['.'] * len(message) for _ in range(rails)]

    # Create a que of pattern of rail movement
    que = deque(list(range(rails)) + list(range(rails-2, 0, -1)))
    # For a rail of 3, the que pattern will be [0,1,2] + [1] = [0,1,2,1]
    # See this example to understand it
    #    W . . . E . . . C . . . R . . . L . . . T . . . E
    #    . E . R . D . S . O . E . E . F . E . A . O . C .
    #    . . A . . . I . . . V . . . D . . . E . . . N . .

    # Fill the empty matrix with the message by following the rail
    for index, char in enumerate(message):
        encoded_matrix[que[0]][index] = char
        que.rotate(-1)

    return "".join(char for row in encoded_matrix for char in row if char != '.')


def decode(encoded_message: str, rails: int):
    decoded_text = ""
    length = len(encoded_message)

    decoded_matrix = [['.'] * length for _ in range(rails)]
    que1 = deque(list(range(rails)) + list(range(rails-2, 0, -1)))
    
    # Turn the dots across decoded_matrix to question-mark to mark the message's rail
    for i in range(length):
        decoded_matrix[que1[0]][i] = '?'
        que1.rotate(-1)
    # For a rail of 3 and length of 25, decoded_matrix is now become like this
    #    ? . . . ? . . . ? . . . ? . . . ? . . . ? . . . ?
    #    . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
    #    . . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .

    # Turn all question marks to characters. Changes are made to each row in turn.
    que2 = deque(list(encoded_message))
    for row in decoded_matrix:
        for index, char in enumerate(row):
            if char == "?":
                row[index] = que2.popleft()
    
    # Rotate que1 so it turns to 'default' (que starts with 0)
    que1.rotate(-que1.index(0))

    # Read the message inside decoded_matrix by following the message's rail
    for i in range(length):
        decoded_text += decoded_matrix[que1[0]][i]
        que1.rotate(-1)
    
    return decoded_text
    