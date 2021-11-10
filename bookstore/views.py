from django.shortcuts import render, HttpResponseRedirect
from .models import Book


# Create your views here.


def test_html(request):
    return render(request, 'test_html.html')


def test_static(request):
    return render(request, 'test_static.html')


def book_all(request):
    Book_all = Book.objects.filter(is_active=True)
    return render(request, 'book_all.html', locals())


def delete_book(request):
    bid = request.GET.get('bid')
    if not bid:
        return HttpResponse('==bid is error==')
    try:
        book = Book.objects.get(id=bid, is_active=True)
    except Exception as e:
        print('== no book! ==', e.args)
        return HttpResponse('==book is error==')

    book.is_active = False
    book.save()

    return HttpResponseRedirect('book_all')


def update_book(request, bid):
    books = Book.objects.get(id=bid, is_active=True)

    if request.method == 'GET':
        return render(request, 'update_book.html', locals())

    elif request.method == "POST":
        price = request.POST.get('price')
        market_price = request.POST.get('market_price')

        books.price = price
        books.market_price = market_price

        books.save()
        return HttpResponseRedirect('/bookstore/book_all')
