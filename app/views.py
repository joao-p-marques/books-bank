from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import *

from app.forms import *

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def listbooks(request):
    books_list = Book.objects.all()
    return render(request, 'list_books.html', {"books": books_list})

def book(request, book_id):
    book = Book.objects.get(id = book_id)
    return render(request, 'book.html', {"book" : book})

def author(request, author_id):
    author = Author.objects.get(id = author_id)
    author_books = list(Book.objects.filter(authors=author))
    return render(request, 'author.html', {"author" : author, "books" : author_books})

def publisher(request, publisher_id):
    publisher = Publisher.objects.get(id = publisher_id)
    publisher_books = list(Book.objects.filter(publisher = publisher))
    return render(request, 'publisher.html', {"publisher" : publisher, "books" : publisher_books})

def booksearch(request):
    title_query = None
    author_query = None
    publisher_query = None
    if 'title_query' in request.POST:
        title_query = request.POST['title_query']
    if 'author_query' in request.POST:
        author_query = request.POST['author_query']
    if 'publisher_query' in request.POST:
        publisher_query = request.POST['publisher_query']
    if title_query or author_query or publisher_query:
        if title_query and author_query and publisher_query:
            books = Book.objects.filter(title__icontains=title_query, authors__name__icontains=author_query, publisher__name__icontains=publisher_query)
            return render(request, "list_books.html", { 'books' : books, 'title_query' : title_query, 'author_query' : author_query, 'publisher_query' : publisher_query })
        if title_query and author_query:
            books = Book.objects.filter(title__icontains=title_query, authors__name__icontains=author_query)
            return render(request, "list_books.html", { 'books' : books, 'title_query' : title_query, 'author_query' : author_query })
        elif title_query and publisher_query:
            books = Book.objects.filter(title__icontains=title_query, publisher__name__icontains=publisher_query)
            return render(request, "list_books.html", { 'books' : books, 'title_query' : title_query, 'publisher_query' : publisher_query })
        elif author_query and publisher_query:
            books = Book.objects.filter(authors__name__icontains=author_query, publisher__name__icontains=publisher_query)
            return render(request, "list_books.html", { 'books' : books, 'author_query' : author_query, 'publisher_query' : publisher_query })
        elif title_query:
            books = Book.objects.filter(title__icontains=title_query)
            return render(request, "list_books.html", { 'books' : books, 'title_query' : title_query })
        elif publisher_query:
            books = Book.objects.filter(publisher__name__icontains=publisher_query)
            return render(request, "list_books.html", { 'books' : books, 'publisher_query' : publisher_query })
        elif author_query:
            books = Book.objects.filter(authors__name__icontains=author_query)
            return render(request, "list_books.html", { 'books' : books, 'author_query' : author_query })
        else:
            return render(request, "booksearch.html", { 'error' : True })
    else:
        return render(request, 'booksearch.html', { 'error' : False })

def authorsearch(request):
    if 'query' in request.POST:
        query = request.POST['query']
        if query:
            authors = Author.objects.filter(name__icontains=query)
            return render(request, "list_authors.html", { 'authors' : authors, 'query' : query })
        else:
            return render(request, "authorsearch.html", { 'error' : True })
    else:
        return render(request, 'authorsearch.html', { 'error' : False })

def insertauthor(request):
    name = None
    email = None
    if 'name' in request.POST:
        name = request.POST['name']
    if 'email' in request.POST:
        email = request.POST['email']
    if name and email:
        author = Author(name=name, email=email)
        author.save()
        return HttpResponse("<h1>Author Created</h1>") # FIX
    else:
        return render(request, 'insert_author.html')

def insertpublisher(request):
    name = None
    city = None
    country = None
    website = None
    if 'name' in request.POST:
        name = request.POST['name']
    if 'city' in request.POST:
        city = request.POST['city']
    if 'country' in request.POST:
        country = request.POST['country']
    if 'website' in request.POST:
        website = request.POST['website']
    if name and city and country and website:
        publisher = Publisher(name=name, city=city, country=country, website=website)
        publisher.save()
        return HttpResponse("<h1>Publisher Created</h1>") # FIX
    else:
        return render(request, 'insert_publisher.html')

def insertbook(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            book = Book(title=data['title'], date=data['date'], author=data['authors'], publisher=data['publisher'])
            book.save()
            books = Book.objects.all()
            return render(request, 'list_books.html', {'books' : books })
    else:
        form = CreateBookForm()
    return render(request, 'insert_book.html', {'form' : form})

# def insertbook(request):
#     title = None
#     date = None
#     authors = None
#     publisher = None
#     if 'title' in request.POST:
#         title = request.POST['title']
#     if 'date' in request.POST:
#         date = request.POST['date']
#     if 'authors' in request.POST:
#         authors = request.POST['authors']
#         for author in request.POST['authors']
#     if 'website' in request.POST:
#         website = request.POST['website']
#     if name and city and country and website:
#         publisher = Publisher(name=name, city=city, country=country, website=website)
#         publisher.save()
#         return HttpResponse("<h1>Publisher Created</h1>") # FIX
#     else:
#         return render(request, 'insert_publisher.html')
