from rest_framework.routers import SimpleRouter
from core_learn_race import views


router = SimpleRouter()

router.register(r'race', views.RaceViewSet, 'Race')
router.register(r'player', views.PlayerViewSet, 'Player')
router.register(r'question', views.QuestionViewSet, 'Question')

urlpatterns = router.urls
