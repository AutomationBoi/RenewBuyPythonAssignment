class DivisibleBySevenAndFiveGenerator():
    def __init__(self,rangeLimit):
        self.rangeLimit=rangeLimit
        pass
    def numberGenerator(self):
        for i in range(0,self.rangeLimit):
            if i%35==0:
                yield i


if __name__=='__main__':
    n=int(input('Enter the Number(n):'))
    obj=DivisibleBySevenAndFiveGenerator(n)
    num = obj.numberGenerator()
    while True:
        try:
            val=next(num)
            print(val)
        except Exception as e:
            break