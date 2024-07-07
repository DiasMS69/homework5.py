immutable_var = tuple_ = 1, 2, 3, "red", "black"
print(immutable_var)
#immutable_var[2] = "true"
#print(immutable_var)
#Кортеж является неизменным типом данных,
#его можно менять только в случае,
#если внутри кортежа будет добавлен список.
mutable_list = ["pink", "green", "blue"]
print(mutable_list)
mutable_list[1] = "yellow"
print(mutable_list)
