"""
ID: benzhao1
LANG: PYTHON3
TASK: skidesign
"""
fin = open ('skidesign.in', 'r')
fout = open ('skidesign.out', 'w')

hill_amount = fin.readline()
hill_amount = int(hill_amount)

hill_heights = []

for i in range (hill_amount):
    height = fin.readline()
    hill_heights.append(int(height))
hill_heights.sort()

cost = 100000000000000000
print(hill_heights[0])
print(hill_heights[hill_amount - 1])

for i in range (hill_heights[hill_amount - 1] - hill_heights[0]):
    temp = []
    temp_cost = 0
    first = i + hill_heights[0]
    last = first + 17
    for j in range (hill_amount):
        temp.append(hill_heights[j])
    for k in range (hill_amount):
        if temp[k] < first:
            difference = first - temp[k]
            temp_cost = temp_cost + difference * difference
        elif temp[k] > last:
            difference2 = temp[k] - last
            temp_cost = temp_cost + difference2 * difference2
        elif first <= temp[k] <= last:
            continue
    if temp_cost < cost:
        cost = temp_cost



print(cost)


fout.write(str(cost) + '\n')
fout.close()