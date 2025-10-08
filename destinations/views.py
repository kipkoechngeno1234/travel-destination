from django.shortcuts import render, get_object_or_404
from .models import Destination

# Create your views here.
def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, "list.html", {"destinations": destinations})


def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, "detail.html" {"destination": destination})