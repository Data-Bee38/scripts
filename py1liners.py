#Python one liner utility scripts

#=============================================================
# Generate a Random Number between.. 
#=============================================================
import random

def randnum(min, max):
    return round(random.uniform(min, max))

print(randnum(1, 7))  # Outputs a random number between 1 and 7

#=============================================================
# Check first value in an array 
#=============================================================
import numpy as np

def is_first_biggest(xs):
    return xs[0] == sorted(xs, reverse=True)[0]

print(is_first_biggest([20.1, 5, 4, 3, 2, 1]))  # True

#=============================================================
# Remove item form an array
#=============================================================
def remove_array_item(array, item):
    return [x for x in array if x != item]

print( remove_array_item(['red', 'blue', 'green', 'tan'], 'tan') ) #=> ['red','blue','green']

#=============================================================
# Generate a Random Number between.. 
#=============================================================
import random

def rand_step(min, max, step):
    return min + (step * int(random.random() * (max - min) / step))

print( rand_step(0, 100, 20) #=> 0,20,40,60,80

#=============================================================
# Get random item an an array 
#=============================================================
import random

def get_rand_array_item(arr):
    return random.choice(arr)

print(get_rand_array_item(['red', 'blue', 'green', 'tan']))  #=> green

#=============================================================
# Check array for specific item
#=============================================================
def array_has_item(array, item):
    return item in array

print( array_has_item(['orange', 'red', 'blue'], 'blue') ) #=> True

#=============================================================
# Remove specicif item an an array
#=============================================================
def remove_array_item(array, item):
    return [x for x in array if x != item]

print(remove_array_item(['red', 'blue', 'green', 'tan'], 'tan'))  #=> ['red', 'blue', 'green']

#=============================================================
# Shuffle an array
#=============================================================
import random

def shuffle_array(arr):
    return sorted(arr, key=lambda x: random.random() - 0.5)

print( shuffle_array(['a','b','c','d']) ) #=> ['d','a','c','b']

#=============================================================
# Sort an array
#=============================================================
def my_sort(*args):
    return sorted(args)

print( my_sort(10, 2, 3) ) #=> [2, 3, 10]

#=============================================================
# Break down an array in chunks
#=============================================================
def chunk_array(arr, size):
    return [arr[i:i + size] for i in range(0, len(arr), size)]

print(chunk_array([1, 2, 3, 4, 5, 9, 8, 7], 3))  #=> [[1, 2, 3], [4, 5, 9], [8, 7]]

#=============================================================
# Create range
#=============================================================
def create_range(start, end):
    return list(range(start, end + 1))
    
print( create_range(5,10) ) #=> [5, 6, 7, 8, 9, 10]
print( create_range(5,10)[::-1] ) #=> [10, 9, 8, 7, 6, 5]

#=============================================================
# Check if array is empty
#=============================================================
def check_empty_array(arr):
    return not isinstance(arr, list) or len(arr) == 0
    
    
print( check_empty_array([]) )	  #=> True
print( check_empty_array([""]) )  #=> False

#=============================================================
# Find similarity in an array
#=============================================================
def find_similarity(arr, values):
    return [v for v in arr if v in values]

print( find_similarity([1,2,3], [1,2,4]) ) #=> [1,2]

#=============================================================
# Count occurences in an array
#=============================================================
def count_occurrences(arr, value):
    return sum(1 for v in arr if v == value)

print( count_occurrences([7,7,7,1,1,2,1,2,3,7], 7) ) #=> 4    
print( count_occurrences(list(map(str.lower,["cat", "dog", "moose", "Cat"])), "cat") ) #=> 2
    
#=============================================================
# Loop through array 
#=============================================================
upper_case = list(map(lambda x: x.upper(), ['apple', 'banana', 'cherry']))

#=============================================================
# Zip Function
#=============================================================
students = ['Dilli', 'Vikram', 'Rolex', 'Leo']
grades = [85, 92, 78, 88]

student_grade_pairs = list(zip(students, grades))
print(student_grade_pairs)

#=============================================================
# Enumerate Function
#=============================================================
grocery_list = ['Apples', 'Milk', 'Bread', 'Eggs', 'Cheese']

for index, item in enumerate(grocery_list):
    print(f"{index}. {item}")

#=============================================================
# Unpacking List
#=============================================================
numbers = [1, 2, 3]

a, b, c = numbers

print(a, b, c)

#=============================================================
# Convert object to array and array to object
#=============================================================
def obj_to_array(obj):
    return [obj[key] for key in obj.keys()]

def array_to_object(arr, key_field):
    return {item[key_field]: item for item in arr}
    
our_data = {
    "123456a": {
        "name": "tim",
        "age": 40,
        "city": "Farmtown"
    },
    "123456b": {
        "name": "jerry",
        "age": 40,
        "city": "Beachroad"
    },
    "123456c": {
        "name": "bob",
        "age": 30,
        "city": "Busyville"
    }
}


print( obj_to_array(our_data) )

#[{'name': 'tim', 'age': 40, 'city': 'Farmtown'}, {'name': 'jerry', 'age': 40, 'city': 'Beachroad'}, {'name': 'bob', 'age': 30, 'city': 'Busyville'}]


print( array_to_object(obj_to_array(our_data), "city") ) 

#{'Farmtown': {'name': 'tim', 'age': 40, 'city': 'Farmtown'}, 'Beachroad': {'name': 'jerry', 'age': 40, 'city': 'Beachroad'}, 'Busyville': {'name': 'bob', 'age': 30, 'city': 'Busyville'}}

#=============================================================
# Sum up value in an object
#=============================================================
arr_obj = [
    {"name": "Larry", "likes": 300},
    {"name": "Curly", "likes": 100},
    {"name": "Monica", "likes": 50}
]

result = sum(map(lambda d: sum([d["likes"]]), arr_obj))
print(result) #=> 450

#=============================================================
# Dictionary
#=============================================================
def search_dic(name):
    the_dict = {'red': '#ff4444', 'blue': '#3b5998', 'yellow': '#fff68f'}
    return the_dict[name]

print( search_dic('red') ) # => '#ff4444'

#=============================================================
# Check if number is odd
#=============================================================
def is_odd(num):
    return True if num % 2 != 0 else False

print( is_odd(7) ) #=> True

#=============================================================
# Check if number is even
#=============================================================
def iseven(num):
    return False if num % 2 != 0 else True

print( iseven(4) ) #=> True

#=============================================================
# Get average
#=============================================================
def get_average(tests):
    return sum(tests) / len(tests)

print( get_average([10, 20, 30]) ) #=> 20.0

#=============================================================
# Sum Over Every Other Value Python One-Liner
#=============================================================
sum(stock_prices[::2])

#=============================================================
# Return index number
#=============================================================
lst = [1, 2, 3, 'Alice', 'Alice']
indices = [i for i in range(len(lst)) if lst[i]=='Alice']
print(indices) # [3, 4]

#=============================================================
# CSV file to json
#=============================================================
python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"

#=============================================================
# Compress CSS file
#=============================================================
python -c 'import re,sys;print re.sub("\s*([{};,:])\s*", "\\1", re.sub("/\*.*?\*/", "", re.sub("\s+", " ", sys.stdin.read())))'

#=============================================================
# This can be used to convert a string into a "url safe" string
#=============================================================
python -c "import urllib, sys ; print urllib.quote_plus(sys.stdin.read())";




#=============================================================
# Sum of all numbers in a list
sum([1, 2, 3, 4, 5])
#=============================================================


#=============================================================
# Flatten a nested list
flattened = [item for sublist in [[1, 2], [3, 4], [5]] for item in sublist]
#=============================================================


#=============================================================
# Generate Fibonacci sequence (up to n terms)
fibonacci = lambda n: [0, 1][:n] + [sum(fibonacci(n - 1)[-2:])]
#=============================================================


#=============================================================
# Factorial of a number
import math; 
factorial = math.factorial(5)
#=============================================================


#=============================================================
# Calculate the length of each word in a list of words
word_lengths = list(map(len, ["hello", "world", "Python"]))
#=============================================================


#=============================================================
# Reverse a string
reversed_string = "hello world"[::-1]
#=============================================================


#=============================================================
# Check if a string is a palindrome
is_palindrome = lambda s: s == s[::-1]
#=============================================================


#=============================================================
# Capitalize first letter of each word in a sentence
capitalized = " ".join(word.capitalize() for word in "hello world from python".split())
#=============================================================


#=============================================================
# Count occurrences of each character in a string
from collections import Counter; 
char_count = Counter("hello world")
#=============================================================


#=============================================================
# Remove vowels from a string
no_vowels = "".join(c for c in "hello world" if c.lower() not in "aeiou")
#=============================================================


#=============================================================
# Create a dictionary from two lists
keys, values = ["name", "age"], ["Alice", 25]; dictionary = dict(zip(keys, values))
#=============================================================


#=============================================================
# Filter even numbers from a list
even_numbers = [x for x in range(10) if x % 2 == 0]
#=============================================================


#=============================================================
# Get squares of numbers in a list
squares = [x**2 for x in range(10)]
#=============================================================


#=============================================================
# Reverse a dictionary
reversed_dict = {v: k for k, v in {"a": 1, "b": 2}.items()}
#=============================================================


#=============================================================
# Read all lines from a file
lines = [line.strip() for line in open("file.txt")]
#=============================================================


#=============================================================
# Write a list to a file, each element on a new line
with open("output.txt", "w") as f: [f.write(f"{line}\n") for line in ["hello", "world"]]
#=============================================================


#=============================================================
# Get current working directory
import os; 
cwd = os.getcwd()
#=============================================================


#=============================================================
# Check if a file exists
import os; 
file_exists = os.path.isfile("file.txt")
#=============================================================


#=============================================================
# Count lines in a file
line_count = sum(1 for _ in open("file.txt"))
#=============================================================


#=============================================================
# Get current date and time
from datetime import datetime; 
now = datetime.now()
#=============================================================


#=============================================================
# Get yesterday’s date
from datetime import datetime, timedelta; 
yesterday = datetime.now() - timedelta(days=1)
#=============================================================


#=============================================================
# Format current time as "YYYY-MM-DD HH:MM:SS"
formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#=============================================================


#=============================================================
# Measure execution time of a one-liner
import time; 
start = time.time(); [x**2 for x in range(10000)]; execution_time = time.time() - start
#=============================================================


#=============================================================
import pandas as pd

# Create a DataFrame from a list of dictionaries
data = pd.DataFrame([{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}])

# Get summary statistics for a DataFrame
summary = data.describe()

# Read a CSV file into a DataFrame
df = pd.read_csv("file.csv")

# Filter rows in a DataFrame
filtered_df = df[df["age"] > 25]

# Calculate the average of a column
average_age = df["age"].mean()
#=============================================================


#=============================================================
# Calculate squares of numbers using map
squares = list(map(lambda x: x**2, range(10)))
#=============================================================


#=============================================================
# Filter even numbers using filter
evens = list(filter(lambda x: x % 2 == 0, range(10)))
#=============================================================


#=============================================================
# Reduce: Calculate factorial of a number
from functools import reduce; 
factorial = reduce(lambda x, y: x * y, range(1, 6))
#=============================================================


#=============================================================
import re

# Find all words in a string
words = re.findall(r'\b\w+\b', "hello world, welcome to Python")

# Replace all digits with "#"
masked_string = re.sub(r'\d', '#', "My phone number is 123-456-7890")

# Extract email addresses from text
emails = re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', "Contact me at email@example.com")
#=============================================================


#=============================================================
import random

# Generate a random integer between 1 and 100
rand_int = random.randint(1, 100)

# Pick a random element from a list
random_choice = random.choice(["apple", "banana", "cherry"])

# Shuffle a list
my_list = [1, 2, 3, 4, 5]; random.shuffle(my_list)

# Generate a random string of letters
random_string = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(10))
#=============================================================


#=============================================================
# Get the title of a webpage (requires requests and BeautifulSoup)
import requests; from bs4 import BeautifulSoup; title = BeautifulSoup(requests.get("http://example.com").content, "html.parser").title.string
#=============================================================



#=============================================================
# Generate an MD5 hash of a string
import hashlib; 
md5_hash = hashlib.md5("hello world".encode()).hexdigest()

# Generate a random 8-character password
import random; import string; 
password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# Base64 encode a string
import base64; 
encoded = base64.b64encode("hello world".encode()).decode()
#=============================================================



#=============================================================
# Convert a dictionary to JSON string
import json; 
json_string = json.dumps({"name": "Alice", "age": 25})

# Parse JSON string to dictionary
parsed_json = json.loads('{"name": "Alice", "age": 25}')

# Pretty-print a JSON object
pretty_json = json.dumps({"name": "Alice", "age": 25}, indent=4)

# Merge two lists of dictionaries by a common key
from itertools import chain
merged_list = list(chain([{"id": 1, "value": "a"}], [{"id": 1, "extra": "info"}]))
#=============================================================



#=============================================================
# Calculate the mean of a list of numbers
mean = lambda lst: sum(lst) / len(lst) if lst else None

# Find the median of a list of numbers
median = lambda lst: sorted(lst)[len(lst) // 2]

# Calculate standard deviation of a list
import statistics; 
stdev = statistics.stdev([1, 2, 3, 4, 5])

# Generate a list of prime numbers up to n
primes = lambda n: [x for x in range(2, n) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]
#=============================================================



#=============================================================
# Sort a list of dictionaries by a key
sorted_list = sorted([{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}], key=lambda x: x["age"])

# Find the maximum value in a dictionary by key
max_value = max({"a": 10, "b": 20, "c": 15}.items(), key=lambda x: x[1])

# Check if an element exists in a list
exists = 10 in [1, 2, 3, 10, 20]

# Find the index of an element in a list
index = [1, 2, 3, 4].index(3) if 3 in [1, 2, 3, 4] else -1
#=============================================================



#=============================================================
# Find the union of two sets
union = {1, 2, 3} | {3, 4, 5}

# Find the intersection of two sets
intersection = {1, 2, 3} & {3, 4, 5}

# Find the difference between two sets
difference = {1, 2, 3} - {3, 4, 5}

# Find unique elements in a list
unique_elements = list(set([1, 1, 2, 3, 3, 4]))
#=============================================================



#=============================================================
# Zip two lists into a dictionary
keys, values = ["name", "age"], ["Alice", 25]; zipped_dict = dict(zip(keys, values))

# Flatten a nested dictionary
flat_dict = {k: v for d in [{"a": 1}, {"b": 2}, {"c": 3}] for k, v in d.items()}

# Find duplicate elements in a list
duplicates = set([x for x in [1, 2, 3, 2, 4, 5, 1] if [1, 2, 3, 2, 4, 5, 1].count(x) > 1])

# Merge two dictionaries
merged_dict = {**{"a": 1, "b": 2}, **{"b": 3, "c": 4}}
#=============================================================



#=============================================================
# Remove duplicates from a list
unique = list(set([1, 2, 3, 1, 2, 4]))

# Get the product of all elements in a list
import math; 
product = math.prod([1, 2, 3, 4])

# Get a cumulative sum of a list
cumulative_sum = [sum([1, 2, 3, 4][:i+1]) for i in range(len([1, 2, 3, 4]))]

# Transpose a matrix (list of lists)
transposed = list(map(list, zip(*[[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
#=============================================================



#=============================================================
# Ternary operation (inline if-else)
result = "yes" if True else "no"

# Conditional list comprehension
filtered = [x for x in range(10) if x % 2 == 0]

# Check if all elements in a list are positive
all_positive = all(x > 0 for x in [1, 2, 3])

# Check if any element in a list is negative
any_negative = any(x < 0 for x in [1, 2, -3, 4])
#=============================================================



#=============================================================
# Create a simple class with a method in one line
Person = type('Person', (), {'greet': lambda self: "Hello!"})

# Create an instance and call the method
p = Person(); greeting = p.greet()

# Quick class with an init method
Point = type('Point', (object,), {'__init__': lambda self, x, y: setattr(self, 'x', x) or setattr(self, 'y', y)})
point = Point(3, 4)
#=============================================================



#=============================================================
# List all files in a directory
import os; 
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Read and print all lines from a file in reverse order
with open("file.txt") as f: lines = f.readlines()[::-1]

# Get the size of a file
file_size = os.path.getsize("file.txt")

# Count occurrences of a word in a file
with open("file.txt") as f: word_count = sum(1 for line in f for word in line.split() if word == "word")
#=============================================================