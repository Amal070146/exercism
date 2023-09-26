def convert(n):
    result = ""
    
    # Check for factors and add respective sound to result
    if n % 3 == 0:
        result += "Pling"
    if n % 5 == 0:
        result += "Plang"
    if n % 7 == 0:
        result += "Plong"
    
    # If no factors found, return the number itself as a string
    if result == "":
        return str(n)
    return result
