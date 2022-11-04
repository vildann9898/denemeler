class Nokta():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.koordinat = (self.x, self.y)
    def __add__(self, p): # toplama dunder mothodu
        return Nokta(self.x + p.x, self.y + p.y)
    def __sub__(self, p): # çıkarma dunder methodu
        return Nokta(self.x - p.x, self.y - p.y)
    def __mul__(self, p): # çarpma dunder methodu
        return Nokta(self.x * p.x, self.y * p.y)

    def buyukluk(self):
        return (self.x**2 + self.y**2)**0.5
    def __gt__(self,p): # greater than ( büyüktür)
        return self.buyukluk() > p.buyukluk()
    def __ge__(self,p): # greater than or equal to (büyük eşittir)
        return self.buyukluk() >= p.buyukluk()
    def __lt__(self,p): # less than (küçüktür)
        return self.buyukluk() < p.buyukluk()
    def __le__(self,p): # less than or equal to (küçük eşittir)
        return self.buyukluk() <= p.buyukluk()
    def __eq__(self,p): # equal to
        return (self.x == p.x and self.y == p.y) or (self.x == p.y and self.y == p.x)
     

    def __str__(self): # printle yazdırmaya çalıştığımda yazmasını istediğim şey
        return f"({self.x}, {self.y})"

  
p1 = Nokta(3,4)
p2 = Nokta(4,3)
print(p1>p2)
print(p1<p2)
print(p1==p2)