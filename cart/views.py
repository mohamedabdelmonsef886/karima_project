from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem, Order
from products.models import Product
import stripe  # لو هتستخدم الدفع، pip install stripe لو مش مثبت

# غير الـ key ده لـ API key الحقيقي من Stripe dashboard
stripe.api_key = 'pk_test_your_stripe_public_key_here'  # أو sk_ للـ secret

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # لو موجود، زد الكمية؛ غير كده أضف جديد
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    if request.method == 'POST':
        # إنشاء طلب في الـ DB
        order = Order.objects.create(user=request.user, total_price=total)
        order.products.set(cart_items)
        # Stripe session للدفع (اختياري)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'egp',
                    'product_data': {'name': 'طلب كريمة'},
                    'unit_amount': int(total * 100),  # بالسنت
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/success/',  # صفحة نجاح
            cancel_url='http://127.0.0.1:8000/cart/',
        )
        return redirect(session.url)
    return render(request, 'checkout.html', {'total': total, 'cart_items': cart_items})