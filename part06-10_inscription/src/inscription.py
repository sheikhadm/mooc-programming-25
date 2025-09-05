# Write your solution here
name = input('Who should i sign this to: ')
fle = input('where shall i save it: ')

with open(fle, 'w') as new_file:
    new_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
