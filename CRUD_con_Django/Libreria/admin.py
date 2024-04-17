from django.contrib import admin
from Libreria.models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')

# Registrar los modelos para su administración.
admin.site.register(Books, BooksAdmin)