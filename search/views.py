<<<<<<< HEAD
from django.shortcuts import render,redirect,reverse
from search.models import Game
from search.forms import GameForm
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST



def show_search(request):
    game_entries = Game.objects.all()
    context = {
        'name': 'Dummy',
        'last_login' : "Dummy",
        'game_entries' :game_entries
    }

    return render(request, "search.html", context)


def create_game_entry(request):
    form = GameForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('search:show_search')  # Adjust the redirect based on your URL configuration

    context = {'form': form}
    return render(request, "create_game_entry.html", context)

def show_json(request):
    data = Game.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def edit_game(request, id):
    # Get the game entry based on the id
    game = Game.objects.get(pk = id)

    # Set the game entry as the instance for the form
    form = GameForm(request.POST or None, instance=game)

    if form.is_valid() and request.method == "POST":
        # Save the form and redirect to the main page
        form.save()
        return HttpResponseRedirect(reverse('search:show_search'))

    context = {'form': form}
    return render(request, "edit_game.html", context)

def delete_game(request, id):
    # Get game berdasarkan id
    game = Game.objects.get(pk = id)
    # Hapus game
    game.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('search:show_search'))

@csrf_exempt
@require_POST
def add_game_entry_ajax(request):
    # Extract data from the POST request
    name = request.POST.get("name")
    year = request.POST.get("year")
    description = request.POST.get("description")
    developer = request.POST.get("developer")
    genre = request.POST.get("genre")
    ratings = request.POST.get("ratings")
    harga = request.POST.get("harga")
    toko1 = request.POST.get("toko1")
    alamat1 = request.POST.get("alamat1")
    toko2 = request.POST.get("toko2", "")  # Optional
    alamat2 = request.POST.get("alamat2", "")  # Optional
    toko3 = request.POST.get("toko3", "")  # Optional
    alamat3 = request.POST.get("alamat3", "")  # Optional

    # Create and save the new Game entry
    new_game = Game(
        name=name,
        year=int(year) if year else None,
        description=description,
        developer=developer,
        genre=genre,
        ratings=float(ratings) if ratings else 0.0,
        harga=int(harga) if harga else 0,
        toko1=toko1,
        alamat1=alamat1,
        toko2=toko2,
        alamat2=alamat2,
        toko3=toko3,
        alamat3=alamat3,
    )
    new_game.save()

=======
from django.shortcuts import render,redirect,reverse, get_object_or_404
from search.models import Game
from search.forms import GameForm
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST



def show_search(request):
    context = {
        'role':'admin'
    }
    return render(request, "search.html", context)


def show_json(request):
    data = Game.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    # Dapatkan objek Game berdasarkan id atau kembalikan 404 jika tidak ditemukan
    game = get_object_or_404(Game, pk=id)
    # Serialisasi objek Game menjadi JSON
    return HttpResponse(serializers.serialize("json", [game]), content_type="application/json")



@csrf_exempt
@require_POST
def edit_game_ajax(request, id):
    # Mendapatkan game berdasarkan id atau mengembalikan 404 jika tidak ditemukan
    game = Game.objects.get(pk=id)

    # Menggunakan GameForm dengan instance game untuk memvalidasi data POST
    form = GameForm(request.POST or None, instance=game)
    
    if form.is_valid():
        form.save()  # Menyimpan perubahan
        # Mengembalikan response sukses sederhana
        return HttpResponse("Game updated successfully!", status=200)
    else:
        # Mengembalikan pesan error jika form tidak valid
        return HttpResponse("Error updating game.", status=400)


def delete_game(request, id):
    # Get game berdasarkan id
    game = Game.objects.get(pk = id)
    # Hapus game
    game.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('search:show_search'))

@csrf_exempt
@require_POST
def add_game_entry_ajax(request):
    # Extract data from the POST request
    name = request.POST.get("name")
    year = request.POST.get("year")
    description = request.POST.get("description")
    developer = request.POST.get("developer")
    genre = request.POST.get("genre")
    ratings = request.POST.get("ratings")
    harga = request.POST.get("harga")
    toko1 = request.POST.get("toko1")
    alamat1 = request.POST.get("alamat1")
    toko2 = request.POST.get("toko2", "")  # Optional
    alamat2 = request.POST.get("alamat2", "")  # Optional
    toko3 = request.POST.get("toko3", "")  # Optional
    alamat3 = request.POST.get("alamat3", "")  # Optional

    # Create and save the new Game entry
    new_game = Game(
        name=name,
        year=int(year) if year else None,
        description=description,
        developer=developer,
        genre=genre,
        ratings=float(ratings) if ratings else 0.0,
        harga=int(harga) if harga else 0,
        toko1=toko1,
        alamat1=alamat1,
        toko2=toko2,
        alamat2=alamat2,
        toko3=toko3,
        alamat3=alamat3,
    )
    new_game.save()

>>>>>>> 320f02c7688d29fe78f1f4130ecbf852bcb527d3
    return HttpResponse(b"CREATED", status=201)