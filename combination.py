class Ordering:
    def __init__(self, alist):
        self.alist = alist

    def combination(self):
        a = []
        for i in self.alist:
            b = str(i)
            for j in b:
                a.append(j)
                a.sort(reverse=True)
                # print(a)
        c = int("".join(a))
        print(c)


my_list = Ordering([11, 52, 5, 6, 511])
print(my_list.combination())

