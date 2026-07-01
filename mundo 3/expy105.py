def grades(*num, state=False):
    '''Grades calculate the total, biggest and smaller numbers, average and can also tell if its a passing or failing grade from the values num
    that have been typed
    All values are stored in a Dictionary
    Num: numerics values
    state: Opcional, Determines to show or not the state of the student
    return: Returns a Dictionary with all the values calculated by grade'''
    data = {}
    numbers = []
    total = 0
    for value in num:
        total += 1
        numbers.append(value)
    data['Total'] = total
    data['Maior'] = max(numbers)
    data['Menor'] = min(numbers)
    data['Media'] = sum(numbers) / total
    if state:
        if data['Media'] >= 6:
            data['Situacao'] = 'Boa'
        else:
            data['Situacao'] = 'Reprovado'
    return data

answer = grades(8.5, 5.5, 7, 4, state=True)
print(answer)