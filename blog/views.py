from django.conf import settings
from django.views.generic import DetailView, ListView

from blog.models import Entry, Category


class EntryDetailView(DetailView):
    model = Entry
    queryset = Entry.objects.filter(published=True)
    template_name = 'blog/entry_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EntryDetailView, self).get_context_data()
        try:
            context['next'] = self.object.get_next_by_posted()
        except Entry.DoesNotExist:
            pass

        try:
            context['previous'] = self.object.get_previous_by_posted()
        except Entry.DoesNotExist:
            pass

        return context


class EntryListView(ListView):
    model = Entry
    paginate_by = 2
    queryset = Entry.objects.filter(published=True).order_by('-posted')
    template_name = 'blog/entry_list.html'

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data()
        word_limit = str(getattr(settings, 'BLOG_WORD_LIMIT', 50))
        context['word_limit'] = word_limit

        return context


class CategoryDetailView(DetailView):
    queryset = Category.objects.all()

