from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(_("Categoría"), max_length=100, unique=True)
    slug = models.SlugField(_("Slug"), unique=True)
    subcategory_of = models.ForeignKey("api.Category", verbose_name=_("Sub categoría de"), on_delete=models.CASCADE, blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_("Nombre"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    description = models.TextField(_("Descripción"))
    category = models.ForeignKey(Category, verbose_name=_("Categoría"), on_delete=models.SET_NULL, blank=True, null=True)
    price = models.DecimalField(_("Precio"), max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(_("Fecha de creación"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Última modificación"), auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Producto"), on_delete=models.CASCADE, related_name="products")
    color = models.CharField(_("Color"), max_length=50)
    discount = models.FloatField(_("Descuento"), validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f'{self.product.name} - {self.color}'


class ProductImage(models.Model):
    productvariant = models.ForeignKey(ProductVariant, verbose_name=_("Producto"), related_name='productimages', on_delete=models.CASCADE)
    image = models.ImageField(_("Imagen"), upload_to='media/products/')
    

class ProductSize(models.Model):
    productvariant = models.ForeignKey(ProductVariant, verbose_name=_("Variante Producto"), related_name='productsizes', on_delete=models.CASCADE)
    size  = models.CharField(_("Talla"), max_length=50)
    stock = models.PositiveIntegerField(_("Cantidad"), default=0)

    class Meta:
        unique_together = [['productvariant', 'size']]

    def __str__(self):
        return f'{self.productvariant.product.name} - {self.productvariant.color} - {self.size}'


class Order(models.Model):
    productsize = models.ForeignKey(ProductSize, verbose_name=_("Talla Variante Producto"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("Usuario"), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_("Cantidad"))


@receiver(pre_save, sender=Order)
def order_pre_save_receiver(sender, instance, **kwargs):

    if (Order.objects.filter(pk=instance.pk)):
        print('test')
    else:
        if instance.quantity <= instance.productsize.stock:
            instance.productsize.stock -= instance.quantity
            instance.productsize.save()
        else:
            raise BaseException()