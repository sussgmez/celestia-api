from django.contrib import admin
from .models import Product, ProductImage, ProductSize, ProductVariant, Order, Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductSizeInline(admin.TabularInline):
    model = ProductSize

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductSizeInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


