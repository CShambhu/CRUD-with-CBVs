from django.urls import path
from . views import MyView, BookShowDetails, BookCreateView, BookListView, BookUpdateView, BookDeleteView
urlpatterns = [
    # path('', MyView.as_view(), name='home'),
    path('book/<int:pk>/', BookShowDetails.as_view(), name='book_detail'),
    path('add', BookCreateView.as_view(),name='addbook'),
    path('', BookListView.as_view(), name='booklist'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]