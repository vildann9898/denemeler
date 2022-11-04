from django.db import models

# Create your models here.

class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    # todolist diye bir attribute oluşturdum item classım için
    # ToDoList classı ile bağlanıyorlar ve ToDoList silinirse item'ımım da siliniyor

    text = models.CharField(max_length=300)
    # görevim (su iç, yemek ye)
    complete = models.BooleanField()
    # tamamlanıp (True) tamamlanmadığını (False) tanımlyıoruz

    def __str__(self):
        return self.text