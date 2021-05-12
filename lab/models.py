from django.db import models


class Item(models.Model):
    """
    カードローン
    """
    class Meta:
        db_table = 'loan'
    loan4 = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    name_id = models.CharField(max_length=20)
    kariretaImages2_250250 = models.CharField(max_length=70, null=True)
    kariretaImages2_32050 = models.CharField(max_length=70, null=True)
    kariretaLinkurl = models.CharField(max_length=70, null=True)
    limit = models.CharField(max_length=15)
    Annualrate = models.CharField(max_length=20)
    examination = models.CharField(max_length=11)
    loantime = models.CharField(max_length=11)
    point = models.TextField(null=True)
    selectRank = models.IntegerField(null=True)
    limit_id = models.IntegerField(null=True)
    loantime_id = models.IntegerField(null=True)
    sokujitu = models.IntegerField(default=0)
    murisoku = models.IntegerField(default=0)
    raitenhuyou = models.IntegerField(default=0)
    compWeb = models.IntegerField(default=0)
    noneCheck = models.IntegerField(default=0)
    applyWeekend = models.IntegerField(default=0)
    teirate = models.IntegerField(default=0)
    shufu = models.IntegerField(default=0)
    syunyuusyoumei = models.IntegerField(default=0)
    highlimit = models.IntegerField(default=0)
    attention = models.TextField(null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    カテゴリー名
    """
    name = models.CharField('カテゴリ名', max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    appear_r = models.IntegerField(default=0)
    item_id = models.ForeignKey(
        Item,
        verbose_name='アイテム',
        on_delete=models.PROTECT,
        null=True)
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT,
        null=True)  # カテゴリー削除でItemは消さない

    def __str__(self):
        return self.title