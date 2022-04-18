from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404

from newsletter.models import Category, Newsletter
# Create your views here.

def NewsListView(request, parent_or_child=None, pk=None):
    categories = Category.objects.filter(parent=None)
    
    if parent_or_child is None:
        newsletters = Newsletter.objects.all()
        paginator = Paginator(newsletters, 6)
            
    elif parent_or_child == 'child':
        sub_cat= Category.objects.get(pk=pk)
        newsletters= sub_cat.newsletter_set.all()
        paginator = Paginator(newsletters, 6)
            
    elif parent_or_child == 'parent':
        newsletters= []
        sub_cats= Category.objects.get(pk=pk).children.all()

        for sub_cat in sub_cats:
            prds = sub_cat.newsletter_set.all()
            newsletters += prds
        paginator = Paginator(newsletters, 6)
            
    else:
        newsletters = []        
          
    page = request.GET.get('page')
 
    try:
        newsletters = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        newsletters = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        newsletters= paginator.page(paginator.num_pages)

    return render(
        request,
        'news_list.html',
        {'categories': categories, 'newsletters': newsletters, }
    )

class NewsDetailView(generic.DetailView):
    model: Newsletter
    template_name = 'news_detail.html'

    def get_object(self):
        return get_object_or_404(Newsletter, id = self.kwargs["id"])

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['newsletter'] = self.get_object()
        return context
    