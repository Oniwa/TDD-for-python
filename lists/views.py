from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    #TODO: Display multiple items in the table
    #TODO: Support more than one list
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})