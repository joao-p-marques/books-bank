from app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('listbooks/', views.listbooks, name="listbooks"),
    path('book/<int:book_id>', views.book, name="book"),
    path('author/<int:author_id>', views.author, name="author"),
    path('publisher/<int:publisher_id>', views.publisher, name="publisher"),
    path('booksearch/', views.booksearch, name="booksearch"),
    path('authorsearch/', views.authorsearch, name="authorsearch"),
    path('insertauthor/', views.insertauthor, name="insertauthor"),
    path('insertpublisher/', views.insertpublisher, name="insertpublisher"),
    path('insertbook/', views.insertbook, name="insertbook"),
]
