def filter_incorrect():
    # Clear the output file first
    with open('correct_numbers.csv', 'w') as f:
        pass  

    with open('lottery_numbers.csv') as infile:
        for line in infile:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            try:
                parts = line.split(';')
                cn = parts[0].split(' ')
                bon = parts[1].split(',')

                # Convert week number to int
                nt = int(cn[1])

                # Check there are exactly 7 numbers
                if len(bon) != 7:
                    continue

                numbers = []
                valid = True
                for x in bon:
                    num = int(x)
                    if num < 0 or num > 39 or num in numbers:
                        valid = False
                        break
                    numbers.append(num)

                if valid:
                    with open('correct_numbers.csv', 'a') as outfile:
                        outfile.write(f'{" ".join(cn)};{",".join(map(str, numbers))}\n')

            except (IndexError, ValueError):
                # Skip malformed lines
                continue


if __name__ == "__main__":
    filter_incorrect()
