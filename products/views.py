from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


def home(request):
    products = Product.objects
    return render(request, 'products/home.html', {'products': products})


@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        url = request.POST['url']
        pub_date = timezone.datetime.now()
        votes_total = 1
        icon = request.FILES['icon']
        image = request.FILES['image']
        body = request.POST['body']
        hunter = request.user

        if title and url and icon and image and body:
            product = Product()
            product.title = title

            if url.startswith("http://") or url.startswith("htttps://"):
                product.url = url
            else:
                product.url = "http://" + url

            product.pub_date = pub_date
            product.icon = icon
            product.image = image
            product.body = body
            product.votes_total = votes_total
            product.hunter = hunter
            product.save()
            return redirect('allproducts')
        else:
            return render(request, 'products/create.html', {'error': 'All fields are required'})
    else:
        return render(request, 'products/create.html')


@login_required
def allproducts(request):
    products = Product.objects
    return render(request, 'products/allproducts.html', {'products': products})


@login_required
def details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/details.html', {'product': product})


@login_required
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        votes = product.votes_total
        votes += 1
        product.votes_total = votes
        product.save()
        # return redirect('product_details', product_id)
        return redirect('/products/' + str(product_id))
