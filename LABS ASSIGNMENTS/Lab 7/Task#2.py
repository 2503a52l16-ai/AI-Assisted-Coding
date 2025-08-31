def sort_list(data):
    def safe_key(x):
        if isinstance(x, int):
            return (0, x)  # sort integers before strings
        try:
            iv = int(x)
            return (0, iv)
        except:
            return (1, str(x).lower())  # sort strings after numbers
    return sorted(data, key=safe_key)

items = [3, "apple", 1, "banana", 2]
print(sort_list(items))
