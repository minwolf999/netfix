from django.shortcuts import render

from users.models import User, Company, Customer
from services.models import Service, Request

from datetime import datetime
import pytz


def home(request):
    return render(request, 'users/home.html', {'user': request.user})


def customer_profile(request, name):
    user = User.objects.get(username=name)

    if (user.is_customer) :
        date_naissance = datetime.combine(user.customer.birth, datetime.min.time())
        date_aujourdhui = datetime.now(pytz.utc)

        if date_naissance.tzinfo is None:
            date_naissance = pytz.utc.localize(date_naissance)

        difference_dates = date_aujourdhui - date_naissance
        user.user_age = difference_dates.days // 365

    services = Request.objects.filter(customer = user.id)

    if (request.method == "POST"):
        customer = Customer.objects.get(user_id=user.id)
        req_to_del = Request.objects.filter(service_id = request.POST['id'], customer=customer)

        if req_to_del.exists():
            req_to_del.delete()
    
    try:
        return render(request, 'users/profile.html', {'user':user, 'services':services})
    except:
        return render(request, 'users/profile.html', {'user':user})


def company_profile(request, name):
    # fetches the company user and all of the services available by it
    user = User.objects.get(username=name)
    services = Service.objects.filter(company=Company.objects.get(user=user)).order_by("-date")

    if (request.method == "POST"):
        serv_to_del = Service.objects.filter(id = request.POST['id'])

        if serv_to_del.exists():
            serv_to_del.delete()

    try:
        if (request.user.username == user.username):
            return render(request, 'users/profile.html', {'user': user, 'services': services, 'Visitor': True})
        else:
            return render(request, 'users/profile.html', {'user': user, 'services': services, 'Visitor': False})
    except:
        return render(request, 'users/profile.html')
