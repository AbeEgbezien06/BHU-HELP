from django.urls import path, include
from .views import complaint, ComplaintDetail, ComplaintViewSet, CategoryDetail, newItemForm
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'complaints', ComplaintViewSet)

app_name = 'core'
urlpatterns = [
    path('pending/', complaint.as_view()),
    path('core/', include(router.urls)),
    path('core/complaints/<slug:category_slug>/<slug:complaint_slug>/', ComplaintDetail.as_view()),
    path('core/complaints/<slug:category_slug>/', CategoryDetail.as_view()),
    path('pending/newissue/', newItemForm, name='new')
    
]

# todo: 
# 1. finish the project
# 2. work on url routing and json responses to axios
# 3. work on forms.py (optional)
# prepare for hosting
# 4. switch to railway db