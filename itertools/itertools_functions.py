import itertools
import operator

# Use of itertool.accumulate() function
def accumulate_usage():
    data = [1,2,8,3,4,5] 

    # Multiply items with result
    multipy_result = itertools.accumulate(data, operator.mul) 

    # Find Max Values
    max_result = itertools.accumulate(data,max)

    # If no function, sum is returned
    result = itertools.accumulate(data)
    for res in result:
        print(res)

# Use of itertool.combinations()
def combinations_usage():
    random_people = ["Edward","June", "Monica","Hirally","Mascot", "Threza"]

    # This allowes to make combinations with replacement, ie Have individual elements grouped more than once
    # Edward and Edward can be grouped together

    results_with_replacement = itertools.combinations_with_replacement(random_people, 2)

    # Make combinations of two people, we could make more.
    mingle_results = itertools.combinations(random_people,2)
    for grp in mingle_results:
        print(grp)

# Use this to return evenly spaced values starting with start number applying step number provided
def count_usage():
    for i in itertools.count(0, 3):
        print(i)
        if i >= 33:
            break

# Use cycle to traverse the list endlessly
def cycle_usage():
    data = ["Start Work","Finish LT", "Call Client", "Schedule Meeting", "Meet CEO", "Go Home"]
    for task in itertools.cycle(data):
        print(task)

# Use chain to put together two iterables, get a series of iterables and returns one long iterable
def chain_usage():
    data1 = ["Blue", "Black", "Orange", "Red", "Yellow"]
    data2 = ["Iphone", "BlackBerry", "Windows 10", "Red Hat"]

    chained_result = itertools.chain(data1, data2)

    for data in chained_result:
        print(data)

# Use compress() to filter one iterable with another
def compress_usage():
    data1 = ["Nokia","Windows","Football","Linux"]
    data2 = [True,False,False,True]

    compress_result = itertools.compress(data1, data2)
    for data in compress_result:
        print(data)

# Use dropwhile() to drop elements from iterable if condtionis true, return remaining elements.
# for better performance, sort iterable first
def dropwhile_usage():
    data = [1,3,5,8,9,10,56,89]

    result = itertools.dropwhile(lambda x: x < 8, data)
    for res in result:
        print(res)


# use filterfalse() to return iterator with elements from passed iterator whose predicate is False
# itertools.filterfalse(predicate, iterable)

def filterfalse_usage():
    data = [1,2,3,4,5,6,7,8,9,10]
    result = itertools.filterfalse(lambda x: x<5, data)
    for res in result:
        print(res)

# Use groupby() to group iterables
# Groups Last element alone, does not include it in first grouping of
# Software Developers. Try Sort first may be!
def groupby_usage():
    robots = [
        {
            'name': 'Edward',
            'role': 'Software Developer'
        },
        {
            'name': 'Herbert',
            'role': 'Software Developer'
        },
        {
            'name': 'Arthur',
            'role': 'Graphics Designer'
        },
        {
            'name': 'Daniel',
            'role': 'Graphics Designer',
        },
        {
            'name': 'Anita',
            'role': 'Sales'
        },
        {
            'name': 'Julie',
            'role': 'Sales'
        },
        {
            'name': 'Rita',
            'role': 'Software Developer'
        }
    ]

    for key, group in itertools.groupby(robots, key=lambda x: x['role']):
        print(key)
        print(list(group))

# Use islice to cut out a part of iterable
# Works much like slice

def islice_usage():
    data = ["Python", "Solidity", "Rust", "Java"]
    result = itertools.islice(data, 3)
    for res in result:
        print(res)

# Use permutations() to create well ..., permutations!!
def permutations_usage():
    data = ['Edward', 27, 'Tim', 22, 'Tevin', 14]
    result = itertools.permutations(data)
    for res in result:
        print(res)

# Use product() to create cartesian products from a series of iterables
def product_usage():
    data = [1,2,3,4,5]
    data1 = ['a','b','c','d','e']

    result = itertools.product(data, data1)
    for res in result:
        print(res)

# Use repeat() to repeat an object endlessly, unless times arg is passed

def repeat_usage():
    # for command in itertools.repeat("Get me Eggs"): Repeated endlessly
    for command in itertools.repeat("Get me Eggs", 2): #Repeated 2 times
        print(command)

# Use starmap() to make an iterator that computes the function
# using args from iterable
def starmap_usage():
    data = [(2,7),(2,11), (2,13.5)]
    result = itertools.starmap(operator.mul, data)
    for res in result:
        print(res)

# Use takewhile() to return elements from iterable if predicate is True
# itertools.takewhile(predicate, iterable) opposite of dropwhile()
# ..Does not, include 4 in results, ends at 34...again need to first sort 
def takewhile_usage():
    data = [1,2,34,4,5,6,7,9]
    result = itertools.takewhile(lambda x: x<5, data)
    for res in result:
        print(res)

# Use tee() to create n independent iterators from a single iterable
#creating more than 2 fails....why??
def tee_usage():
    data = ["Ed", "Ro", "He"]
    data1, data2 = itertools.tee(data)

    print("----Data1----")
    for res in data1:
        print(res)
    
    print("----Data2----")
    for res in data2:
        print(res)

# Use zip_longest() to make iterator that aggregates elements from each of
# the iterables, missing values filled in with fillvalue arg
# itertools.zip_longest(*iterables, fillvalue=None)

def zip_longest_usage():
    data = ["red", "blue", "aqua", "sliq", "Brown", "Black"]
    data1 = [1,2,3,4]

    for res in itertools.zip_longest(data, data1, fillvalue=None):
        print(res)


if __name__ == '__main__':
    zip_longest_usage()