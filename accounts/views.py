from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import Profile  # لو عندك model Profile
from cart.models import Order
from products.models import Product

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # أضف profile إضافي لو عايز (اختياري)
            Profile.objects.get_or_create(user=user)  # ينشئ profile فارغ
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user)
    query = request.GET.get('q')
    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query)
    context = {
        'orders': orders,
        'products': products,
    }
    # لو اليوزر admin، أضف خيارات إدارة
    if request.user.is_superuser:
        context['is_admin'] = True
    return render(request, 'dashboard.html', context)

# للدخول، استخدم built-in، بس لو عايز custom:
class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm