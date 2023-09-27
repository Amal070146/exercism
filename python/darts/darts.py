def score(x, y):
    # Calculate the distance from the center
    distance = (x**2 + y**2)**0.5
    
    # Determine the score based on the distance
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0
