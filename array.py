# 





# we need to reverse the string


# def reverse_str(name):
#     reverse = ""
#     stack = []
#     for i in range(len(name)-1):
#         stack.append(name[i])

#     while stack:
#         reverse= reverse+stack.pop()
#     return reverse


# name = "janaklodhi"
# print(reverse_str(name))


# def reverse_str(name):
#     reverse = ""
#     stack = []

#     # Push all characters onto the stack
#     for char in name:
#         stack.append(char)

#     # Pop characters from the stack and build the reversed string
#     while stack:
#         reverse = reverse + (stack.pop())

#     # Join the list into a string
#     return reverse

# name = "janaklodhi"
# print(reverse_str(name))  # Output: "ihdolkanaJ"







# def reverse_str(name):
#     reverse = ""
#     stack = []

#     # Push all characters onto the stack
#     for char in name:
#         stack.append(char)

#     # Pop characters from the stack and build the reversed string
#     while stack:
#         reverse = reverse + (stack.pop())

#     # Join the list into a string
#     return reverse

# name = "janaklodhi"
# print(reverse_str(name))  # Output: "ihdolkanaJ"



# def reverse_words_stack(sentence):
#     stack = []
#     words = sentence.split()
    
#     # Push all words onto the stack
#     for word in words:
#         stack.append(word)
    
#     # Pop words from the stack to reverse their order
#     reversed_words = []
#     while stack:
#         reversed_words.append(stack.pop())
    
#     return ' '.join(reversed_words)


# # Example usage
# sentence = "I love programming"
# result = reverse_words_stack(sentence)
# print(result)  # Output: "programming love I"




# def longest_comman_prefix(strings):
#     if not strings:
#         return ""

#     strings.sort()
#     first = strings[0]
#     last =  strings[-1]


#     longest_comman_prefix_element = []

#     for i in range(min(len(first), len(last))):
#         if first[i] == last[i]:
#             longest_comman_prefix_element.append(first[i])
#         else:
#             break
#     return ''.join(longest_comman_prefix_element)
# strings = ["flower", "flow", "flight"]
# print(longest_comman_prefix(strings))



# object
# class:
# inheritance:
# encapsulation:
# Abstractions:
# polymorphism:


# class Car:
#     def __init__(self, name, brand):
#         self.name = name
#         self.brand = brand
    

#     def show_data(self):
#         return self.name, self.brand
    
# obj = Car("punch", "tata")
# print(obj.show_data())


# Encapsulation here

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        # This is the private attribute
        self.__balance = balance

    def deposit_amount(self, amount):  # Fixed indentation and method name typo
        self.__balance += amount
        return f"Deposited: {amount}. New balance is: {self.__balance}"

    def withdraw(self, amount):
        if amount > self.__balance:  # Fixed incorrect use of `balance`
            return "Sorry, insufficient funds. Cannot withdraw."
        else:
            self.__balance -= amount
            return f"Withdrew: {amount}. Remaining balance is: {self.__balance}"

    def get_balance(self):
        return self.__balance


# Creating an instance of the BankAccount class
bank1 = BankAccount("Janak", 10000)

# Testing the deposit_amount method
print(bank1.deposit_amount(5000))  # Corrected method call






class A:
    def Hello(self):
        print("good morning")
        
class B(A):
    def greet(self):
        pass