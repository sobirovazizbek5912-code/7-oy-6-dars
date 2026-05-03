
from django.shortcuts import get_object_or_404, redirect, render
from .models import Elon, Category, Comment
from .forms import ElonForm
from django.contrib import messages
from django.http import HttpRequest,HttpResponse
from django.core.paginator import Paginator


def home(request:HttpRequest):
    categories = Category.objects.all()

    category_id = request.GET.get('category')

    if category_id:
        elons = Elon.objects.filter(category_id=category_id)
    else:
        elons = Elon.objects.all()

    paginator=Paginator(elons,3)
    page = paginator.page(request.GET.get('page',default=1))
    context = {
            'page': page,
            'categories': categories
        }


    return render(request, 'home.html',context)



def elon_detail(request, id):
    elon = get_object_or_404(Elon, id=id)
    comments = elon.comments.all()

    return render(request, 'detail.html', {
        'elon': elon,
        'comments': comments
    })


def create_elon(request):
    if request.method == 'POST':
        form = ElonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Elon muafiqiyatli qoshildi ')
            return redirect('home')
    else:
        form = ElonForm()

    return render(request, 'create.html', {'form': form})



def update_elon(request, id):
    elon = get_object_or_404(Elon, id=id)

    if request.method == 'POST':
        form = ElonForm(request.POST, request.FILES, instance=elon)
        if form.is_valid():
            form.save()
            return redirect('detail', id=elon.id)
    else:
        form = ElonForm(instance=elon)

    return render(request, 'update.html', {'form': form})

def delete_elon(request, id: int):
    if request.user.is_staff:
        elon = get_object_or_404(Elon, id=id)

        if request.method == 'POST':
            elon.delete()
            messages.success(request, "Elon muvaffaqiyatli o‘chirildi")
            return redirect('home')

        messages.warning(request, "Shu elonni aniq o‘chirmoqchimisiz?")
        return render(request, 'delete.html', {'elon': elon})

    else:
        messages.error(request, "Sizda ruxsat yo‘q")
        return redirect('home')




def add_comment(request, elon_id):
    elon = get_object_or_404(Elon, id=elon_id)

    if request.method == 'POST':
        Comment.objects.create(
            elon=elon,
            user=request.user if request.user.is_authenticated else None,
            name=request.POST.get('name'),
            text=request.POST.get('text')
        )

    return redirect('detail', id=elon.id)



def update_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if request.method == 'POST':
        comment.name = request.POST.get('name')
        comment.text = request.POST.get('text')
        comment.save()
        return redirect('detail', id=comment.elon.id)

    return render(request, 'update_comment.html', {'comment': comment})


def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if request.user == comment.user or request.user.is_superuser:
        elon_id = comment.elon.id
        comment.delete()
        return redirect('detail', id=elon_id)

    return redirect('detail', id=comment.elon.id)

def like_elon(request, elon_id):
    elon = get_object_or_404(Elon, id=elon_id)

    if request.user.is_authenticated:
        if request.user in elon.likes.all():
            elon.likes.remove(request.user)
        else:
            elon.likes.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', 'home'))



def favorites(request):
    if request.user.is_authenticated:
        elons = request.user.liked_elons.all()
    else:
        elons = []

    return render(request, 'favorites.html', {'elons': elons})