from django.db.models.expressions import result
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from djangoMigrationProject.models import Product

class HelloWorld(View):
    def get(self, request):
        return render (request, "hello_world.html", {"name": "Ayesha"})


class MyForm(View):
    def get(self, request):
        return render (request, "form_page.html", {})
    def post(self, request):
        print(request.POST)
        x = int(request.POST["x"])
        y = int(request.POST["y"])
        if x>y:
            result = x
        else:
            result = y
        result = 100
        return render(request, "form_page.html", {"max": result})
class ProductView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class Counter(View):
  def get(self, request):
    count = request.session.get("count",0)
    return render(request, 'counter_page.html', {"count":count})
  def post(self, request):
    count = request.session.get("count",0)
    count = count + 1
    request.session["count"]=count
    request.session.set_expiry(300)
    return render(request, 'counter_page.html', {"count":count})
