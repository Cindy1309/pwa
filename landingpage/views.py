from django.shortcuts import render
from django.http import JsonResponse
from .models import Subscriber, Visitor


def home(request):

    # Registrar visitante una sola vez por sesión
    if not request.session.get("visit_registered"):

        ip = request.META.get("REMOTE_ADDR")

        user_agent = request.META.get(
            "HTTP_USER_AGENT",
            ""
        )

        Visitor.objects.create(
            ip=ip,
            user_agent=user_agent
        )

        request.session["visit_registered"] = True

    # Registro de acceso anticipado
    if request.method == "POST":

        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")

        if nombre and correo:

            try:

                Subscriber.objects.create(
                    nombre=nombre,
                    correo=correo
                )

                return JsonResponse({
                    "success": True,
                    "message": "✅ Pronto recibirás más noticias, explorador."
                })

            except Exception:

                return JsonResponse({
                    "success": False,
                    "message": "⚠ Este correo ya está registrado."
                })

    return render(
        request,
        "landingpage/home.html"
    )