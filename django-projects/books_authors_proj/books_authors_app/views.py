from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        "all_the_books": Book.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    title = request.POST['title']
    desc = request.POST['desc']

    Book.objects.create(
        title=title,
        desc=desc
    )
    return redirect('/')

def show(request, number):
    book = Book.objects.get(id=number)
    context = {
        "book": book,
        "all_authors": Author.objects.all()
    }
    return render(request, "show.html", context)

def add_author(request, number):
    if request.method == "POST":
        book = Book.objects.get(id=number)
        author_id = request.POST.get("author_id")
        author = Author.objects.get(id=author_id)
        book.authors.add(author)
    return redirect(f"/books/{number}")

def authors(request):
    context = {
        "all_the_authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def create_author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']

    Author.objects.create(
        first_name=first_name,
        last_name=last_name,
        notes=notes
    )
    return redirect('/authors')

def show_author(request, number):
    author = Author.objects.get(id=number)
    context = {
        "author": author,
        "all_books": Book.objects.all()
    }
    return render(request, "show_author.html", context)

def add_book(request, number):
    if request.method == "POST":
        author = Author.objects.get(id=number)
        book_id = request.POST.get("book_id")
        book = Book.objects.get(id=book_id)
        author.books.add(book)
    return redirect(f"/authors/{number}")