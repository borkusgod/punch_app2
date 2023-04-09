import random

with open("names_list.txt") as file_read:
    name_file = file_read.readlines()
    len_of_nf = len(name_file)

print(name_file)
print(len(name_file))

print(type(name_file[5]))
get_rand = random.randint(0, len_of_nf)
print(name_file[get_rand])

