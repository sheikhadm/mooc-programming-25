# WRITE YOUR SOLUTION HERE:
class ListHelper:
    def __init__(self):
        pass

    
    @classmethod
    def greatest_frequency(cls,my_list:list):
        """Return the item with the highest frequency in the list."""
        if not my_list:
            return None  # handle empty list safely
        
        # Count occurrences using a dictionary
        counts = {}
        for item in my_list:
            counts[item] = counts.get(item, 0) + 1
        
        # Find the key (item) with the maximum value (count)
        return max(counts, key=counts.get)
    
    @classmethod
    def doubles(cls, my_list: list):
        """Return the number of unique items that appear at least twice."""
        counts = {}
        for item in my_list:
            counts[item] = counts.get(item, 0) + 1
        
        # Count how many have frequency >= 2
        return sum(1 for count in counts.values() if count >= 2)

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))

