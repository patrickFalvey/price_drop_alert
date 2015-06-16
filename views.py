from .forms import price_drop_alert_form
from .models import Price_Drop_Alert


def price_drop_alert_entry(request):
    form = price_drop_alert_form(request.POST or None)
    context = {"form": form}
    user = UserProfile.objects.get(user=request.user)
    product = Product.objects.get(id=request.GET.get('product_id'))
    template = "saas_app/search-result.html"
    if form.is_valid():
        target = form.cleaned_data['Desired_Price']
        alert = Price_Drop_Alert(email=user.email, item=product.id, price=target)
        alert.save()
    return render(request, template, context)



