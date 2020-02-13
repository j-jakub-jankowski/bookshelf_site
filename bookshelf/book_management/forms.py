from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'authors', 'published_date', 'isbn', 'page_count', 'small_thumbnail', 'language']


class GoogleBookApiForm(forms.Form):
    q = forms.CharField(label='Search', max_length=50)
    intitle = forms.CharField(label='Title', max_length=50, required=False)
    inauthor = forms.CharField(label='Author', max_length=50, required=False)
    inpublisher = forms.CharField(label='Publisher', max_length=50, required=False)
    subject = forms.CharField(label='Subject', max_length=50, required=False)
    isbn = forms.CharField(label='ISBN', max_length=13, required=False)
    lccn = forms.CharField(label='LCCN', max_length=20, required=False)
    oclc = forms.CharField(label='OCLC', max_length=20, required=False)
