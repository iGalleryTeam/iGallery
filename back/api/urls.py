from rest_framework.routers import DefaultRouter

from api.views.viewsets import GalleryViewSet, PictureViewSet

router = DefaultRouter()

router.register(r'galleries', GalleryViewSet, basename='galleries')
router.register(r'pictures', PictureViewSet, basename='pictures')

urlpatterns = router.urls
