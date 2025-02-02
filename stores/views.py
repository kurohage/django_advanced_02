from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreModelForm

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)

def store_create(request):
    form = StoreModelForm()
    if request.method == "POST":
        form = StoreModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        print (form.errors)
    context = {
    "form": form,
    }
    return render(request, 'store_create.html', context)

def store_detail(request, slug):
    store = Store.objects.get(slug=slug)

    context = {
        "store": store,
    }
    return render(request, 'store_detail.html', context)