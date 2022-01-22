# Set - collection which is unordered , unindexed . no duplicate values


utensils = {"knife","spoon","fork","knife"}
dishes = {"plate","bowl","cup","knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)
#dishes.update(utensils)
#dinner_table = utensils.union(dishes)
print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))
#for i in dinner_table:
 #   print(i)