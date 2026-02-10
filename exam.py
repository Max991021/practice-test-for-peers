"""
Python Apprentice Assessment: Core Logic & Algorithms
Focus: Control flow, data manipulation, and problem-solving.
"""

def calculate_shipping_cost(weight, destination):
    """
    Question 1: Conditional Statements
    Calculate shipping based on weight and zone.
    - 'domestic': $5.00 flat rate + $1.50 per lb.
    - 'international': $15.00 flat rate + $5.00 per lb.
    - If weight <= 0, return 0.0.
    """
    while weight >0:
        if 'domestic' == destination.lower():
            return  (5.00) + (1.50)* weight
        elif 'international' == destination.lower():
            return (15.00) + (5.00)*weight
            
    else:
        return  0.0



def filter_even_numbers(numbers):
    """
    Question 2: Functions & Basic Loops
    Accept a list of integers and return a new list containing only the even numbers.
    - If the list is empty, return an empty list.
    """
    if numbers is None:
        return []
    else:
        return [i for i in numbers if i%2 ==0]
    

def generate_multiplication_table(n, limit):
    """
    Question 3: Advanced Loops
    Generate a list of strings representing the multiplication table for 'n' 
    up to the 'limit'. 
    Example: n=2, limit=3 -> ["2 * 1 = 2", "2 * 2 = 4", "2 * 3 = 6"]
    """
    return [str(f'{n} * {i} = {n*i}') for i in range(1,limit+1) ]
    

def find_longest_word(sentence):
    """
    Question 4: Simple Algorithms
    Find the longest word in a space-separated string.
    - If there is a tie, return the first one found.
    - If the string is empty, return an empty string.
    """
    if sentence == '':
        word = ''
    else:
        sentence = sentence.split()
        worddict = {}
        for word in sentence:
            
            worddict[word] = len(word)
        
    
            
        wordnum = max(worddict.values())
        print(wordnum)
        for key, value in worddict.items():
            if value == wordnum:
                word = key 
                break
    return word
print(find_longest_word(""))
        

def fizz_buzz_custom(start, end, fizz_val, buzz_val):
    """
    Question 5: Problem Solving
    Iterate from start to end (inclusive). Return a list where:
    - Multiples of fizz_val are "Fizz"
    - Multiples of buzz_val are "Buzz"
    - Multiples of both are "FizzBuzz"
    - Otherwise, use the number as a string.
    """
    fb = []
    for i in range(start,end+1):
        if i % fizz_val == 0 and i % buzz_val == 0:
            fb.append('FizzBuzz')
        elif i % fizz_val == 0:
            fb.append('Fizz')
        elif i % buzz_val == 0:
            fb.append('Buzz')
        else:
            fb.append(str(i))
    
    return fb