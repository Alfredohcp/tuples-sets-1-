#Ramon Saucedo and Alfredo Garcia
import requests
response = requests.get("https://randomuser.me/api")
#print(response.json())

gender = response.json()['results'][0]['gender']
print(gender)

title = response.json()['results'][0]['name']['title']
print(title)

first = response.json()['results'][0]['name']['first']
print(first)

last = response.json()['results'][0]['name']['last']
print(last)

postcode = response.json()['results'][0]['location']['postcode']
print(postcode)

timezone = response.json()['results'][0]['location']['timezone']
print(timezone)

username = response.json()['results'][0]['login']['username']
print(username)

date = response.json()['results'][0]['dob']['date']
print(date)

# Unique Elements:
# Given a list of integers, return a set containing only the unique integers.
# python
# Copy code
# example_input = [1, 2, 2, 3, 4, 4, 4]
# # Your code

# # Expected Output: {1, 2, 3, 4}
# Set Operations:
example_input = [1, 2, 2, 3, 4, 4, 4]
unique_elements = set(example_input)
print(unique_elements)

# Given two sets, perform the following operations:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Union
print(set1.union(set2))

# Intersection
print(set1.intersection(set2))

# Difference (Set 1 - Set 2)
print(set1.difference(set2))

# Given two sets, check if the first set is a subset of the second set.
# Remove Duplicates:
def isThis_subset(set1, set2):
  return set1.issubset(set2)


print(isThis_subset(set1, set2))
