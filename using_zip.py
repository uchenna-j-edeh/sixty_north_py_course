from itertools import chain

sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]
tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]
for temps in zip(sunday, monday, tuesday):
#    print (item, " ", "Average =", sum(item)/len(item))
    print("min = {:4.1f}, max={:4.1f}, average={:4.1f}".format(min(temps), max(temps), sum(temps) / len(temps)))

# All temperature above freezing point?
temperatures = chain(sunday, monday, tuesday)
my_result = all(t > 0 for t in temperatures)
print(my_result)
