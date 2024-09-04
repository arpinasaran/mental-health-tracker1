from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306259780',
        'name': 'M. Arvin Wijayanto',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
