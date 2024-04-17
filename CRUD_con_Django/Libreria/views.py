from django.shortcuts import render, redirect
from Libreria.models import Books
from Libreria.modelsforms import BookForm

def start(request):
    return render(request, 'index.html')


def us(request):
    return render(request, 'us.html')


def list_books(request):
    # Obtenemos todos los libros de la tabla Books.
    all_books = Books.objects.all()
    return render(request, 'books/list_books.html', {'books': all_books})


def create_book(request):
    books_form = BookForm(request.POST or None, request.FILES or None)
    if books_form.is_valid() and request.POST:
        books_form.save()
        return redirect(list_books)
    return render(request, 'books/create_book.html', {'form': books_form})


def edit_book(request, book_id):
    book = Books.objects.get(id=book_id)
    books_form = BookForm(request.POST or None, 
                           request.FILES or None, 
                           instance=book)
    
    if books_form.is_valid() and request.POST:
        books_form.save()
        return redirect(list_books)

    return render(request, 'books/edit_book.html', {'form': books_form})


def delete_book(request, book_id):
    book = Books.objects.get(id=book_id)
    book.delete()
    return redirect(list_books)