from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
	# Fix saving items on every post request
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect("/")

	items = Item.objects.all()
	return render(request, 'home.html',	 {'items': items})