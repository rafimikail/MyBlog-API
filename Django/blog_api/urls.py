from .views import AdminPostDetail, CreatePost, DeletePost, EditPost, PostList, PostDetail, PostListDetailfilter, PublicPosts
#from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls

# urlpatterns = [
#     path('search/', PostListDetailfilter.as_view(), name='postsearch'),
#     path('', PostList.as_view(), name='listcreate'),
#     path('posts/', PostDetail.as_view(), name='detailcreate'),
#     path('admin/create/', CreatePost.as_view(), name='createpost'),
#     path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
#     path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
#     path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
# ]

urlpatterns = [
    path('', PostList.as_view(), name='listpost'),
    path('post/<str:pk>/', PostDetail.as_view(), name='detailpost'),
    path('search/', PostListDetailfilter.as_view(), name='searchpost'),
    path('publicposts/', PublicPosts.as_view(), name='publicposts'),
    # Post Admin URLs
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]