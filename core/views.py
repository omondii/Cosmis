from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import AcademicYear, AcademicTerm, StudentClass, Subject
from .forms import AcademicYearForm, AcademicTermForm, SubjectForm, StudentClassForm, CurrentYearForm

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

class YearListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = AcademicYear
    template_name = "school/yearlist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AcademicYearForm()
        return context

class YearCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = AcademicYear
    form_class = AcademicYearForm
    template_name = "school/mgt_form.html"
    success_url = reverse_lazy("years")
    success_message = "New year successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new year"
        return context

class YearUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AcademicYear
    form_class = AcademicYearForm
    success_url = reverse_lazy("years")
    success_message = "Year successfully updated."
    template_name = "school/mgt_form.html"

    def form_valid(self, form):
        obj = self.object
        if obj.current == False:
            terms = (
                AcademicYear.objects.filter(current=True)
                .exclude(name=obj.name)
                .exists()
            )
            if not terms:
                messages.warning(self.request, "You must set a year to current.")
                return redirect("yearlist")
        return super().form_valid(form)

class YearDeleteView(LoginRequiredMixin, DeleteView):
    model = AcademicYear
    success_url = reverse_lazy("years")
    template_name = "school/core_confirm_delete.html"
    success_message = "The year {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(request, "Cannot delete year as it is set to current")
            return redirect("years")
        messages.success(self.request, self.success_message.format(obj.name))
        return super(YearDeleteView, self).delete(request, *args, **kwargs)

class TermListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = AcademicTerm
    template_name = "school/term_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AcademicTermForm()
        return context

class TermCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = AcademicTerm
    form_class = AcademicTermForm
    template_name = "school/mgt_form.html"
    success_url = reverse_lazy("terms")
    success_message = "New term successfully added"

class TermUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AcademicTerm
    form_class = AcademicTermForm
    success_url = reverse_lazy("terms")
    success_message = "Term successfully updated."
    template_name = "school/mgt_form.html"

    def form_valid(self, form):
        obj = self.object
        if obj.current == False:
            terms = (
                AcademicTerm.objects.filter(current=True)
                .exclude(name=obj.name)
                .exists()
            )
            if not terms:
                messages.warning(self.request, "You must set a term to current.")
                return redirect("term")
        return super().form_valid(form)

class TermDeleteView(LoginRequiredMixin, DeleteView):
    model = AcademicTerm
    success_url = reverse_lazy("terms")
    template_name = "school/core_confirm_delete.html"
    success_message = "The term {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(request, "Cannot delete term as it is set to current")
            return redirect("terms")
        messages.success(self.request, self.success_message.format(obj.name))
        return super(TermDeleteView, self).delete(request, *args, **kwargs)


class ClassListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = StudentClass
    template_name = "school/class_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = StudentClassForm()
        return context

class ClassCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentClass
    form_class = StudentClassForm
    template_name = "school/mgt_form.html"
    success_url = reverse_lazy("classes")
    success_message = "New class successfully added"

class ClassUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = StudentClass
    fields = ["name"]
    success_url = reverse_lazy("classes")
    success_message = "class successfully updated."
    template_name = "school/mgt_form.html"

class ClassDeleteView(LoginRequiredMixin, DeleteView):
    model = StudentClass
    success_url = reverse_lazy("classes")
    template_name = "school/core_confirm_delete.html"
    success_message = "The class {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        print(obj.name)
        messages.success(self.request, self.success_message.format(obj.name))
        return super(ClassDeleteView, self).delete(request, *args, **kwargs)

class SubjectListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Subject
    template_name = "school/subject_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SubjectForm()
        return context

class SubjectCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "school/mgt_form.html"
    success_url = reverse_lazy("subjects")
    success_message = "New subject successfully added"

class SubjectUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Subject
    fields = ["name"]
    success_url = reverse_lazy("subjects")
    success_message = "Subject successfully updated."
    template_name = "school/mgt_form.html"

class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Subject
    success_url = reverse_lazy("subjects")
    template_name = "school/core_confirm_delete.html"
    success_message = "The subject {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message.format(obj.name))
        return super(SubjectDeleteView, self).delete(request, *args, **kwargs)

class CurrentYearAndTermView(LoginRequiredMixin, View):
    """Current Year and Term"""

    form_class = CurrentYearForm
    template_name = "school/current_year.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(
            initial={
                "current_year": AcademicYear.objects.get(current=True),
                "current_term": AcademicTerm.objects.get(current=True),
            }
        )
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_Class(request.POST)
        if form.is_valid():
            year = form.cleaned_data["current_year"]
            term = form.cleaned_data["current_term"]
            AcademicYear.objects.filter(name=year).update(current=True)
            AcademicYear.objects.exclude(name=year).update(current=False)
            AcademicTerm.objects.filter(name=term).update(current=True)

        return render(request, self.template_name, {"form": form})
