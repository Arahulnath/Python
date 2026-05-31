#A set is also mutable
# it is unordered
# it doest have index position
#ir doent allow duplicate
a={"chennai","Andra","malasiya","chennai","coimbatore"}
print(a)
#it can add, remove , discard , but canot update beacue there is no index value
a.remove("chennai")
print(a)
a.add("Natrampalli")
print(a)
#if u need to update delete the items and add
a.remove("Natrampalli")
a.add("kandhili")
print(a)
a.discard("kandhili")
print(a)