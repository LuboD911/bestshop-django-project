from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from bestshop.products.forms import ProductForm, CommentForm, EditProductForm
from bestshop.products.models import Product

from django.views.generic import ListView

#
# UserModel = get_user_model()



def home(request):
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'all_products': all_products,
        'page_obj': page_obj
    }

    return render(request,'home.html',context)

@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('home')
    else:
        form = ProductForm()

    context = {
        'form':form,
    }

    return render(request,'products/add_product.html',context)

def product_details(request,pk):
    product = Product.objects.get(pk=pk)

    is_owner = product.user == request.user

    context = {
        'product':product,
        'comment_form': CommentForm(
            initial={
                'product_pk': pk,
            }
        ),
        'comments': product.comment_set.all(),
        'is_owner': is_owner,
    }

    return render(request,'products/product_details.html',context)

@login_required
def comment_product(request,pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()
    return redirect('details product', pk)

@login_required
def product_edit(request,pk):
    product = Product.objects.get(pk=pk)

    if request.method =="POST":
        form = EditProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            product.user = request.user
            form.save()
            return redirect('home')

    else:
        form = ProductForm(instance=product)

    context = {
        'form':form,
        'product':product,
    }

    return render(request,'products/edit_product.html',context)

@login_required
def product_delete(request,pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('home')
    else:
        context = {
            'product':product,
        }
        return render(request, 'products/delete_product.html', context)

@login_required()
def buy(request,pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'buy.html', context)



class ContactListView(ListView):
    paginate_by = 2
    model = Product