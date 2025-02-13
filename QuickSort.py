def quick_sort(sequence):
    lower = []
    greater = []
    if len(sequence) < 1:
        return sequence
    else:
        pivot = sequence.pop()


    for item in sequence:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item)

    return quick_sort(lower) + [pivot] + quick_sort(greater)
print(quick_sort([2,11,4,8,0,1]))