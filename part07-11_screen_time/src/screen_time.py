# Write your solution here
# from datetime import datetime, timedelta

# fn = input('Filename: ')
# sd = input('Starting date: ')
# day = int(input('How many days: '))
# print('Please type in screen time in minutes on each day (TV computer mobile):')
# c = timedelta(days= day - 1)
# finish = datetime.strptime(sd, '%d.%m.%Y') + c
# dif = finish - datetime.strptime(sd,'%d.%m.%Y')
# total = dif.total_seconds()
# with open(fn,'w') as new_file:
#     new_file.write(f'Time period: {sd}-{finish.strftime("%d.%m.%Y")}\n')
#     new_file.write(f'Total minutes: {(int(total)% 3600)//60}\n')
#     new_file.write(f'Average minutes: {(int(total)//60)/ day}\n')
# one_day = timedelta(days = 1)
# for x in range(day):
#     st = input(f'Screen time {sd}:')
#     st= st.split(' ')
#     with open(fn,'a') as new_file:
#         new_file.write(f'{sd}: {'/'.join(st)}\n')
#     new_date = datetime.strptime(sd, '%d.%m.%Y') + one_day
#     sd = new_date.strftime("%d.%m.%Y")
# print(f'Data stored in file {fn}')

from datetime import datetime, timedelta

fn = input('Filename: ')
sd_input = input('Starting date: ')
day = int(input('How many days: '))
print('Please type in screen time in minutes on each day (TV computer mobile):')

# Convert start date to datetime for consistent formatting
start_dt = datetime.strptime(sd_input, '%d.%m.%Y')
finish = start_dt + timedelta(days=day - 1)

total_minutes = 0
one_day = timedelta(days=1)
current_date = start_dt

# Store records to write later
records = []

for x in range(day):
    st = input(f"Screen time {current_date.strftime('%d.%m.%Y')}: ")
    tv, comp, mob = map(int, st.split())
    total_minutes += (tv + comp + mob)
    records.append(f"{current_date.strftime('%d.%m.%Y')}: {tv}/{comp}/{mob}\n")
    current_date += one_day

# Write to file
with open(fn, 'w') as new_file:
    new_file.write(f"Time period: {start_dt.strftime('%d.%m.%Y')}-{finish.strftime('%d.%m.%Y')}\n")
    new_file.write(f"Total minutes: {total_minutes}\n")
    new_file.write(f"Average minutes: {total_minutes / day:.1f}\n")
    for rec in records:
        new_file.write(rec)

print(f"Data stored in file {fn}")
