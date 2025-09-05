# Write your solution here
from datetime import datetime

def is_it_valid(pic: str) -> bool:
    # Control character table
    control_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    
    # Check format length
    if len(pic) != 11:
        return False

    # Extract parts
    date_part = pic[:6]        # ddmmyy
    century_marker = pic[6]    # +, -, or A
    personal_id = pic[7:10]    # yyy
    control_char = pic[10].upper()  # z
    
    # Check century marker
    if century_marker not in ['+', '-', 'A']:
        return False
    
    # Determine full year
    yy = int(date_part[4:6])
    if century_marker == '+':
        year = 1800 + yy
    elif century_marker == '-':
        year = 1900 + yy
    else:  # 'A'
        year = 2000 + yy
    
    # Validate date
    try:
        datetime(year, int(date_part[2:4]), int(date_part[0:2]))
    except ValueError:
        return False

    # Check control character
    nine_digit_number = date_part + personal_id
    remainder = int(nine_digit_number) % 31
    if control_chars[remainder] != control_char:
        return False
    
    return True

if __name__ == "__main__":
    # Test examples
    print(is_it_valid("230827-906F"))  # True
    print(is_it_valid("120488+246L"))  # True
    print(is_it_valid("310823A9877"))  # True
    print(is_it_valid("310223A9878"))  # False (wrong control char)
