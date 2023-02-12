a = [1, 2, 3, 4, 5, 9, 11, 13, 12, 15, 19, 18, 25, 22, 45, 68, 57, 55, 46]
b = [1, 2, 3, 4, 8, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 25, 28, 29, 54, 45, 75, 57, 56, 65, 58, 85]

c = []
class overLape:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compare(self ):
        if len(self.a) > len(self.b):
            print("A is grater then B")
        elif len(self.b) > len(self.a):
            print("B is grater then A")
        else:
            print("Both are same ")

    def overList(self):
        if len(self.a) > len(self.b):
            print(f"length of A is {len(self.a)}")
        elif len(self.b) > len(self.a):
            #print(f"length of B is {len(self.b)}")
            for i in range(len(self.b)):
                try:
                    if self.b[i] == self.a[i]:
                        c.append(self.b[i])
                    elif self.b[i] >= self.a[i]:
                        c.append(self.b[i])
                        c.append(self.a[i])
                    elif self.a[i] >= self.b[i]:
                        c.append(self.a[i])
                        c.append(self.b[i])
                    else:
                        print("None")
                except:
                    c.append(self.b[i])
        else:
            print("Both A and B are same")


Olap = overLape(a,b)
Olap.compare()
Olap.overList()
print(c)
f_Olap = []
[f_Olap.append(x) for x in c if x not in f_Olap]
f_Olap.sort()
print(f_Olap)


