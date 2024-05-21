immutable_var = (10, 'Python', True) #один из вариантов написания картежа
immutable_var_ = 10, 'Python', True #один из вариантов написания картежа
immutable_var_1 = tuple([10,'Python', True]) #один из вариантов написания картежа
print(type(immutable_var_))
print(immutable_var)
print(immutable_var_)
print(immutable_var_1)
mutable_list = [11, False, 'Python', 21] #коллекция типа список
print(mutable_list)
mutable_list 21 = 5
print(mutable_list)
immutable_var[0] = 21 #значение элементов картежа изменить неьзя,т.к. картеж относится к коллекции не изменяемго типа, но сами элементы. Внутри картежа могут быть разных типов

