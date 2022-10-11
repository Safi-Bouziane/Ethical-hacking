from django.shortcuts import render
from django.http import HttpResponse
from .models import Film, Review
from django.shortcuts import get_object_or_404, redirect
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def detail(request, film_id):
    film = get_object_or_404(Film,pk=film_id)
    reviews = Review.objects.filter(film = film)
    return render(request, 'detail.html',{'film':film, 'reviews': reviews})


def home(request):
    zoekTerm = request.GET.get('zoekFilm')
    if zoekTerm:
        films = Film.objects.filter(titel__icontains=zoekTerm)
    else:
        films = Film.objects.all()
    return render(request, 'home.html', {'zoekTerm':zoekTerm, 'films': films})


def over(request):
    return HttpResponse('<h1>Welkom op de over-ons pagina</h1>')


def schrijfin(request):
    email = request.GET.get('email')
    return render(request, 'schrijfin.html', {'email':email})


@login_required
def maakreview(request, film_id):
    film = get_object_or_404(Film,pk=film_id)
    if request.method == 'GET':
        return render(request, 'maakreview.html', {'form':ReviewForm(), 'film': film})
    else:
        try:
            form = ReviewForm(request.POST)
            nieuwReview = form.save(commit=False)
            nieuwReview.user = request.user
            nieuwReview.film = film
            nieuwReview.save()
            return redirect('detail', nieuwReview.film.id)
        except ValueError:
            return render(request, 'maakreview.html', {'form':ReviewForm(),'error':'Niet correcte data ingevoerd'})


@login_required
def wijzigreview(request, review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'wijzigreview.html',{'review': review,'form':form})
    else:
        try:
            form = ReviewForm(request.POST,instance=review)
            form.save()
            return redirect('detail', review.film.id)
        except ValueError:
            return render(request,'wijzigreview.html',{'review': review,'form':form,'error':'Foute data aanwezig in het formulier'})

@login_required
def verwijderreview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.film.id)
