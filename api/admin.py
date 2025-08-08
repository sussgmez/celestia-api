from django.contrib import admin
from .models import Product, ProductImage, ProductSize, ProductVariant, Order, Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


