from django.shortcuts import render
from .models import Curso
from AppCoder.forms import CursoFormulario, BuscaCursoForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Curso, Estudiante, Profesor, Entregable
from django.urls import reverse_lazy
from users.models import Imagen

from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):

    return render(request, "AppCoder/index.html")

@login_required
def about(request):
    return render(request, "AppCoder/about.html")



class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "AppCoder/curso_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CursoDetailView(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "AppCoder/curso_detail.html"


class CursoCreateView(LoginRequiredMixin, CreateView):

    model = Curso
    template_name = "AppCoder/curso_create.html"
    fields = ["nombre", "camada"]

    success_url = reverse_lazy("CursoList")


class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    success_url = reverse_lazy("CursoList")
    fields = ["nombre", "camada"]
    template_name = "AppCoder/curso_update.html"


class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = reverse_lazy("CursoList")
    template_name = 'AppCoder/curso_confirm_delete.html'


class EstudianteListView(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = "AppCoder/estudiante_list.html"


class EstudianteDetailView(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name = "AppCoder/estudiante_detail.html"


class EstudianteCreateView(LoginRequiredMixin, CreateView):

    model = Estudiante
    template_name = "AppCoder/estudiante_create.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("EstudianteList")


class EstudianteUpdateView(LoginRequiredMixin, UpdateView):
    model = Estudiante
    success_url = reverse_lazy("EstudianteList")
    fields = ["nombre", "apellido", "email"]
    template_name = "AppCoder/estudiante_update.html"


class EstudianteDeleteView(LoginRequiredMixin, DeleteView):
    model = Estudiante
    success_url = reverse_lazy("EstudianteList")
    template_name = 'AppCoder/estudiante_confirm_delete.html'


class ProfesorListView(LoginRequiredMixin, ListView):
    model = Profesor
    template_name = "AppCoder/profesor_list.html"


class ProfesorDetailView(LoginRequiredMixin, DetailView):
    model = Profesor
    template_name = "AppCoder/profesor_detail.html"


class ProfesorCreateView(LoginRequiredMixin, CreateView):
    model = Profesor
    template_name = "AppCoder/profesor_create.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("ProfesorList")


class ProfesorUpdateView(LoginRequiredMixin, UpdateView):
    model = Profesor
    success_url = reverse_lazy("ProfesorList")
    fields = ["nombre", "apellido", "email"]
    template_name = "AppCoder/profesor_update.html"


class ProfesorDeleteView(LoginRequiredMixin, DeleteView):
    model = Profesor
    success_url = reverse_lazy("ProfesorList")
    template_name = 'AppCoder/profesor_confirm_delete.html'


class EntregableListView(LoginRequiredMixin, ListView):
    model = Entregable
    template_name = "AppCoder/entregable_list.html"


class EntregableDetailView(LoginRequiredMixin, DetailView):
    model = Entregable
    template_name = "AppCoder/entregable_detail.html"


class EntregableCreateView(LoginRequiredMixin, CreateView):
    model = Entregable
    template_name = "AppCoder/entregable_create.html"
    fields = ["nombre", "fecha_de_entrega", "entregado"]
    success_url = reverse_lazy("EntregableList")


class EntregableUpdateView(LoginRequiredMixin, UpdateView):
    model = Entregable
    success_url = reverse_lazy("EntregableList")
    fields = ["nombre", "fecha_de_entrega", "entregado"]
    template_name = "AppCoder/entregable_update.html"


class EntregableDeleteView(LoginRequiredMixin, DeleteView):
    model = Entregable
    success_url = reverse_lazy("EntregableList")
    template_name = 'AppCoder/entregable_confirm_delete.html'




