# Write your solution here
def print_letter_square(layers):
    size = 2 * layers - 1
    for i in range(size):
        row = ''
        for j in range(size):
            layer = min(i, j, size - 1 - i, size - 1 - j)
            letter = chr(ord('A') + layers - 1 - layer)
            row += letter
        print(row)

# Example usage
layers = int(input("Layers: "))
if 1 <= layers <= 26:
    print_letter_square(layers)
else:
    print("Please enter a number between 1 and 26.")
