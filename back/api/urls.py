from views.viewsets import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'galleries', GalleryListViewSet, basename='galleries')
router.register(r'pictures', PictureListViewSet, basename='pictures')

urlpatterns = router.urls

