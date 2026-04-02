# Count positive, negative and zero values in a list

def count_signs(numbers):
    pos = sum(1 for n in numbers if n > 0)
    neg = sum(1 for n in numbers if n < 0)
    zero = sum(1 for n in numbers if n == 0)
    print(f"Positive: {pos}, Negative: {neg}, Zero: {zero}")
    