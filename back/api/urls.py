from rest_framework.routers import DefaultRouter

from api.views.viewsets import GalleryViewSet, PictureViewSet, SculptureViewSet

router = DefaultRouter()

router.register(r'galleries', GalleryViewSet, basename='galleries')
router.register(r'pictures', PictureViewSet, basename='pictures')
router.register(r'sculpture', SculptureViewSet, basename='sculptures')

urlpatterns = router.urls
