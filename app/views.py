from django.shortcuts import render, redirect


# Create your views here.
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('app:login-user')
    context = {}
    return render(request, 'app/chatPage.html', context)
