from django.shortcuts import render
from .forms import BookForm

from .models import Book
def index(request):
    return render(request, 'members/home.html')


def home(request):
    books = Book.objects.all()
    return render(request, 'members/home.html', {'books': books})

def login(request):
    return render(request, 'members/login.html')
def signup(request):
    return render(request, 'members/signup.html')

def sin(request):
    return render(request, 'members/sin.html')
def shoping_basket(request):
    return render(request, 'members/shoping_basket.html')
def edit(request):
    return render(request, 'edit.html')
def addnew(request):
    return render(request, 'addnew.html')    
def addnew(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after successfully adding the book
    else:
        form = BookForm()
    return render(request, 'members/addnew.html', {'form': form})