from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter

from api.views.viewsets import GalleryViewSet, PictureViewSet, SculptureViewSet

extended_router = ExtendedSimpleRouter()
router = DefaultRouter()

extended_router.register(r'galleries', GalleryViewSet, basename='galleries').\
    register(r'pictures', PictureViewSet, basename='pictures', parents_query_lookups=['gallery'])
extended_router.register(r'galleries', GalleryViewSet, basename='galleries').\
    register(r'sculptures', SculptureViewSet, basename='sculptures', parents_query_lookups=['gallery'])

router.register(r'pictures', PictureViewSet, basename='pictures')
router.register(r'sculptures', SculptureViewSet, basename='sculptures')

urlpatterns = extended_router.urls + router.urls
