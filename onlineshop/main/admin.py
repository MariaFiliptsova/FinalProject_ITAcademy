from django.contrib import admin
from django.forms import ModelChoiceField

from .models import *


class VagonkaAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='vagonka'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class TerraceAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='terrace'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class DoskaPolaAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='doska-pola'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class BrusAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='brus'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class StairsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='stairs'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Vagonka, VagonkaAdmin)
admin.site.register(Terrace, TerraceAdmin)
admin.site.register(Stairs, StairsAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(DoskaPola, DoskaPolaAdmin)
admin.site.register(Brus, BrusAdmin)
