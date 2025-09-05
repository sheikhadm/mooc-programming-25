# Write your solution here
# Dictionary file name
filename = "dictionary.txt"

# Load existing entries from the file into a list
entries = []

try:
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if '-' in line:
                parts = line.split(' - ')
                if len(parts) == 2:
                    entries.append((parts[0], parts[1]))
except FileNotFoundError:
    pass  # If file doesn't exist, start with empty dictionary

# Main loop
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    choice = input("Function: ")

    if choice == "1":
        finnish = input("The word in Finnish: ").strip()
        english = input("The word in English: ").strip()
        entry = f"{finnish} - {english}"
        with open(filename, "a", encoding="utf-8") as file:
            file.write(entry + "\n")
        entries.append((finnish, english))
        print("Dictionary entry added")
    
    elif choice == "2":
        search = input("Search term: ").strip().lower()
        for finnish, english in entries:
            if search in finnish.lower() or search in english.lower():
                print(f"{finnish} - {english}")
    
    elif choice == "3":
        print("Bye!")
        break
    
    else:
        print("Unknown command.")

