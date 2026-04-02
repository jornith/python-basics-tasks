# Format full name with optional middle name

def format_name(first, last, middle=None):
    if middle:
        return f"{last} {first} {middle}"
    return f"{last} {first}"
