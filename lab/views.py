from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from django.template import Context, loader

from .models import Item, Article, Category


class IndexView(generic.ListView):
    model = Item

    def get_queryset(self):
        queryset = Item.objects.db_manager('finance').order_by('selectRank')
        get_param = dict(self.request.GET)
        con_loantime = Q()
        con_limit = Q()
        con_sokujitu = Q()
        con_teirate = Q()
        con_biz = Q()
        con_part = Q()
        con_shufu = Q()
        con_diff = Q()
        for p_key in get_param.keys():
            if p_key == 'loantime_id':
                loantime_id = self.request.GET.get('loantime_id')
                con_loantime = Q(loantime_id__lte=len(loantime_id))
            else:
                con_loantime = Q()
            if p_key == 'limit_id':
                limit_id = self.request.GET.get('limit_id')
                con_limit = Q(limit_id__gte=len(limit_id))
            else:
                con_limit = Q()
            if p_key == 'sokujitu':
                sokujitu = self.request.GET.get('sokujitu')
                con_sokujitu = Q(sokujitu=sokujitu)
            else:
                con_sokujitu = Q()
            if p_key == 'teirate':
                teirate = self.request.GET.get('teirate')
                con_teirate = Q(teirate=teirate)
            else:
                con_teirate = Q()
            if p_key == 'biz':
                biz = self.request.GET.get('biz')
                con_biz = Q(biz=biz)
            else:
                con_biz = Q()
            if p_key == 'part':
                part = self.request.GET.get('part')
                con_part = Q(part=part)
            else:
                con_part = Q()
            if p_key == 'shufu':
                shufu = self.request.GET.get('shufu')
                con_shufu = Q(shufu=shufu)
            else:
                con_shufu = Q()
            if p_key == 'diff':
                diff = self.request.GET.getlist('diff')
                con_diff = ~Q(name_id__in=diff)
            else:
                con_diff = Q()
        queryset = queryset.filter(
            con_loantime, con_limit, con_sokujitu, con_teirate, con_biz, con_part, con_shufu, con_diff
        )
        return queryset


class CategoryView(generic.ListView):
    model = Article
    paginate_by = 10

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Article.objects.filter(category=category)
        return queryset


class ArticleView(generic.ListView):
    model = Article
    paginate_by = 10

    def get_queryset(self):
        queryset = Article.objects.all()
        # keyword = self.request.GET.get('keyword')
        # if keyword:
        #     queryset = queryset.filter(
        #         Q(title__icontains=keyword) | Q(article__icontains=keyword)
        #     )
        return queryset


class ArticleDetailView(generic.DetailView):
    model = Article


def company(request):
    return render(request, 'lab/company.html')