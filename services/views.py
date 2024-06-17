from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from datetime import datetime

from users.models import Company, Customer, User

from .models import Service, Request
from .forms import CreateNewService, RequestServiceForm


def service_list(request):
    services = Service.objects.all().order_by("-date")
    return render(request, 'services/list.html', {'services': services})


def index(request, id):
    service = Service.objects.get(id=id)

    if (request.method == "POST"):
        customer = Customer.objects.get(user_id=request.POST['id'])
        req_to_del = Request.objects.get(service = service, customer = customer)
        req_to_del.delete()

    if request.user.username != "":
        request_services = Request.objects.filter(service=service).order_by('-request_date')

        if request.user.id == service.company.user.id:
            return render(request, 'services/single_service.html', {'service': service, 'request_services': request_services})
    
    return render(request, 'services/single_service.html', {'service': service})




def create(request, name):
    user = User.objects.get(username=name)
    company = Company.objects.get(user=user)
    if (request.method == 'POST'):
        if (company.field != 'All in One'):
            choices = [(company.field, company.field)]
            form = CreateNewService(request.POST, choices=choices)
        else:
            form = CreateNewService(request.POST)

        if (form.is_valid()):
            Service.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                price_hour = form.cleaned_data['price_hour'],
                rating = company.rating,
                field = form.cleaned_data['field'],
                date = datetime.now().strftime('%Y-%d-%m'),
                company_id = user.id,
            )
        
            return redirect('/')
        
    if (company.field != 'All in One'):
        choices = [(company.field, company.field)]
        form = CreateNewService(choices=choices)
    else:
        form = CreateNewService()

    return render(request, 'services/create.html', {'form': form})


def service_field(request, field):
    # search for the service present in the url
    field = field.replace('-', ' ').title()
    services = Service.objects.filter(
        field=field)
    return render(request, 'services/field.html', {'services': services, 'field': field})


def request_service(request, id):
    service = Service.objects.get(id=id)
    if (request.method == 'POST'):
        form = RequestServiceForm(request.POST)
        if (form.is_valid()) :
            customer = Customer.objects.get(user_id=request.user.id)
            if (Request.objects.filter(service_id = id, customer = customer).exists()):
                return redirect('/customer/' + request.user.username)

            Request.objects.create(
                service_id = id,
                customer_id = request.user.id,
                address = form.cleaned_data['address'],
                period = form.cleaned_data['period'],
                request_date = datetime.now().strftime('%Y-%d-%m'),
                price = int(form.cleaned_data['period']) * service.price_hour,
            )

        return redirect('/customer/' + request.user.username)

    form = RequestServiceForm()
    return render(request, 'services/request_service.html', {'form': form})
