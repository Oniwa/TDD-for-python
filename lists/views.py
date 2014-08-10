from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')

    #TODO: Display multiple items in the table
    #TODO: Support more than one list
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})


def view_list(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
