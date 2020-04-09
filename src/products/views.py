from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product
from django.urls import reverse

# using forms.ModelForm
def product_create_view(request):
    # create initial data of form in view
    initial_data = {
        'title': 'title',
        'description': 'nothing',
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "product_create.html", context)

# using forms.Form
# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         'form': form
#     }
#     return render(request, "product_create.html", context)

def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # render an object to form in the view
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "product_create.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('products:product_list')
    context = {
        "object": obj
    }
    return render(request, "product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "product_list.html", context)

def product_detail_view(request, id):
    # Handle DoesNotExist method1
    obj = get_object_or_404(Product, id=id)

    # Handle DoesNotExist method2
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404('Product DoesNotExist')

    context = {
        "object": obj
    }
    return render(request, "product_detail.html", context)


