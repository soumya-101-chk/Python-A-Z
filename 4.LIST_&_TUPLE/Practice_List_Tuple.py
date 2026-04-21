"""
Python Practice: List & Tuple (Teacher Edition)
Goal: Use descriptive variable names and clean code structure.
"""

# ==========================================
# PART 1: BASIC LIST OPERATIONS
# ==========================================

# --- Question 1: Basic List Creation ---
# Problem: Initialize an empty list and add the integers 1 through 5.
numbers_list = []
for value in range(1, 6):
    numbers_list.append(value)
print(f"Question 1 Result: {numbers_list}")

# --- Question 2: Accessing by Index ---
# Problem: From the list [10, 20, 30, 40], retrieve and print the third element.
sample_scores = [10, 20, 30, 40]
third_element = sample_scores[2]
print(f"Question 2 Result: {third_element}")

# --- Question 3: Modifying Elements ---
# Problem: Change the first element of ['apple', 'banana'] to 'cherry'.
fruit_collection = ['apple', 'banana']
fruit_collection[0] = 'cherry'
print(f"Question 3 Result: {fruit_collection}")

# --- Question 4: List Length ---
# Problem: Calculate the total number of items in the list [1, 2, 3, 4, 5, 6].
data_points = [1, 2, 3, 4, 5, 6]
total_count = len(data_points)
print(f"Question 4 Result: {total_count}")

# --- Question 5: Removing the Last Item ---
# Problem: Remove the final element from the list [1, 2, 3].
simple_sequence = [1, 2, 3]
simple_sequence.pop()
print(f"Question 5 Result: {simple_sequence}")

# --- Question 6: Reversing a List ---
# Problem: Reverse the order of elements in [1, 2, 3, 4].
ordered_list = [1, 2, 3, 4]
ordered_list.reverse()
print(f"Question 6 Result: {ordered_list}")

# --- Question 7: Sorting Data ---
# Problem: Sort the list [5, 2, 9, 1] in ascending order.
unsorted_numbers = [5, 2, 9, 1]
unsorted_numbers.sort()
print(f"Question 7 Result: {unsorted_numbers}")

# --- Question 8: Counting Occurrences ---
# Problem: Count how many times the number 2 appears in [1, 2, 3, 2, 4, 2].
repeated_numbers = [1, 2, 3, 2, 4, 2]
occurrence_count = repeated_numbers.count(2)
print(f"Question 8 Result: {occurrence_count}")

# --- Question 9: Finding an Index ---
# Problem: Find the position (index) of 'blue' in the list ['red', 'green', 'blue'].
color_palette = ['red', 'green', 'blue']
blue_index = color_palette.index('blue')
print(f"Question 9 Result: {blue_index}")

# --- Question 10: Clearing a List ---
# Problem: Remove all elements from the list [1, 2, 3] so it becomes empty.
temporary_list = [1, 2, 3]
temporary_list.clear()
print(f"Question 10 Result: {temporary_list}")

# --- Question 11: List Concatenation ---
# Problem: Combine two lists [1, 2] and [3, 4] into a single list.
first_half = [1, 2]
second_half = [3, 4]
combined_list = first_half + second_half
print(f"Question 11 Result: {combined_list}")

# --- Question 12: List Repetition ---
# Problem: Create a new list that repeats [1, 2] three times.
base_pattern = [1, 2]
repeated_pattern = base_pattern * 3
print(f"Question 12 Result: {repeated_pattern}")

# --- Question 13: Membership Testing ---
# Problem: Check if the number 10 is present in the list [5, 10, 15].
search_list = [5, 10, 15]
is_present = 10 in search_list
print(f"Question 13 Result: {is_present}")

# --- Question 14: Basic Slicing ---
# Problem: Extract the first three elements from [10, 20, 30, 40, 50].
large_list = [10, 20, 30, 40, 50]
first_three = large_list[:3]
print(f"Question 14 Result: {first_three}")

# --- Question 15: Range Slicing ---
# Problem: Extract elements from index 2 to 4 (inclusive of 4).
data_range = [10, 20, 30, 40, 50]
middle_slice = data_range[2:5]
print(f"Question 15 Result: {middle_slice}")

# --- Question 16: Negative Indexing ---
# Problem: Use negative indexing to get the last two elements of a list.
price_list = [10, 20, 30, 40, 50]
last_two_items = price_list[-2:]
print(f"Question 16 Result: {last_two_items}")

# --- Question 17: Inserting at a Position ---
# Problem: Insert the number 25 at the third position (index 2) in [10, 20, 30].
target_list = [10, 20, 30]
target_list.insert(2, 25)
print(f"Question 17 Result: {target_list}")

# --- Question 18: Extending a List ---
# Problem: Append all elements of [3, 4] to the end of [1, 2] using extend.
main_list = [1, 2]
extra_elements = [3, 4]
main_list.extend(extra_elements)
print(f"Question 18 Result: {main_list}")

# --- Question 19: Statistics (Max/Min) ---
# Problem: Find the maximum and minimum values in the list [4, 1, 8, 2].
stats_list = [4, 1, 8, 2]
max_val = max(stats_list)
min_val = min(stats_list)
print(f"Question 19 Result: Max={max_val}, Min={min_val}")

# --- Question 20: Calculating Sum ---
# Problem: Calculate the sum of all elements in [10, 20, 30].
inventory_values = [10, 20, 30]
total_sum = sum(inventory_values)
print(f"Question 20 Result: {total_sum}")

# ==========================================
# PART 2: INTERMEDIATE LIST TECHNIQUES
# ==========================================

# --- Question 21: List Comprehension (Squares) ---
# Problem: Use a list comprehension to create a list of squares for numbers 1 to 10.
squares_list = [number**2 for number in range(1, 11)]
print(f"Question 21 Result: {squares_list}")

# --- Question 22: Filtering Evens ---
# Problem: Filter out only the even numbers from [1, 2, 3, 4, 5, 6].
mixed_numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in mixed_numbers if num % 2 == 0]
print(f"Question 22 Result: {even_numbers}")

# --- Question 23: Type Conversion ---
# Problem: Convert a list of strings ['1', '2', '3'] into a list of integers.
string_digits = ['1', '2', '3']
integer_digits = [int(digit) for digit in string_digits]
print(f"Question 23 Result: {integer_digits}")

# --- Question 24: Finding Intersection ---
# Problem: Find elements that are common to both [1, 2, 3] and [2, 3, 4].
list_a = [1, 2, 3]
list_b = [2, 3, 4]
common_elements = [item for item in list_a if item in list_b]
print(f"Question 24 Result: {common_elements}")

# --- Question 25: Removing Duplicates ---
# Problem: Remove all duplicate values from [1, 2, 2, 3, 4, 4, 5].
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(duplicate_list))
print(f"Question 25 Result: {unique_list}")

# --- Question 26: List of Tuples ---
# Problem: Create a list of tuples where each tuple is (number, square) for 1 to 5.
number_square_pairs = [(x, x**2) for x in range(1, 6)]
print(f"Question 26 Result: {number_square_pairs}")

# --- Question 27: Flattening a List ---
# Problem: Flatten a 2D list [[1, 2], [3, 4]] into a 1D list [1, 2, 3, 4].
matrix_2d = [[1, 2], [3, 4]]
flattened_list = [element for sublist in matrix_2d for element in sublist]
print(f"Question 27 Result: {flattened_list}")

# --- Question 28: Second Smallest Element ---
# Problem: Find the second smallest unique element in the list [5, 2, 9, 1, 7].
raw_data = [5, 2, 9, 1, 7]
sorted_unique = sorted(list(set(raw_data)))
second_smallest = sorted_unique[1] if len(sorted_unique) > 1 else None
print(f"Question 28 Result: {second_smallest}")

# --- Question 29: Zipping Lists ---
# Problem: Combine [1, 2] and ['a', 'b'] into a list of pairs.
ids = [1, 2]
labels = ['a', 'b']
zipped_result = list(zip(ids, labels))
print(f"Question 29 Result: {zipped_result}")

# --- Question 30: Unzipping Data ---
# Problem: Take a list of tuples [(1, 'a'), (2, 'b')] and separate them into two lists.
tuple_data = [(1, 'a'), (2, 'b')]
unzipped_ids, unzipped_labels = zip(*tuple_data)
print(f"Question 30 Result: IDs={list(unzipped_ids)}, Labels={list(unzipped_labels)}")

# --- Question 31: Length Filtering ---
# Problem: Find all words longer than 3 characters in ['hi', 'hello', 'cat'].
vocabulary = ['hi', 'hello', 'cat']
long_words = [word for word in vocabulary if len(word) > 3]
print(f"Question 31 Result: {long_words}")

# --- Question 32: Value Mapping (Conditional) ---
# Problem: Replace all negative numbers in [1, -2, 3, -4] with 0.
raw_readings = [1, -2, 3, -4]
normalized_readings = [val if val > 0 else 0 for val in raw_readings]
print(f"Question 32 Result: {normalized_readings}")

# --- Question 33: Sorting by Key (Length) ---
# Problem: Sort the strings ['apple', 'kiwi', 'banana'] by their length.
fruits = ['apple', 'kiwi', 'banana']
sorted_by_length = sorted(fruits, key=len)
print(f"Question 33 Result: {sorted_by_length}")

# --- Question 34: Logical Check (All) ---
# Problem: Verify if all elements in [1, 2, 3] are positive.
positive_check_list = [1, 2, 3]
all_positive = all(x > 0 for x in positive_check_list)
print(f"Question 34 Result: {all_positive}")

# --- Question 35: Logical Check (Any) ---
# Problem: Check if any element in [5, 8, 12] is greater than 10.
threshold_list = [5, 8, 12]
any_greater_than_ten = any(x > 10 for x in threshold_list)
print(f"Question 35 Result: {any_greater_than_ten}")

# --- Question 36: Finding First Even Index ---
# Problem: Find the index of the first even number in [1, 3, 5, 8, 9].
search_data = [1, 3, 5, 8, 9]
first_even_index = next(idx for idx, val in enumerate(search_data) if val % 2 == 0)
print(f"Question 36 Result: {first_even_index}")

# --- Question 37: List Splitting ---
# Problem: Split the list [1, 2, 3, 4, 5, 6] into two equal halves.
full_list = [1, 2, 3, 4, 5, 6]
middle_point = len(full_list) // 2
left_half = full_list[:middle_point]
right_half = full_list[middle_point:]
print(f"Question 37 Result: Left={left_half}, Right={right_half}")

# --- Question 38: Interleaving Elements ---
# Problem: Interleave two lists [1, 3] and [2, 4] to get [1, 2, 3, 4].
evens = [2, 4]
odds = [1, 3]
interleaved = [val for pair in zip(odds, evens) for val in pair]
print(f"Question 38 Result: {interleaved}")

# --- Question 39: String Prefix Counting ---
# Problem: Count how many strings start with 'a' in ['apple', 'berry', 'abc'].
word_list = ['apple', 'berry', 'abc']
starts_with_a_count = len([w for w in word_list if w.startswith('a')])
print(f"Question 39 Result: {starts_with_a_count}")

# --- Question 40: Cumulative Sum ---
# Problem: Calculate the cumulative sum of [1, 2, 3, 4] (result: [1, 3, 6, 10]).
input_list = [1, 2, 3, 4]
cumulative_list = []
current_sum = 0
for value in input_list:
    current_sum += value
    cumulative_list.append(current_sum)
print(f"Question 40 Result: {cumulative_list}")

# ==========================================
# PART 3: ADVANCED DATA STRUCTURES
# ==========================================

# --- Question 41: Generating Sublists ---
# Problem: Generate all possible sublists of [1, 2].
base_list = [1, 2]
all_sublists = [base_list[i:j] for i in range(len(base_list)) for j in range(i+1, len(base_list)+1)]
print(f"Question 41 Result: {all_sublists}")

# --- Question 42: Left Rotation ---
# Problem: Rotate the list [1, 2, 3, 4, 5] left by 2 positions.
rotate_me = [1, 2, 3, 4, 5]
shift_amount = 2
left_rotated = rotate_me[shift_amount:] + rotate_me[:shift_amount]
print(f"Question 42 Result: {left_rotated}")

# --- Question 43: Finding Mode ---
# Problem: Find the most frequent element in [1, 2, 3, 2, 2, 4].
frequency_data = [1, 2, 3, 2, 2, 4]
most_frequent = max(set(frequency_data), key=frequency_data.count)
print(f"Question 43 Result: {most_frequent}")

# --- Question 44: Custom Partitioning ---
# Problem: Partition [1, 2, 3, 4, 5, 6] such that even numbers come first.
source_numbers = [1, 2, 3, 4, 5, 6]
evens_first = [x for x in source_numbers if x % 2 == 0] + [x for x in source_numbers if x % 2 != 0]
print(f"Question 44 Result: {evens_first}")

# --- Question 45: Grouping by Parity ---
# Problem: Group [1, 2, 3, 4] into a dictionary of 'even' and 'odd' keys.
raw_integers = [1, 2, 3, 4]
parity_groups = {
    'even': [x for x in raw_integers if x % 2 == 0],
    'odd': [x for x in raw_integers if x % 2 != 0]
}
print(f"Question 45 Result: {parity_groups}")

# --- Question 46: Matrix Transposition ---
# Problem: Transpose the matrix [[1, 2], [3, 4]].
orig_matrix = [[1, 2], [3, 4]]
transposed_matrix = [list(column) for column in zip(*orig_matrix)]
print(f"Question 46 Result: {transposed_matrix}")

# --- Question 47: Finding a Missing Number ---
# Problem: Given a list of numbers 1-10 with one missing, find the missing one.
incomplete_range = [1, 2, 3, 4, 6, 7, 8, 9, 10]
full_set = set(range(1, 11))
missing_number = list(full_set - set(incomplete_range))[0]
print(f"Question 47 Result: {missing_number}")

# --- Question 48: Multiple Intersection ---
# Problem: Find the common elements among three lists.
lists_to_intersect = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
common_to_all = list(set.intersection(*map(set, lists_to_intersect)))
print(f"Question 48 Result: {common_to_all}")

# --- Question 49: List Difference ---
# Problem: Find elements in List 1 that are NOT in List 2.
list_one = [1, 2, 3, 4]
list_two = [2, 4]
difference_list = [item for item in list_one if item not in list_two]
print(f"Question 49 Result: {difference_list}")

# --- Question 50: Selective Removal ---
# Problem: Remove all occurrences of the value 2 from [1, 2, 3, 2, 4, 2].
data_to_clean = [1, 2, 3, 2, 4, 2]
cleaned_data = [item for item in data_to_clean if item != 2]
print(f"Question 50 Result: {cleaned_data}")

# --- Question 51: Maximum String Length ---
# Problem: Find the length of the longest string in ['a', 'abc', 'ab'].
strings_to_check = ['a', 'abc', 'ab']
max_length = max(len(s) for s in strings_to_check)
print(f"Question 51 Result: {max_length}")

# --- Question 52: Palindrome Check ---
# Problem: Determine if the list [1, 2, 3, 2, 1] is a palindrome.
potential_palindrome = [1, 2, 3, 2, 1]
is_palindrome = potential_palindrome == potential_palindrome[::-1]
print(f"Question 52 Result: {is_palindrome}")

# --- Question 53: Merging Sorted Lists ---
# Problem: Merge two sorted lists into a single sorted list.
sorted_left = [1, 3, 5]
sorted_right = [2, 4, 6]
merged_sorted = sorted(sorted_left + sorted_right)
print(f"Question 53 Result: {merged_sorted}")

# --- Question 54: Step Extraction ---
# Problem: Extract every 3rd element from the list 1 to 9.
full_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
step_slice = full_sequence[::3]
print(f"Question 54 Result: {step_slice}")

# --- Question 55: Content Filtering ---
# Problem: Filter strings that contain the letter 'e' from ['apple', 'banana', 'kiwi'].
fruit_list = ['apple', 'banana', 'kiwi']
fruits_with_e = [f for f in fruit_list if 'e' in f]
print(f"Question 55 Result: {fruits_with_e}")

# --- Question 56: Multi-Index Modification ---
# Problem: Update elements at indices 1 and 3 of [0, 0, 0, 0, 0] to 1.
zeros_list = [0, 0, 0, 0, 0]
indices_to_change = [1, 3]
for idx in indices_to_change:
    zeros_list[idx] = 1
print(f"Question 56 Result: {zeros_list}")

# --- Question 57: Counting Sublists ---
# Problem: Count how many elements in [1, [2, 3], 4, [5]] are themselves lists.
mixed_types = [1, [2, 3], 4, [5]]
sublist_count = sum(1 for item in mixed_types if isinstance(item, list))
print(f"Question 57 Result: {sublist_count}")

# --- Question 58: Case-Insensitive Sorting ---
# Problem: Sort ['banana', 'Apple', 'cherry'] ignoring uppercase/lowercase.
words_to_sort = ['banana', 'Apple', 'cherry']
properly_sorted = sorted(words_to_sort, key=str.lower)
print(f"Question 58 Result: {properly_sorted}")

# --- Question 59: Cleaning Empty Strings ---
# Problem: Remove empty or whitespace-only strings from ['a', '', 'b', ' '].
dirty_strings = ['a', '', 'b', ' ']
clean_strings = [s for s in dirty_strings if s.strip()]
print(f"Question 59 Result: {clean_strings}")

# --- Question 60: Calculating Product ---
# Problem: Find the product of all elements in [1, 2, 3, 4].
multipliers = [1, 2, 3, 4]
running_product = 1
for factor in multipliers:
    running_product *= factor
print(f"Question 60 Result: {running_product}")

# ==========================================
# PART 4: TUPLES & IMMUTABILITY
# ==========================================

# --- Question 61: Tuple Creation ---
# Problem: Create a tuple with values 1, 2, and 3.
constant_tuple = (1, 2, 3)
print(f"Question 61 Result: {constant_tuple}")

# --- Question 62: Tuple Access ---
# Problem: Access the second element of the tuple (10, 20, 30).
data_tuple = (10, 20, 30)
second_val = data_tuple[1]
print(f"Question 62 Result: {second_val}")

# --- Question 63: List to Tuple ---
# Problem: Convert the list [1, 2, 3] into a tuple.
mutable_list = [1, 2, 3]
immutable_tuple = tuple(mutable_list)
print(f"Question 63 Result: {immutable_tuple}")

# --- Question 64: Tuple to List ---
# Problem: Convert the tuple (1, 2, 3) back into a list.
source_tuple = (1, 2, 3)
result_list = list(source_tuple)
print(f"Question 64 Result: {result_list}")

# --- Question 65: Membership in Tuple ---
# Problem: Check if the string 'a' exists in ('a', 'b', 'c').
char_tuple = ('a', 'b', 'c')
found_a = 'a' in char_tuple
print(f"Question 65 Result: {found_a}")

# --- Question 66: Finding Tuple Index ---
# Problem: Find the index of the number 2 in the tuple (1, 2, 3).
search_tuple = (1, 2, 3)
index_of_two = search_tuple.index(2)
print(f"Question 66 Result: {index_of_two}")

# --- Question 67: Counting in Tuples ---
# Problem: Count occurrences of 1 in the tuple (1, 2, 1, 3).
frequency_tuple = (1, 2, 1, 3)
one_count = frequency_tuple.count(1)
print(f"Question 67 Result: {one_count}")

# --- Question 68: Tuple Concatenation ---
# Problem: Merge two tuples (1, 2) and (3, 4).
left_tuple = (1, 2)
right_tuple = (3, 4)
merged_tuple = left_tuple + right_tuple
print(f"Question 68 Result: {merged_tuple}")

# --- Question 69: Single Element Tuple ---
# Problem: Create a tuple with only one element (number 5).
single_item_tuple = (5,)
print(f"Question 69 Result: {single_item_tuple}, Type={type(single_item_tuple)}")

# --- Question 70: Unpacking Tuples ---
# Problem: Unpack the tuple (1, 2, 3) into variables first, second, and third.
coordinate_tuple = (1, 2, 3)
first_coord, second_coord, third_coord = coordinate_tuple
print(f"Question 70 Result: {first_coord}, {second_coord}, {third_coord}")

# --- Question 71: Swapping with Tuples ---
# Problem: Swap two variables 'val_a' and 'val_b' without using a temp variable.
val_a, val_b = 100, 200
val_a, val_b = val_b, val_a
print(f"Question 71 Result: val_a={val_a}, val_b={val_b}")

# --- Question 72: Tuple Reversal ---
# Problem: Reverse the elements of a tuple (1, 2, 3).
original_tuple = (1, 2, 3)
reversed_tuple = original_tuple[::-1]
print(f"Question 72 Result: {reversed_tuple}")

# --- Question 73: Nested Tuple Access ---
# Problem: Access the first element of the inner tuple in (1, (2, 3), 4).
nested_tuple = (1, (2, 3), 4)
inner_first_val = nested_tuple[1][0]
print(f"Question 73 Result: {inner_first_val}")

# --- Question 74: List of Tuples to Dict ---
# Problem: Convert [('a', 1), ('b', 2)] into a dictionary.
pairs_list = [('a', 1), ('b', 2)]
dict_from_tuples = dict(pairs_list)
print(f"Question 74 Result: {dict_from_tuples}")

# --- Question 75: Tuple Length ---
# Problem: Find how many items are in (1, 2, 3, 4).
counting_tuple = (1, 2, 3, 4)
tuple_size = len(counting_tuple)
print(f"Question 75 Result: {tuple_size}")

# --- Question 76: Sum of Tuple ---
# Problem: Calculate the sum of elements in (10, 20, 30).
values_tuple = (10, 20, 30)
total_sum_val = sum(values_tuple)
print(f"Question 76 Result: {total_sum_val}")

# --- Question 77: Max Value in Tuple ---
# Problem: Find the largest number in (5, 12, 3).
numerical_tuple = (5, 12, 3)
max_val_tuple = max(numerical_tuple)
print(f"Question 77 Result: {max_val_tuple}")

# --- Question 78: Homogeneous Type Check ---
# Problem: Check if all elements in a tuple are of type 'str'.
mixed_types_tuple = ('apple', 'banana', 'cherry')
is_all_strings = all(isinstance(item, str) for item in mixed_types_tuple)
print(f"Question 78 Result: {is_all_strings}")

# --- Question 79: Tuple Multiplier ---
# Problem: Multiply a tuple (1, 2) by 2.
seed_tuple = (1, 2)
multiplied_tuple = seed_tuple * 2
print(f"Question 79 Result: {multiplied_tuple}")

# --- Question 80: String to Tuple ---
# Problem: Convert the string 'hello' into a tuple of individual characters.
input_string = 'hello'
character_tuple = tuple(input_string)
print(f"Question 80 Result: {character_tuple}")
