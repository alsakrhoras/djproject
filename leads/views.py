from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Lead
from .forms import AddLeadModelForm


def leads(request):
    """present the leads in the database"""
    context = {
        "leads": Lead.objects.all().order_by("first_name")
    }
    return render(request, "leads/leads.html", context)


def leads_detail(request, pk):
    """"present the details for a given lead"""
    context = {
        "the_lead": Lead.objects.get(id=pk)
    }
    return render(request, "leads/leads_details.html", context)


def add_lead(request):
    """Add a new Lead to the database"""
    form = AddLeadModelForm()
    if request.method == "POST":
        form = AddLeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads/all")

        context = {
            "add_lead_form": form,
        }
        return render(request, "leads/addlead.html", context)
        
    context = {
        "add_lead_form": AddLeadModelForm(),
    }
    return render(request, "leads/addlead.html", context)
