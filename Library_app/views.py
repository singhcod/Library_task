from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from Library_app.forms import SignUpForm
from Library_app.models import BookModel



import email
from django.shortcuts import redirect, render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import User
from django.contrib.auth.hashers import make_password, check_password

#signup view for admin singnup

def sign_up(request):
    fm = SignUpForm()
    if request.method == 'POST':
        fm = SignUpForm(request.POST)

        if fm.is_valid():
            name = request.POST.get('username')
            first_name = request.POST.get('first_name')

            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = make_password(request.POST.get('password'))
            user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            return redirect('login')

        else:
            fm.SignUpForm()
    return render(request, 'Library_app/signup.html', {'form': fm})

#login for admin user which already register
def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                return render(request, 'Library_app/homenavbar.html')
            else:
                return redirect('signup')

        return render(request, 'Library_app/login.html')
    else:
        return redirect('home')
#view for logout exiting user
def log_out(request):
    logout(request)
    return redirect('home')


#view for getting users detials


def user_detail(request):
    users = User.objects.all()
    return render(request,'Library_app/user_detail.html',{"users":users})


#for visit admin pannel
def adminview(request):
    return render(request,'Library_app/admin.html')




# Create your views here.
def homeView(request):
    return render(request,'Library_app/homenavbar.html')



#view for create a book entery

def bookdata_view(request):
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        book_price = request.POST.get('book_price')
        book_pages = request.POST.get('book_pages')
        book_author = request.POST.get('book_author')
        book_publisher = request.POST.get('book_publisher')

        BookModel(
            book_name=book_name,
            book_price=book_price,
            book_pages = book_pages,
            book_author = book_author,
            book_publisher = book_publisher,
        ).save()
        return redirect('dispaly_all')
    else:
        return render(request,'Library_app/book_create.html')



# dispaly all record of books

def display_view(request):

    books = BookModel.objects.all()

    return render(request,'Library_app/only_display_all.html',{'books':books})


#view for show all books data with update button

def showupdate(request):
    books = BookModel.objects.all()
    return render(request,'Library_app/only_update.html',{"books":books})


# for update paricular book record

def update_view(request,pk):
    book = BookModel.objects.get(id= pk)
    return render(request,'Library_app/updatedata.html',{'book':book})

#after update add view

def updateSave_view(request,pk):
    Book = BookModel.objects.get(id=pk)
    Book.book_name = request.POST.get('book_name')
    Book.book_pages = request.POST.get('book_pages')
    Book.book_author = request.POST.get('book_author')
    Book.publisher = request.POST.get("book_publisher")
    Book.save()
    return redirect('dispaly_all')

#show delete option on particular book record
def showdelete(request):
    books = BookModel.objects.all()
    return render(request,'Library_app/only_delete.html',{"books":books})

#Delete a particular book form the list of library book

def delete_view(request,pk):
    book = BookModel.objects.get(id= pk)
    book.delete()
    return redirect('dispaly_all')

#for dispaly student Panel
def studnetpanel(request):
    return render(request,'Library_app/Sstudent.html')

# for student getting all record
def studentView(request):
    books = BookModel.objects.all()
    return render(request,'Library_app/only_display_all.html',{'books':books})


