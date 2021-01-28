def process_numbers(arr):
    if type(arr) == list:
        l = [str(i) for i in arr]
        return sorted([int(i) for i in l if i.isdigit()])
    else:
        return []

def process_names(arr):
    if type(arr) == list:
        l = [str(i) for i in arr]
        return sorted([i for i in l if i.isalpha()])
    else:
        return []