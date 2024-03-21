from django.db import models

class Product(models.Model):
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    title = models.CharField(max_length=100, verbose_name='название')
    price = models.IntegerField(verbose_name='цена')
    content = models.TextField(verbose_name='описание')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='product', verbose_name='категория')
    tags = models.ManyToManyField('Tag', related_name='news', verbose_name='теги', blank=True)
    date = models.DateTimeField(verbose_name='дата добавление', auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='публичность')


    def __str__(self):
        return f'{self.title} - {self.price}'


class Image (models.Model):
    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'

    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='image')
    image = models.ImageField(upload_to='media/', null=True, verbose_name='фотографии')


class ProductAttribute(models.Model):
    class Meta:
        verbose_name='атрибут продукта'
        verbose_name_plural = 'атрибуты продуктов'
    
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='attributes')
    key = models.CharField(verbose_name='название', max_length=100)
    value = models.CharField(verbose_name='значение',max_length=100)
    link = models.URLField(verbose_name='ссылка', null=True, blank=True)


class Category(models.Model):

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    title = models.CharField(verbose_name='название', max_length=50, unique=True)

    def __str__(self):
        return f'{self.title}'



class Tag(models.Model):

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    title = models.CharField(verbose_name='название', max_length=50, unique=True)

    def __str__(self):
        return f'{self.title}'
