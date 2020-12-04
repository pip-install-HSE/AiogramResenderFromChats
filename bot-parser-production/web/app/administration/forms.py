from django.forms import Form, Textarea, CharField


class StopwordsForm(Form):

    stopwords = CharField(widget=Textarea(attrs={
        'class': 'form-control mt-2',
        'placeholder': 'Стоп, слова, ...',
    }), label=False, required=False)