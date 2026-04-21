"""
Python Practice: Dictionary & Set (Teacher Edition)
Focus: Mapping relationships and unique collections with clean logic.
"""

# ==========================================
# PART 1: DICTIONARY ESSENTIALS
# ==========================================

# --- Question 1: Basic Dictionary Creation ---
# Problem: Create a dictionary for a student with name "Alice" and age 20.
student_record = {"name": "Alice", "age": 20}
print(f"Question 1 Result: {student_record}")

# --- Question 2: Accessing Values ---
# Problem: Retrieve the age from the student dictionary created above.
student_age = student_record["age"]
print(f"Question 2 Result: {student_age}")

# --- Question 3: Adding New Keys ---
# Problem: Add a new key "grade" with value "A" to the student dictionary.
student_record["grade"] = "A"
print(f"Question 3 Result: {student_record}")

# --- Question 4: Modifying Values ---
# Problem: Update Alice's age to 21 in the record.
student_record["age"] = 21
print(f"Question 4 Result: {student_record}")

# --- Question 5: Removing a Key (pop) ---
# Problem: Remove the "grade" key and return its value.
removed_grade = student_record.pop("grade")
print(f"Question 5 Result: Removed={removed_grade}, Current Record={student_record}")

# --- Question 6: Using get() for Safety ---
# Problem: Access the key "GPA" safely. If it doesn't exist, return 0.0.
gpa_value = student_record.get("GPA", 0.0)
print(f"Question 6 Result: {gpa_value}")

# --- Question 7: Listing All Keys ---
# Problem: Get a list of all keys currently in the dictionary.
record_keys = list(student_record.keys())
print(f"Question 7 Result: {record_keys}")

# --- Question 8: Listing All Values ---
# Problem: Get a list of all values currently in the dictionary.
record_values = list(student_record.values())
print(f"Question 8 Result: {record_values}")

# --- Question 9: Item Iteration ---
# Problem: Print all key-value pairs in the format 'Key: Value'.
for category, details in student_record.items():
    print(f"Question 9 Info - {category}: {details}")

# --- Question 10: Dictionary Length ---
# Problem: Find out how many attributes are in the student record.
attribute_count = len(student_record)
print(f"Question 10 Result: {attribute_count}")

# --- Question 11: Checking Key Existence ---
# Problem: Verify if 'name' is a valid key in the dictionary.
has_name = "name" in student_record
print(f"Question 11 Result: {has_name}")

# --- Question 12: Merging Dictionaries ---
# Problem: Merge {'city': 'New York'} into {'name': 'Bob'}.
base_info = {"name": "Bob"}
location_info = {"city": "New York"}
base_info.update(location_info)
print(f"Question 12 Result: {base_info}")

# --- Question 13: Dictionary Comprehension ---
# Problem: Create a dictionary where keys are 1-5 and values are their cubes.
cubes_map = {num: num**3 for num in range(1, 6)}
print(f"Question 13 Result: {cubes_map}")

# --- Question 14: Clearing a Dictionary ---
# Problem: Remove all entries from a dictionary.
temp_data = {"id": 101, "status": "active"}
temp_data.clear()
print(f"Question 14 Result: {temp_data}")

# --- Question 15: Copying a Dictionary ---
# Problem: Create a shallow copy of {'a': 1, 'b': 2}.
original_data = {'a': 1, 'b': 2}
cloned_data = original_data.copy()
print(f"Question 15 Result: {cloned_data}")

# --- Question 16: Nested Dictionaries ---
# Problem: Create a dictionary of 'students' containing another dictionary for 'Alice'.
classroom_data = {
    "students": {
        "Alice": {"age": 20, "score": 95}
    }
}
alice_score = classroom_data["students"]["Alice"]["score"]
print(f"Question 16 Result: Alice's Score = {alice_score}")

# --- Question 17: Setting Default Values ---
# Problem: Use setdefault() to add 'active': True if the key is missing.
user_settings = {"theme": "dark"}
user_settings.setdefault("active", True)
print(f"Question 17 Result: {user_settings}")

# --- Question 18: Swapping Keys and Values ---
# Problem: Invert {'A': 1, 'B': 2} to become {1: 'A', 2: 'B'}.
original_map = {'A': 1, 'B': 2}
inverted_map = {value: key for key, value in original_map.items()}
print(f"Question 18 Result: {inverted_map}")

# --- Question 19: Character Frequency Counter ---
# Problem: Count the frequency of characters in "hello".
target_word = "hello"
frequency_counter = {}
for char in target_word:
    frequency_counter[char] = frequency_counter.get(char, 0) + 1
print(f"Question 19 Result: {frequency_counter}")

# --- Question 20: Filtering Dictionary by Value ---
# Problem: From {'a': 10, 'b': 5, 'c': 15}, keep only items where value > 8.
raw_scores = {'a': 10, 'b': 5, 'c': 15}
filtered_scores = {k: v for k, v in raw_scores.items() if v > 8}
print(f"Question 20 Result: {filtered_scores}")

# ==========================================
# PART 2: SET OPERATIONS (UNORDERED & UNIQUE)
# ==========================================

# --- Question 21: Basic Set Creation ---
# Problem: Create a set containing the numbers 1, 2, 2, 3 (notice duplicates).
unique_numbers = {1, 2, 2, 3}
print(f"Question 21 Result: {unique_numbers}")

# --- Question 22: Adding Elements to a Set ---
# Problem: Add the number 4 to the set {1, 2, 3}.
number_collection = {1, 2, 3}
number_collection.add(4)
print(f"Question 22 Result: {number_collection}")

# --- Question 23: Removing Elements (remove) ---
# Problem: Remove 2 from {1, 2, 3}.
my_set = {1, 2, 3}
my_set.remove(2)
print(f"Question 23 Result: {my_set}")

# --- Question 24: Removing Safely (discard) ---
# Problem: Discard 10 from {1, 2, 3} without raising an error.
small_set = {1, 2, 3}
small_set.discard(10)
print(f"Question 24 Result: {small_set}")

# --- Question 25: Set Union ---
# Problem: Find the union of {1, 2} and {2, 3}.
set_a = {1, 2}
set_b = {2, 3}
combined_set = set_a.union(set_b)
print(f"Question 25 Result: {combined_set}")

# --- Question 26: Set Intersection ---
# Problem: Find elements common to {1, 2, 3} and {2, 3, 4}.
prime_set = {1, 2, 3}
even_set = {2, 3, 4}
intersection_result = prime_set.intersection(even_set)
print(f"Question 26 Result: {intersection_result}")

# --- Question 27: Set Difference ---
# Problem: Find elements in {1, 2, 3} but NOT in {2, 3, 4}.
first_set = {1, 2, 3}
second_set = {2, 3, 4}
exclusive_to_first = first_set.difference(second_set)
print(f"Question 27 Result: {exclusive_to_first}")

# --- Question 28: Symmetric Difference ---
# Problem: Find elements that are in either set but not both.
alpha_set = {1, 2, 3}
beta_set = {3, 4, 5}
symmetric_diff = alpha_set.symmetric_difference(beta_set)
print(f"Question 28 Result: {symmetric_diff}")

# --- Question 29: Checking for Subset ---
# Problem: Check if {1, 2} is a subset of {1, 2, 3}.
small_group = {1, 2}
large_group = {1, 2, 3}
is_subset = small_group.issubset(large_group)
print(f"Question 29 Result: {is_subset}")

# --- Question 30: Checking for Superset ---
# Problem: Check if {1, 2, 3} is a superset of {1, 2}.
is_superset = large_group.issuperset(small_group)
print(f"Question 30 Result: {is_superset}")

# --- Question 31: Clearing a Set ---
# Problem: Remove all items from {1, 2, 3}.
clean_me = {1, 2, 3}
clean_me.clear()
print(f"Question 31 Result: {clean_me}")

# --- Question 32: Converting List to Set ---
# Problem: Use a set to find unique items in [1, 2, 2, 3, 3, 3].
raw_list = [1, 2, 2, 3, 3, 3]
unique_items_set = set(raw_list)
print(f"Question 32 Result: {unique_items_set}")

# --- Question 33: FrozenSets (Immutable Sets) ---
# Problem: Create an immutable set containing (1, 2, 3).
immutable_collection = frozenset([1, 2, 3])
print(f"Question 33 Result: {immutable_collection}")

# --- Question 34: Set Pop ---
# Problem: Remove and return an arbitrary element from {1, 2, 3}.
temp_set = {1, 2, 3}
popped_element = temp_set.pop()
print(f"Question 34 Result: Popped={popped_element}, Remaining={temp_set}")

# --- Question 35: Disjoint Check ---
# Problem: Check if {1, 2} and {3, 4} have NO common elements.
set_x = {1, 2}
set_y = {3, 4}
are_disjoint = set_x.isdisjoint(set_y)
print(f"Question 35 Result: {are_disjoint}")

# --- Question 36: Set Comprehension ---
# Problem: Create a set of squares for numbers 1 to 5.
squares_set = {x**2 for x in range(1, 6)}
print(f"Question 36 Result: {squares_set}")

# --- Question 37: Filtering a Set ---
# Problem: Remove all numbers less than 5 from {2, 4, 6, 8}.
original_set = {2, 4, 6, 8}
filtered_set = {n for n in original_set if n >= 5}
print(f"Question 37 Result: {filtered_set}")

# --- Question 38: Counting Vowels ---
# Problem: Use a set to count unique vowels in the word "education".
word = "education"
vowels = {'a', 'e', 'i', 'o', 'u'}
unique_vowels_found = set(word).intersection(vowels)
print(f"Question 38 Result: {len(unique_vowels_found)} vowels ({unique_vowels_found})")

# --- Question 39: Set Membership Test ---
# Problem: Check if 1 is in the set {1, 2, 3} (O(1) complexity).
presence_check = 1 in {1, 2, 3}
print(f"Question 39 Result: {presence_check}")

# --- Question 40: Set Length ---
# Problem: Find how many unique elements are in {1, 2, 3, 3, 3}.
collection_size = len({1, 2, 3, 3, 3})
print(f"Question 40 Result: {collection_size}")

# ==========================================
# PART 3: PRACTICAL APPLICATIONS (DICT & SET)
# ==========================================

# --- Question 41: Merging List of Dicts ---
# Problem: Combine [{'a':1}, {'b':2}] into one dictionary.
list_of_dicts = [{'a': 1}, {'b': 2}]
combined_result = {}
for d in list_of_dicts:
    combined_result.update(d)
print(f"Question 41 Result: {combined_result}")

# --- Question 42: Finding Dictionary Min/Max by Key ---
# Problem: In {'apple': 50, 'banana': 20}, find the key with the minimum value.
inventory = {'apple': 50, 'banana': 20, 'cherry': 30}
cheapest_item = min(inventory, key=inventory.get)
print(f"Question 42 Result: {cheapest_item}")

# --- Question 43: Sorting Dictionary by Key ---
# Problem: Sort {'z': 1, 'a': 10, 'm': 5} alphabetically by keys.
unordered_map = {'z': 1, 'a': 10, 'm': 5}
sorted_by_key = dict(sorted(unordered_map.items()))
print(f"Question 43 Result: {sorted_by_key}")

# --- Question 44: Sorting Dictionary by Value ---
# Problem: Sort {'z': 1, 'a': 10, 'm': 5} numerically by values.
sorted_by_value = dict(sorted(unordered_map.items(), key=lambda item: item[1]))
print(f"Question 44 Result: {sorted_by_value}")

# --- Question 45: Grouping List by First Letter ---
# Problem: Group ['apple', 'apricot', 'banana'] by their first character.
words_list = ['apple', 'apricot', 'banana', 'blueberry']
grouped_words = {}
for word in words_list:
    first_char = word[0]
    grouped_words.setdefault(first_char, []).append(word)
print(f"Question 45 Result: {grouped_words}")

# --- Question 46: Nested Dictionary Update ---
# Problem: Update the 'score' of 'Alice' in a nested structure.
grades = {"Alice": {"math": 90, "science": 85}}
grades["Alice"]["math"] = 95
print(f"Question 46 Result: {grades}")

# --- Question 47: Dictionary from Two Lists ---
# Problem: Map ['id1', 'id2'] to ['Alice', 'Bob'].
keys = ['id1', 'id2']
names = ['Alice', 'Bob']
mapped_dict = dict(zip(keys, names))
print(f"Question 47 Result: {mapped_dict}")

# --- Question 48: Removing None Values ---
# Problem: Remove keys with value None from {'a': 1, 'b': None, 'c': 3}.
data_with_nones = {'a': 1, 'b': None, 'c': 3}
cleaned_data = {k: v for k, v in data_with_nones.items() if v is not None}
print(f"Question 48 Result: {cleaned_data}")

# --- Question 49: Finding Intersection of Values ---
# Problem: Find values common to two dictionaries.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'x': 2, 'y': 3, 'z': 4}
common_values = set(dict1.values()) & set(dict2.values())
print(f"Question 49 Result: {common_values}")

# --- Question 50: Most Frequent Value ---
# Problem: Find the most frequent value in {'a':1, 'b':2, 'c':1, 'd':1}.
user_data = {'a': 1, 'b': 2, 'c': 1, 'd': 1}
vals = list(user_data.values())
mode_value = max(set(vals), key=vals.count)
print(f"Question 50 Result: {mode_value}")

# --- Question 51: Difference between two dictionaries ---
# Problem: Find keys present in dict_a but not in dict_b.
dict_a = {'id': 1, 'name': 'Alice'}
dict_b = {'id': 1}
exclusive_keys = set(dict_a.keys()) - set(dict_b.keys())
print(f"Question 51 Result: {exclusive_keys}")

# --- Question 52: Converting Dict to List of Tuples ---
# Problem: Convert {'a':1, 'b':2} into [('a', 1), ('b', 2)].
sample_dict = {'a': 1, 'b': 2}
list_of_tuples = list(sample_dict.items())
print(f"Question 52 Result: {list_of_tuples}")

# --- Question 53: Merging with Priority ---
# Problem: Merge two dicts where values from the second dict override the first if duplicate.
d1 = {'a': 1, 'b': 2}
d2 = {'b': 10, 'c': 3}
d1.update(d2)
print(f"Question 53 Result: {d1}")

# --- Question 54: Inverting Dictionary with Multiple Values ---
# Problem: Invert {'a': 1, 'b': 1} to become {1: ['a', 'b']}.
multi_map = {'a': 1, 'b': 1, 'c': 2}
inverted_multi_map = {}
for k, v in multi_map.items():
    inverted_multi_map.setdefault(v, []).append(k)
print(f"Question 54 Result: {inverted_multi_map}")

# --- Question 55: Checking if All Values are Equal ---
# Problem: Check if all values in {'a': 5, 'b': 5, 'c': 5} are the same.
uniform_dict = {'a': 5, 'b': 5, 'c': 5}
all_same = len(set(uniform_dict.values())) == 1
print(f"Question 55 Result: {all_same}")

# --- Question 56: Filtering Set by Multiple Conditions ---
# Problem: Keep numbers in {1, 2, 3, 4, 5} that are even and > 3.
numbers_set = {1, 2, 3, 4, 5, 6}
refined_set = {x for x in numbers_set if x % 2 == 0 and x > 3}
print(f"Question 56 Result: {refined_set}")

# --- Question 57: Set of Tuples ---
# Problem: Create a set that stores coordinate tuples.
coordinates = {(0, 0), (1, 1), (2, 2)}
print(f"Question 57 Result: {coordinates}")

# --- Question 58: Finding Symmetric Difference (Multiple Sets) ---
# Problem: Find items present in exactly one of three sets.
s1, s2, s3 = {1, 2}, {2, 3}, {3, 4}
unique_in_one = (s1 ^ s2 ^ s3) - (s1 & s2 & s3)
print(f"Question 58 Result: {unique_in_one}")

# --- Question 59: Removing Set from Another ---
# Problem: Use difference_update to modify s1 by removing elements of s2.
set_target = {1, 2, 3, 4}
set_to_remove = {2, 3}
set_target.difference_update(set_to_remove)
print(f"Question 59 Result: {set_target}")

# --- Question 60: Creating a Set of Characters from a String ---
# Problem: Get unique characters from "Mississippi".
word_input = "Mississippi"
unique_chars = set(word_input)
print(f"Question 60 Result: {unique_chars}")

# ==========================================
# PART 4: CHALLENGE QUESTIONS
# ==========================================

# --- Question 61: Dictionary with Lambda Functions ---
# Problem: Create a dict where keys are 'add' and 'sub' and values are logic.
math_ops = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y
}
print(f"Question 61 Result: 10 + 5 = {math_ops['add'](10, 5)}")

# --- Question 62: Merging Deep Nested Dictionaries ---
# Problem: Merge {'a': {'x': 1}} and {'a': {'y': 2}}.
dict_x = {'a': {'x': 1}}
dict_y = {'a': {'y': 2}}
# Simple update would overwrite 'a'. We need to update the nested dict.
dict_x['a'].update(dict_y['a'])
print(f"Question 62 Result: {dict_x}")

# --- Question 63: Set of Lists? (Trick Question) ---
# Problem: Why can't we have a set of lists like {[1, 2]}?
# Answer: Lists are mutable (unhashable). We must use tuples.
safe_set = {(1, 2), (3, 4)}
print(f"Question 63 Info: We use tuples because they are hashable.")

# --- Question 64: Finding Max Key in Dictionary ---
# Problem: Find the alphabetically largest key.
names_map = {"Alice": 1, "Zebra": 2, "Bob": 3}
max_key = max(names_map.keys())
print(f"Question 64 Result: {max_key}")

# --- Question 65: Sum of Values in Dictionary ---
# Problem: Sum all numeric values in {'a': 100, 'b': 200}.
prices = {'apple': 1.5, 'banana': 2.0, 'cherry': 5.0}
total_cost = sum(prices.values())
print(f"Question 65 Result: {total_cost}")

# --- Question 66: Extracting Sub-dictionary ---
# Problem: Create a new dict with keys ['a', 'c'] from {'a': 1, 'b': 2, 'c': 3}.
full_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
target_keys = ['a', 'c']
subset_dict = {k: full_data[k] for k in target_keys if k in full_data}
print(f"Question 66 Result: {subset_dict}")

# --- Question 67: Set Equality ---
# Problem: Check if {1, 2, 3} equals {3, 2, 1}.
set_lhs = {1, 2, 3}
set_rhs = {3, 2, 1}
is_equal = set_lhs == set_rhs
print(f"Question 67 Result: {is_equal}")

# --- Question 68: Removing all Duplicate Words from a Sentence ---
# Problem: Print unique words from "the cat and the dog".
sentence = "the cat and the dog"
unique_words = set(sentence.split())
print(f"Question 68 Result: {unique_words}")

# --- Question 69: Dictionary with Range Keys ---
# Problem: Map (1, 10) to "Low", (11, 20) to "High".
range_map = {
    range(1, 11): "Low",
    range(11, 21): "High"
}
# Note: ranges aren't hashable, so we use tuples to represent ranges usually.
proper_range_map = {
    (1, 10): "Low",
    (11, 20): "High"
}
print(f"Question 69 Result: {proper_range_map}")

# --- Question 70: Set Pop Error Handling ---
# Problem: Safely pop from a set if it's not empty.
data_set = {1, 2}
item = data_set.pop() if data_set else None
print(f"Question 70 Result: {item}")

# --- Question 71: Tuple of Sets ---
# Problem: Store two sets inside a tuple.
sets_bundle = ({1, 2}, {3, 4})
print(f"Question 71 Result: {sets_bundle}")

# --- Question 72: Dict from List of Lists ---
# Problem: Convert [[1, 'a'], [2, 'b']] to a dictionary.
matrix_data = [[1, 'a'], [2, 'b']]
dict_matrix = {row[0]: row[1] for row in matrix_data}
print(f"Question 72 Result: {dict_matrix}")

# --- Question 73: Nested Set? (Trick Question) ---
# Problem: Can you have a set of sets?
# Answer: No, use frozenset.
set_of_frozensets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Question 73 Result: {set_of_frozensets}")

# --- Question 74: Counting Distinct Values in Dict ---
# Problem: How many unique values are in {'a':1, 'b':2, 'c':1}?
data_map = {'a': 1, 'b': 2, 'c': 1}
distinct_val_count = len(set(data_map.values()))
print(f"Question 74 Result: {distinct_val_count}")

# --- Question 75: Merging Sets with update() ---
# Problem: Add elements of {3, 4} to {1, 2} in-place.
s_base = {1, 2}
s_extra = {3, 4}
s_base.update(s_extra)
print(f"Question 75 Result: {s_base}")

# --- Question 76: Finding Common Keys in Multiple Dicts ---
# Problem: Find keys present in all three dicts.
d1, d2, d3 = {'a': 1}, {'a': 2, 'b': 3}, {'a': 5, 'c': 6}
common_keys = d1.keys() & d2.keys() & d3.keys()
print(f"Question 76 Result: {common_keys}")

# --- Question 77: Clearing keys starting with 'test' ---
# Problem: Remove keys starting with 'test' from {'test1': 1, 'id': 2}.
raw_data = {'test1': 1, 'test2': 10, 'user_id': 505}
filtered_data = {k: v for k, v in raw_data.items() if not k.startswith('test')}
print(f"Question 77 Result: {filtered_data}")

# --- Question 78: Set Intersection Update ---
# Problem: Modify s1 to only keep elements also in s2.
s1_mod = {1, 2, 3}
s2_mod = {2, 3, 4}
s1_mod.intersection_update(s2_mod)
print(f"Question 78 Result: {s1_mod}")

# --- Question 79: Mapping String Lengths ---
# Problem: Create a dict mapping words to their lengths for ['python', 'code'].
words = ['python', 'code', 'teacher']
length_map = {word: len(word) for word in words}
print(f"Question 79 Result: {length_map}")

# --- Question 80: Reversing a Dictionary ---
# Problem: Create a new dictionary with items in reverse order.
# (Note: Dicts are ordered by insertion since Python 3.7+)
ordered_dict = {'first': 1, 'second': 2, 'third': 3}
reversed_items = list(ordered_dict.items())[::-1]
reversed_dict = dict(reversed_items)
print(f"Question 80 Result: {reversed_dict}")
