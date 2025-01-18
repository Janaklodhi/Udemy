# [2:14 PM, 1/11/2025] Harshita Ji: Sure! Below are the Python solutions for the questions:

### 1. *Decrease the salary of employees by 5%*
python
employee_salaries = {
    'John': 50000,
    'Alice': 60000,
    'Bob': 45000,
    'Eve': 70000
}

for employee in employee_salaries:
    employee_salaries[employee] *= 0.95

print(employee_salaries)


### 2. *Find the highest and lowest salary*
python
employee_salaries = {
    'John': 50000,
    'Alice': 60000,
    'Bob': 45000,
    'Eve': 70000
}

highest_salary_employee = max(employee_salaries, key=employee_salaries.get)
lowest_salary_employee = min(employee_salaries, key=employee_salaries.get)

print(f"Highest Salary: {highest_salary_employee} with ${employee_salaries[highest_salary_employee]}")
print(f"Lowest Salary: {lowest_salary_employee} w…
[2:15 PM, 1/11/2025] Harshita Ji: Here are some more similar questions related to modifying and working with dictionaries in Python:

1. *Decrease the salary of employees by 5%:*
   Write a program to decrease the salary of each employee by 5% in a given dictionary.

2. *Find the highest and lowest salary:*
   Given a dictionary of employee salaries, write a program that finds and prints the employee with the highest and lowest salary.

3. *Add a new employee's salary:*
   Write a program to add a new employee with their salary to the dictionary.

4. *Increase salary by a user-defined percentage:*
   Write a program that asks the user to input a percentage, then increases all employees' salaries by that percentage.

5. *Check for employees earning below a certain threshold:*
   Write a program to find…
[2:15 PM, 1/11/2025] Harshita Ji: You can update the salaries in the dictionary by multiplying each salary by 1.10 (which represents a 10% increase). Here's how you can do it:

python
# Example dictionary of employees and their salaries
employee_salaries = {
    'John': 50000,
    'Alice': 60000,
    'Bob': 45000,
    'Eve': 70000
}

# Increase each employee's salary by 10%
for employee in employee_salaries:
    employee_salaries[employee] *= 1.10

# Print the updated salaries
print(employee_salaries)


This will increase each employee's salary by 10%. After running this, the employee_salaries dictionary will contain the updated values.
[2:22 PM, 1/11/2025] Harshita Ji: Here are some practical *programming challenges* based on dictionaries that you can use to prepare for interviews or to test your understanding of dictionaries in Python:

---

### *1. Merge Two Dictionaries*

*Problem:*  
Write a Python program that merges two dictionaries. If there are duplicate keys, the value from the second dictionary should overwrite the value from the first dictionary.

*Example:*
python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

*Expected Output:*
python
{'a': 1, 'b': 3, 'c': 4}


---

### *2. Remove Keys with a Specific Value*

*Problem:*  
Write a Python program that removes all keys from a dictionary where the value is less than a given threshold.

*Example:*
python
my_dict = {'a': 5, 'b': 12, 'c': 7, 'd': 3}
threshold = 6

*Expected Output:*
python
{'b': 12, 'c': 7}


---

### *3. Find the Key with the Maximum Value*

*Problem:*  
Write a Python program that returns the key corresponding to the maximum value in a dictionary.

*Example:*
python
my_dict = {'a': 10, 'b': 20, 'c': 30}

*Expected Output:*
python
'c'


---

### *4. Dictionary Flattening*

*Problem:*  
Write a Python program to flatten a nested dictionary, so that nested keys become part of the parent key. The nested keys should be joined with an underscore (_).

*Example:*
python
nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3}}

*Expected Output:*
python
{'a_b': 1, 'a_c': 2, 'd_e': 3}


---

### *5. Count the Frequency of Words in a Sentence*

*Problem:*  
Write a Python program that counts the frequency of each word in a sentence and returns a dictionary where the keys are words and the values are their frequencies.

*Example:*
python
sentence = "hello world hello python world hello"

*Expected Output:*
python
{'hello': 3, 'world': 2, 'python': 1}


---

### *6. Find the Intersection of Two Dictionaries*

*Problem:*  
Write a Python program to find the intersection of two dictionaries. The intersection is the set of key-value pairs where the keys are common in both dictionaries and the values are the same.

*Example:*
python
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 3}

*Expected Output:*
python
{'b': 2}


---

### *7. Sort a Dictionary by Values*

*Problem:*  
Write a Python program that sorts a dictionary by its values in descending order.

*Example:*
python
my_dict = {'a': 5, 'b': 12, 'c': 7}

*Expected Output:*
python
{'b': 12, 'c': 7, 'a': 5}


---

### *8. Group a List of Items by a Key in a Dictionary*

*Problem:*  
Write a Python program that groups a list of items by a specific key in a dictionary. The key can be any attribute of the items (e.g., the first letter of a name, age group, etc.).

*Example:*
python
items = ['apple', 'banana', 'apricot', 'blueberry']

*Group by first letter:*
python
{'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}


---

### *9. Swap Keys and Values*

*Problem:*  
Write a Python program to swap keys and values in a dictionary. The dictionary should have unique values for this operation to work correctly.

*Example:*
python
my_dict = {'a': 1, 'b': 2, 'c': 3}

*Expected Output:*
python
{1: 'a', 2: 'b', 3: 'c'}


---

### *10. Merge Lists into Dictionary*

*Problem:*  
Write a Python program that merges two lists into a dictionary. One list will contain keys and the other will contain values. If the lists are of unequal lengths, the remaining keys should have a value of None.

*Example:*
python
keys = ['a', 'b', 'c']
values = [1, 2]

*Expected Output:*
python
{'a': 1, 'b': 2, 'c': None}


---

### *11. Count Occurrences of Each Character in a String*

*Problem:*  
Write a Python program that counts the number of occurrences of each character in a string and stores it in a dictionary.

*Example:*
python
my_string = "programming"

*Expected Output:*
python
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i…
[2:23 PM, 1/11/2025] Harshita Ji: Here are some practical *programming challenges* based on dictionaries that you can use to prepare for interviews or to test your understanding of dictionaries in Python:

---

### *1. Merge Two Dictionaries*

*Problem:*  
Write a Python program that merges two dictionaries. If there are duplicate keys, the value from the second dictionary should overwrite the value from the first dictionary.

*Example:*
python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

*Expected Output:*
python
{'a': 1, 'b': 3, 'c': 4}


---

### *2. Remove Keys with a Specific Value*

*Problem:*  
Write a Python program that removes all keys from a dictionary where the value is less than a given threshold.

*Example:*
python
my_dict = {'a': 5, 'b': 12, 'c': 7, 'd': 3}
threshold = 6

*Expected Output:*
python
{'b': 12, 'c': 7}


---

### *3. Find the Key with the Maximum Value*

*Problem:*  
Write a Python program that returns the key corresponding to the maximum value in a dictionary.

*Example:*
python
my_dict = {'a': 10, 'b': 20, 'c': 30}

*Expected Output:*
python
'c'


---

### *4. Dictionary Flattening*

*Problem:*  
Write a Python program to flatten a nested dictionary, so that nested keys become part of the parent key. The nested keys should be joined with an underscore (_).

*Example:*
python
nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3}}

*Expected Output:*
python
{'a_b': 1, 'a_c': 2, 'd_e': 3}


---

### *5. Count the Frequency of Words in a Sentence*

*Problem:*  
Write a Python program that counts the frequency of each word in a sentence and returns a dictionary where the keys are words and the values are their frequencies.

*Example:*
python
sentence = "hello world hello python world hello"

*Expected Output:*
python
{'hello': 3, 'world': 2, 'python': 1}


---

### *6. Find the Intersection of Two Dictionaries*

*Problem:*  
Write a Python program to find the intersection of two dictionaries. The intersection is the set of key-value pairs where the keys are common in both dictionaries and the values are the same.

*Example:*
python
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 3}

*Expected Output:*
python
{'b': 2}


---

### *7. Sort a Dictionary by Values*

*Problem:*  
Write a Python program that sorts a dictionary by its values in descending order.

*Example:*
python
my_dict = {'a': 5, 'b': 12, 'c': 7}

*Expected Output:*
python
{'b': 12, 'c': 7, 'a': 5}


---

### *8. Group a List of Items by a Key in a Dictionary*

*Problem:*  
Write a Python program that groups a list of items by a specific key in a dictionary. The key can be any attribute of the items (e.g., the first letter of a name, age group, etc.).

*Example:*
python
items = ['apple', 'banana', 'apricot', 'blueberry']

*Group by first letter:*
python
{'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}


---

### *9. Swap Keys and Values*

*Problem:*  
Write a Python program to swap keys and values in a dictionary. The dictionary should have unique values for this operation to work correctly.

*Example:*
python
my_dict = {'a': 1, 'b': 2, 'c': 3}

*Expected Output:*
python
{1: 'a', 2: 'b', 3: 'c'}


---

### *10. Merge Lists into Dictionary*

*Problem:*  
Write a Python program that merges two lists into a dictionary. One list will contain keys and the other will contain values. If the lists are of unequal lengths, the remaining keys should have a value of None.

*Example:*
python
keys = ['a', 'b', 'c']
values = [1, 2]

*Expected Output:*
python
{'a': 1, 'b': 2, 'c': None}


---

### *11. Count Occurrences of Each Character in a String*

*Problem:*  
Write a Python program that counts the number of occurrences of each character in a string and stores it in a dictionary.

*Example:*
python
my_string = "programming"

*Expected Output:*
python
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i…
[2:24 PM, 1/11/2025] Harshita Ji: Absolutely! Here are some important concepts, tricks, and interview-style questions related to Python dictionaries that an interviewer may ask. I'll cover different aspects including basic operations, advanced techniques, and optimization questions.

---

### *1. Basic Dictionary Operations*

#### *Questions:*
1. *What is a dictionary in Python?*
   - A dictionary in Python is an unordered collection of key-value pairs where each key is unique. It's defined using {} braces and the key-value pairs are separated by a colon (:).

2. *How do you create a dictionary?*
   python
   my_dict = {'name': 'John', 'age': 25}
   

3. *How do you add a new key-value pair to a dictionary?*
   python
   my_dict['address'] = '123 Main St'
   

4. *How do you access the value for a s…
[2:27 PM, 1/11/2025] Harshita Ji: Sure! Here are the Python programs for each of the problems mentioned above:

---

### *1. Merge Two Dictionaries*
python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)  # Merges dict2 into dict1
print(dict1)

*Output:*
python
{'a': 1, 'b': 3, 'c': 4}


---

### *2. Remove Keys with a Specific Value*
python
my_dict = {'a': 5, 'b': 12, 'c': 7, 'd': 3}
threshold = 6

my_dict = {k: v for k, v in my_dict.items() if v >= threshold}
print(my_dict)

*Output:*
python
{'b': 12, 'c': 7}


---

### *3. Find the Key with the Maximum Value*
python
my_dict = {'a': 10, 'b': 20, 'c': 30}

max_key = max(my_dict, key=my_dict.get)
print(max_key)

*Output:*
python
'c'


---

### *4. Dictionary Flattening*
python
nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3}}

flat_dict = {f"{k}_{subkey}": subvalue for k, v in nested_dict.items() for subkey, subvalue in v.items()}
print(flat_dict)

*Output:*
python
{'a_b': 1, 'a_c': 2, 'd_e': 3}


---

### *5. Count the Frequency of Words in a Sentence*
python
sentence = "hello world hello python world hello"
words = sentence.split()

word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print(word_freq)

*Output:*
python
{'hello': 3, 'world': 2, 'python': 1}


---

### *6. Find the Intersection of Two Dictionaries*
python
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 3}

intersection = {k: dict1[k] for k in dict1 if k in dict2 and dict1[k] == dict2[k]}
print(intersection)

*Output:*
python
{'b': 2}


---

### *7. Sort a Dictionary by Values*
python
my_dict = {'a': 5, 'b': 12, 'c': 7}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict)

*Output:*
python
{'b': 12, 'c': 7, 'a': 5}


---

### *8. Group a List of Items by a Key in a Dictionary*
python
items = ['apple', 'banana', 'apricot', 'blueberry']

grouped = {}
for item in items:
    first_letter = item[0].lower()
    if first_letter not in grouped:
        grouped[first_letter] = []
    grouped[first_letter].append(item)

print(grouped)

*Output:*
python
{'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}


---

### *9. Swap Keys and Values*
python
my_dict = {'a': 1, 'b': 2, 'c': 3}

swapped_dict = {v: k for k, v in my_dict.items()}
print(swapped_dict)

*Output:*
python
{1: 'a', 2: 'b', 3: 'c'}


---

### *10. Merge Lists into Dictionary*
python
keys = ['a', 'b', 'c']
values = [1, 2]

merged_dict = {keys[i]: values[i] if i < len(values) else None for i in range(len(keys))}
print(merged_dict)

*Output:*
python
{'a': 1, 'b': 2, 'c': None}


---

### *11. Count the Occurrences of Each Character in a String*
python
my_string = "programming"

char_count = {}
for char in my_string:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)

*Output:*
python
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}


---

### *12. Check if a Dictionary is Subset of Another Dictionary*
python
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 2, 'c': 3}

is_subset = all(item in dict2.items() for item in dict1.items())
print(is_subset)

*Output:*
python
True


---

### *13. Filter Dictionary by Condition*
python
my_dict = {'a': 5, 'b': 10, 'c': 3, 'd': 8}
threshold = 5

filtered_dict = {k: v for k, v in my_dict.items() if v >= threshold}
print(filtered_dict)

*Output:*
python
{'b': 10, 'd': 8}


---

### *14. Create a Dictionary from Two Lists*
python
keys = ['a', 'b', 'c']
values = [1, 2, 3]

my_dict = dict(zip(keys, values))
print(my_dict)

*Output:*
python
{'a': 1, 'b': 2, 'c': 3}


---

### *15. Count the Occurrences of Each Value in a Dictionary*
python
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

value_count = {}
for value in my_dict.values():
    value_count[value] = value_count.get(value, 0) + 1

print(value_count)

*Output:*
python
{1: 2, 2: 2, 3: 1}







==============================================================================================================================================================================================================================================================================================================================================================================================================================================





Here’s a comprehensive list of **Algorithms and Data Structures (DSA)** topics, organized by category, including key **patterns** and topics related to **Analysis and Design of Algorithms (ADA)**.

---

### **1. Algorithm Design and Analysis (ADA) Basics**
- **Algorithm Complexity:**
  - Time Complexity (Big-O, Big-Θ, Big-Ω)
  - Space Complexity
  - Best-case, Worst-case, Average-case analysis
- **Algorithm Design Techniques:**
  - Divide and Conquer
  - Greedy Algorithms
  - Dynamic Programming
  - Backtracking
  - Branch and Bound
  - Recursive vs Iterative Algorithms
- **Asymptotic Notations:**
  - O(n), O(log n), O(n²), etc.
  - Master Theorem for Divide and Conquer Recurrence

---

### **2. Searching and Sorting Algorithms**
- **Searching:**
  - Linear Search
  - Binary Search
  - Ternary Search
  - Exponential Search
  - Interpolation Search
- **Sorting:**
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
  - Heap Sort
  - Radix Sort
  - Counting Sort
  - Bucket Sort
  - Shell Sort
- **Patterns:**
  - Two-pointer Technique
  - Sliding Window
  - Partitioning (used in Quick Sort)

---

### **3. Data Structures**
- **Arrays:**
  - Prefix Sum, Suffix Sum
  - Kadane’s Algorithm (Max Subarray Sum)
  - Majority Element Problems
- **Strings:**
  - Pattern Matching (Knuth-Morris-Pratt, Rabin-Karp, Z-algorithm)
  - Anagrams, Palindromes
  - Trie (Prefix Tree)
  - Longest Common Subsequence/Substring
- **Linked Lists:**
  - Singly, Doubly, Circular Linked Lists
  - Floyd’s Cycle Detection Algorithm
  - Reversing a Linked List
- **Stacks and Queues:**
  - Implementation (using arrays or linked lists)
  - Monotonic Stack/Queue
  - Priority Queues (Heaps)
  - Deque
- **Trees:**
  - Binary Tree
  - Binary Search Tree
  - AVL Tree
  - Segment Tree
  - Fenwick Tree (Binary Indexed Tree)
  - Trie
- **Graphs:**
  - Representations: Adjacency List, Adjacency Matrix
  - Graph Traversals: BFS, DFS
  - Minimum Spanning Tree: Kruskal, Prim
  - Shortest Paths: Dijkstra, Bellman-Ford, Floyd-Warshall, A*
  - Topological Sort
  - Strongly Connected Components (Tarjan’s Algorithm)
  - Union-Find (Disjoint Set Union)
- **Hashing:**
  - Hash Tables, Hash Maps
  - Collision Handling (Chaining, Open Addressing)
  - Bloom Filters

---

### **4. Recursion and Backtracking**
- Subset/Subset-Sum Problems
- Permutations and Combinations
- N-Queens Problem
- Sudoku Solver
- Word Search in a Grid
- Rat in a Maze

---

### **5. Dynamic Programming (DP)**
- Fibonacci Sequence (Memoization, Tabulation)
- Longest Increasing Subsequence (LIS)
- Longest Common Subsequence (LCS)
- Knapsack Problems (0/1 Knapsack, Fractional Knapsack)
- Matrix Chain Multiplication
- Coin Change Problem
- Subset Sum Problem
- DP on Trees (Diameter, Path Sums)

---

### **6. Greedy Algorithms**
- Activity Selection Problem
- Huffman Encoding
- Fractional Knapsack
- Job Scheduling Problem
- Minimum Platforms

---

### **7. Divide and Conquer**
- Merge Sort
- Quick Sort
- Binary Search
- Closest Pair of Points
- Strassen’s Matrix Multiplication

---

### **8. Graph Algorithms**
- BFS and DFS
- Topological Sorting
- Minimum Spanning Tree (Kruskal, Prim)
- Shortest Path Algorithms:
  - Dijkstra’s Algorithm
  - Bellman-Ford Algorithm
  - Floyd-Warshall Algorithm
  - A* Algorithm
- Network Flow (Ford-Fulkerson, Edmonds-Karp)
- Bridges and Articulation Points
- Eulerian and Hamiltonian Paths

---

### **9. Mathematical Algorithms**
- GCD and LCM (Euclidean Algorithm)
- Modular Arithmetic
- Sieve of Eratosthenes (Prime Numbers)
- Modular Exponentiation
- Matrix Exponentiation
- Fast Fourier Transform (FFT)

---

### **10. Pattern-Based Problem Solving**
- **Sliding Window:**
  - Maximum/Minimum in a Subarray
  - Longest Substring Problems
- **Two Pointers:**
  - Pair Sum, Triplet Sum
  - Dutch National Flag Problem
- **Divide and Conquer:**
  - Maximum Subarray (Kadane’s Algorithm)
  - Median of Two Sorted Arrays
- **Dynamic Programming Patterns:**
  - Subproblems Overlapping
  - State Transition Diagram

---

### **11. Advanced Topics**
- **Bit Manipulation:**
  - XOR Problems
  - Counting Set Bits
  - Subset Generation
- **Trie and Suffix Trees**
- **Game Theory:**
  - Minimax Algorithm
  - Alpha-Beta Pruning
- **Randomized Algorithms:**
  - Monte Carlo Methods
  - Reservoir Sampling
- **Computational Geometry:**
  - Convex Hull
  - Line Intersection
  - Closest Pair of Points

---

### **12. Practice Problems**
- Implement these algorithms on platforms like **LeetCode**, **Codeforces**, **HackerRank**, and **GeeksforGeeks** to strengthen your skills.

Would you like me to explain any specific algorithm or pattern in detail? 😊




python manage.py shell: Open the default Django shell.
from <app_name>.models import <ModelName>: Import your models.
Model.objects.create(): Create a new record.
Model.objects.all(): Retrieve all records.
Model.objects.filter(): Retrieve filtered records.
Model.objects.get(): Retrieve a single record by primary key.
product.save(): Save updates to a record.
product.delete(): Delete a record.
Model.objects.count(): Count the number of records.
Model.objects.aggregate(): Perform aggregations like sum or average.