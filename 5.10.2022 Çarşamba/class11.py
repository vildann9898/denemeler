class Math:

    @staticmethod # decorator
    def add5(x):
        return x+5

    @staticmethod
    def add10(x):
        return x+10

    @staticmethod
    def yazdir():
        print("yazdırıyorum..")

Math.yazdir()
print(Math.add10(10))
