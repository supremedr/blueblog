from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import TemplateView
from accounts.views import UserRegistrationView
from django.contrib.auth import views as auth_views
# from django.contrib.auth import login
# from django.contrib.auth import logout
from blog.views import NewBlogView
from blog.views import HomeView
from blog.views import UpdateBlogView
from blog.views import NewBlogPostView
from blog.views import UpdateBlogPostView
from blog.views import BlogPostDetailsView
from blog.views import SharePostWithBlog
from blog.views import StopSharingPostWithBlog
from blog.views import ShareBlogPostView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(),name='home'),
    path('new-user/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', auth_views.LoginView.as_view() , name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home') , name='logout'),
    path('blog/new/', NewBlogView.as_view(), name='new-blog'),
    path('blog/<int:pk>/update/', UpdateBlogView.as_view(), name='update-blog'),
    path('blog/post/new/', NewBlogPostView.as_view(), name='new-blogpost'),
    path('blog/post/<int:pk>/update/', UpdateBlogPostView.as_view(), name='update-blog-post'),
    path('blog/post/<int:pk>/', BlogPostDetailsView.as_view(), name='blog-post-details'),
    path('blog/post/<int:pk>/share/', ShareBlogPostView.as_view(), name='share-blog-post-with-blog'),
    path('blog/post/<int:post_pk>/share/to/<int:blog_pk>/',SharePostWithBlog.as_view(), name='share-post-with-blog'),
    path('blog/post/<int:post_pk>/stop/share/to/<int:blog_pk>/', StopSharingPostWithBlog.as_view(), name='stop-sharing-post-with-blog'),
]
