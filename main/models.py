from django.db import models


class AutoMark(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Марка авто"
        verbose_name_plural = "Марки авто"

    def __str__(self):
        return self.name


class AutoPartCategory(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Категория запчастей"
        verbose_name_plural = "Категории запчастей"

    def __str__(self):
        return self.name


class AutoPart(models.Model):
    auto_mark = models.ForeignKey(AutoMark, on_delete=models.CASCADE)
    auto_part_category = models.ForeignKey(AutoPartCategory, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2048)
    image = models.ImageField(upload_to='auto_part/images')
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Авто запчасть"
        verbose_name_plural = "Авто запчасти"
