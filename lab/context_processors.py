from .models import Category, Item, Article


def common(request):
    context = {
        'category_l': Category.objects.all(),
        'item_l': Item.objects.db_manager('finance').filter(loan4=1)[:3],
        'article_l': Article.objects.all()[:6],
    }
    return context