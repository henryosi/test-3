from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from .models import Wishitem


# Create your views here.


def home(request):
  return render(request, 'wishitems/index.html')

def wishitems_index(request):
    wishitems = Wishitem.objects.filter(user=request.user)
    return render (request, 'wishitems/index.html', { 'wishitems': wishitems })

class WishitemList(ListView):
  model = Wishitem

class WishitemCreate (CreateView):
    model = Wishitem
    fields = ['description']

    def form_valid(self, form):
      # Assign the logged in user
      form.instance.user = self.request.user
      # Let the CreateView do its job as usual
      return super().form_valid(form)

class WishitemDelete (DeleteView):
    model = Wishitem
    success_url = '/index/'