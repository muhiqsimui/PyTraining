

variable=[i for i in range(100) if i%2==0]

#python code to same variable to file format txt
with open("namafile.txt", "w") as x:
    x.write(str(variable))
