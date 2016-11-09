from haystack import indexes
from .models import Goods


class GoodsIndex(indexes.SearchIndex, indexes.Indexable):

    """
    商品搜索
    """

    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Goods