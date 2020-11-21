from . import views
from django.urls import path

urlpatterns = [ 
	path('', views.index, name="home"),
	path('add-pin/', views.uploadImage, name="add-pin"),
	path('my-pin/<int:id>/',views.details,name='view'),
	path('update-pin/<int:id>/',views.editPin,name='edit-pin'),
	path('pin/<int:id>/',views.pinDetail,name='view-pin'),
	path('comment/', views.postComment, name="postComment"),
	path('profile/',views.profile,name='profile'),
	
]

