from django.urls import path

from blog.views import (
    article_list_view,
    article_detail_view,
    article_create_view,
    article_update_view,
    article_delete_view,
)

from blog.views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

from blog.views import (
    ArticleDetailView_1,
    ArticleListView_1,
    ArticleCreateView_1,
    ArticleUpdateView_1,
    ArticleDeleteView_1,
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView_1.as_view(), name='article_list'),
    path('create/', ArticleCreateView_1.as_view(), name='article_create'),
    path('<int:id>/', ArticleDetailView_1.as_view(), name='article_detail'),
    path('<int:id>/update/', ArticleUpdateView_1.as_view(), name='article_update'),
    path('<int:id>/delete/', ArticleDeleteView_1.as_view(), name='article_delete'),
]
