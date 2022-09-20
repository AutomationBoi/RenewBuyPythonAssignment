class DivisibleBySevenGenerator():
    def __init__(self,rangeLimit):
        self.rangeLimit=rangeLimit
        pass
    def numberGenerator(self):
        for i in range(0,self.rangeLimit):
            if i%7==0:
                yield i


if __name__=='__main__':
    obj=DivisibleBySevenGenerator(100)
    num = obj.numberGenerator()
    while True:
        try:
            val=next(num)
            print(val)
        except Exception as e:
            break