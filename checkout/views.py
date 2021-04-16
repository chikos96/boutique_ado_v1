from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('product'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IgmbiHEV1si8uzuIDO3TQLBAbaA0R57BEgYDl64QNE2tK697MmaqchhEnWHc93zrGO8KLnownnt4MFwO5kgNPtl00e6SSUf5H',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
