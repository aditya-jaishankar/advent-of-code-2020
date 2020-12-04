from utils import read_input

def calculate_day1_solution(inp):
    """
    The idea here is to exploit the fact that if a + b = 2020, then b = 2020 - a
    So we first find the differences in one pass, and then make another pass to 
    find the element that equals the difference. Finally, we return the product of the element
    and the difference
    """
    differences = [2020 - elem for elem in inp]
    sorted_inp = list(sorted(inp))
    sorted_differences = list(sorted(differences))

    i, j = 0, 0  # index pointers on each of the lists
    while i < len(inp) and j < len(inp):
        if sorted_inp[i] == sorted_differences[j]:
            return sorted_inp[i] * (2020 - sorted_inp[i])
        elif sorted_inp[i] < sorted_differences[j]:
            i += 1
        else:
            j += 1
    return "No pair found that sums to 2020"
    

if __name__ == '__main__':
    inp = read_input('day1')
    print(calculate_day1_solution(inp))
    
    