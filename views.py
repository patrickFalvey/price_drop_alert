from braces.views import LoginRequiredMixin
from .forms import price_drop_alert_form
from .models import Price_Drop_Alert


class price_drop_alert_entry(LoginRequiredMixin, FormView):
    form_class = price_drop_alert_form
    success_url = "/"
    template = "saas_app/search-result.html"
    def form_valid(self, form):
        user = UserProfile.objects.get(user=request.user)
        product = Product.objects.get(id=request.GET.get('product_id'))
        target = form.cleaned_data['Desired_Price']
        alert = Price_Drop_Alert(email=user.email, item=product.id, price=target)
        alert.save()
    return super(price_drop_alert_entry, self).form_valid(form)



