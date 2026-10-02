from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Flan
from .forms import RegistroForm, FlanForm

def registro_usuario(request):
    if request.method == 'POST':          #método debe ser POST para protegernos de las peticiones
        form = RegistroForm(request.POST) #registro del formulario con los datos que le enviamos en el post
        if form.is_valid():
            user = form.save()            #si el formulario es válido, creamos el usuario
            login(request, user)          #nos aprovechamos de logear
            return redirect('index')      #vamos a la vista del index
    else:
        form = RegistroForm()                #este es el caso en que el método no sea post. Crea el formulario para ser llenado (esto ocurre cuando se abre la vista del formulario, el if es cuando se envía el formulario)
    return render(request, 'flanes/registro.html', {'form': form})

#READ sin login
def index



#READ con login