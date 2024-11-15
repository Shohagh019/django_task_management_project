from django.shortcuts import render
from category_app.models import Category
def home(request):
    data = Category.objects.all()
    return render(request, 'base.html', {'data': data})