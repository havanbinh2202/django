from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from .models import Product, Category
from .forms import CartItemForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


def home(request, category_slug=None):
    products = Product.objects.filter(available=True)
    if request.user.is_authenticated:
        categories = Category.objects.all()
        user = request.user
        total_quantity = CartItem.total_quantity(user)
    


    return render(request, 'home.html', locals())

def search(request):
    categories = Category.objects.all()
    user = request.user
    total_quantity = CartItem.total_quantity(user)
    
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains = searched)
    return render(request, 'search.html',{"searched":searched, "keys":keys, 'categories': categories, 'total_quantity': total_quantity})


def category_products(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    categories = Category.objects.all()
    user = request.user
    total_quantity = CartItem.total_quantity(user)
    # Lấy dữ liệu tên sản phẩm cần lọc
    name_to_filter = request.GET.get('name', '')  # Sử dụng query parameter 'name' từ URL
    
    # Truy vấn lọc sản phẩm dựa trên tên và danh mục
    products = Product.objects.filter(category=category, available=True, name__icontains=name_to_filter)
    
    return render(request, 'category_products.html', {'category': category, 'products': products,'category_slug': category_slug, 'categories': categories, 'total_quantity': total_quantity})
    
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        # Sau khi thêm sản phẩm vào giỏ hàng, bạn có thể chuyển người dùng đến trang giỏ hàng hoặc trang sản phẩm.
        return redirect('cart')
    else:
        # Nếu người dùng chưa đăng nhập, bạn có thể thực hiện xử lý tùy ý ở đây, ví dụ: chuyển họ đến trang đăng nhập hoặc đăng ký.
        return redirect('dang_nhap')
    
def view_cart(request,category_slug=None):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.get_total() for item in cart_items)
    total_quantity = CartItem.total_quantity(user)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            cart_item = CartItem.objects.get(user=user, product_id=product_id)
            cart_item.quantity = quantity
            cart_item.save()
            return redirect('cart')
    else:
        form = CartItemForm()
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'form': form,
        'total_quantity': total_quantity,
        'category_slug': category_slug,
        'categories': categories,
    }
    
    return render(request, 'cart.html', context)


# chi tiết sp
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)  # Lấy sản phẩm theo ID hoặc slug của sản phẩm
    categories = Category.objects.all()
    # user = request.user
    # total_quantity = CartItem.total_quantity(user)
    context = {
        'product': product,
        'categories': categories,
        # 'total_quantity': total_quantity# Truyền sản phẩm vào template
    }

    return render(request, 'product_detail.html', context)

@csrf_exempt
def update_cart(request):
    data = json.loads(request.body)
    action = data['action']
    item_id = data['item_id']
    cart_item = CartItem.objects.get(pk=item_id, user=request.user)

    if action == 'add':
        cart_item.quantity += 1
    elif action == 'remove':
        cart_item.quantity -= 1
    cart_item.save()
    if cart_item.quantity <= 0:
        cart_item.delete()

    return JsonResponse('added',safe=False)
def remove_from_cart(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        cart_item = CartItem.objects.filter(user=request.user, product=product).first()

        if cart_item:
            cart_item.delete()

    return redirect('cart')

def checkout(request,category_slug=None):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.get_total() for item in cart_items)
    total_quantity = CartItem.total_quantity(user)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            cart_item = CartItem.objects.get(user=user, product_id=product_id)
            cart_item.quantity = quantity
            cart_item.save()
            return redirect('cart')
    else:
        form = CartItemForm()
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'form': form,
        'total_quantity': total_quantity,
        'category_slug': category_slug,
        'categories': categories,
    }
    
    return render(request, 'checkout.html', context)

#-- view: tai_khoan --
@method_decorator(login_required, name='dispatch')
class Tai_Khoan_GCBV(UpdateView):
  model = User
  fields = ('first_name', 'last_name', 'email', )
  template_name = 'my_account.html'
  success_url = reverse_lazy('my_account')

  def get_object(self):
    return self.request.user




