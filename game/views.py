from django.shortcuts import render, redirect


def login_view(request):

    if request.method == "POST":

        usuario = request.POST.get("usuario")
        password = request.POST.get("password")

        if usuario == "admin" and password == "1234":

            request.session["logueado"] = True
            request.session["usuario"] = usuario

            return redirect("/app/inicio2/")

    return redirect("/app/")


def inicio(request):
    return render(
        request,
        'game/inicio.html'
    )


def inicio2(request):

    if not request.session.get("logueado"):
        return redirect("/app/")

    return render(
        request,
        'game/inicio2.html',
        {
            'usuario': request.session.get('usuario')
        }
    )


def novedades(request):

    if not request.session.get("logueado"):
        return redirect("/app/")

    return render(
        request,
        'game/novedades.html',
        {
            'usuario': request.session.get('usuario')
        }
    )


def personajes(request):

    if not request.session.get("logueado"):
        return redirect("/app/")

    return render(
        request,
        'game/personajes.html',
        {
            'usuario': request.session.get('usuario')
        }
    )


def como_jugar(request):

    if not request.session.get("logueado"):
        return redirect("/app/")

    return render(
        request,
        'game/como_jugar.html',
        {
            'usuario': request.session.get('usuario')
        }
    )


def contacto(request):

    if not request.session.get("logueado"):
        return redirect("/app/")

    return render(
        request,
        'game/contacto.html',
        {
            'usuario': request.session.get('usuario')
        }
    )


def logout_view(request):

    request.session.flush()

    return redirect("/app/")