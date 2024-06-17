# Task1

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

def common_member (submitted, attended):
    submitted = ["Alice", "Bob", "Charlie", "David"]
    attended = ["Charlie", "Eve", "Alice", "Frank"]
    result = [member for member in submitted if member in attended]
    return result

print(common_member(submitted, attended))


# Task2

print(submitted is attended)

# Task3

def remove_member (submitted, attended):
    submitted = ["Alice", "Bob", "Charlie", "David"]
    attended = ["Charlie", "Eve", "Alice", "Frank"]
    for member in attended:
        if member not in submitted:
            attended.remove(member)
        else:
            pass
    print(attended)

print(remove_member(submitted, attended))
