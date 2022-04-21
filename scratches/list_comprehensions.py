numbers = [1,2,3]
new_num_list = []
for n in numbers:
    new_num_list.append(n + 1)

print(new_num_list)

better_new_num_list = [n + 1 for n in numbers]

print(better_new_num_list)

name = "Phill"
big_name = [x.upper() for x in name]

print(big_name)

num_challenge = [i * 2 for i in range(1,10)]
print(num_challenge)

even_num_challenge = [i * 2 for i in range(1,10) if i % 2 == 0]
print(even_num_challenge)