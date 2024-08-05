from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, AddCustomerForm, UpdateCustomerForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Customer

# -- Home page
def home(request):
    
    return render(request, 'home/index.html')

# - Register a user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("my-login")

    context = {'form':form}

    return render(request, 'home/register.html', context = context)

# - Login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form2':form}

    return render(request, 'home/my-login.html',context = context)


# - Dashboard
@login_required(login_url = 'my-login')
def dashboard(request):

    my_customers = Customer.objects.all()

    context = {'customers': my_customers}

    return render(request, 'home/dashboard.html', context = context)


# -  Add a customer

@login_required(login_url = 'my-login')
def add_customer(request):

    form = AddCustomerForm()

    if request.method == "POST":

        form = AddCustomerForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("dashboard")

    context = {'form3':form}

    return render(request, 'home/create-record.html', context = context)

# - Update a record

@login_required(login_url = 'my-login')
def update_customer(request, pk):

    record = Customer.objects.get(id=pk)
    # record --> customer's detail

    form = UpdateCustomerForm(instance=record)

    if request.method == 'POST':

        form = UpdateCustomerForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            return redirect("dashboard")

    context = {'form4':form}

    return render(request, 'home/update-record.html', context = context)


# - Read / View a singular customer record

@login_required(login_url = 'my-login')
def single_customer(request, pk):

    all_records = Customer.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'home/view-record.html',context = context)

# - Delete a Customer record

@login_required(login_url = 'my-login')
def delete_customer(request, pk):

    record = Customer.objects.get(id=pk)

    record.delete()

    return redirect("dashboard")


# - User logout

def user_logout(request):

    auth.logout(request)

    return redirect("my-login")