from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, FormView

from .forms import StopwordsForm


class Stopwords(FormView):
    template_name = 'stopwords.html'

    def get(self, request, *args, **kwargs):
        with open('shared/stopwords.txt', 'r') as f:
            data = f.read()
        initial = {'stopwords': data}
        context = {'form': StopwordsForm(initial=initial)}
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        data = request.POST['stopwords'].strip().lower()
        data = set((map(lambda x: x.strip(), data.split(','))))
        if '' in data:
            data.remove('')
        with open('shared/stopwords.txt', 'w') as f:
            f.write(', '.join(sorted(list(data))))
        return redirect('home')