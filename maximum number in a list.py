def find_repeated_values(lst):
    seen = set()
    repeated = set()
    
    for item in lst:
        if item in seen:
            repeated.add(item)
        else:
            seen.add(item)
    
    return list(repeated)

# Example usage:
my_list = [1, 2, 3, 4, 2, 5, 6, 7, 8, ]
repeated_values = find_repeated_values(my_list)
print(repeated_values)



