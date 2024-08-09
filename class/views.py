from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from . models import Book
from . forms import BookForm
# Create your views here.

class MyView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)
    

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse_lazy('addbook')


    #Get the whole data of book model
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.all()  # Add the list of books to the context
        return context

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'boo'


class BookShowDetails(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'boo'
    

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'edit_book.html'  # Template used for rendering the form
    context_object_name = 'book'  # Name of the context variable to use in the template

    def get_success_url(self):
        return reverse_lazy('booklist')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'confirm_delete.html'  # Template used for rendering the confirmation page
    context_object_name = 'book'  # Name of the context variable to use in the template

    def get_success_url(self):
        return reverse_lazy('booklist') 