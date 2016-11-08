#coding=utf-8
from haystack.generic_views import SearchView
class MySearchView(SearchView):
	def get_context_data(self,*args,**kwargs):
		context = super(MySearchView,self).get_context_data(*args,**kwargs)
		context['user_name'] = self.request.session.get('name',default='')
		print self.request
		print "这是搜索的",context
		return context