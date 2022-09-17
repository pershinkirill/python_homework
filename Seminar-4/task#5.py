# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.



#reading the data from file.txt
frst_prt = open("task#5-1.txt", "r")
frst_prt = frst_prt.readline()
print("First Polynomial", type(frst_prt))
frst_prt_lst = frst_prt.split()

print(frst_prt_lst)

scnd_prt = open("task#5-2.txt", "r")
scnd_prt = scnd_prt.readline()
print("Second Polynomial", scnd_prt)

#result = open("task#5-3.txt", "w")
#result = result.writelines(str(res))
