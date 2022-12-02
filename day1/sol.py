elf_cals = []
rolling_sum = 0

with open('input.txt') as f:
    lines = f.readlines()
    
for l in lines:
    # print(l)
    l = l.strip()
    if l == "":
        elf_cals.append(rolling_sum)
        rolling_sum = 0
    else:
        rolling_sum += int(l)

print("Highest Calories:", max(elf_cals))
print("Top 3:", sum(sorted(elf_cals)[-3:]))