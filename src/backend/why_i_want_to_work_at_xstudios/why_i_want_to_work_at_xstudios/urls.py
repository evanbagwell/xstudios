from django.urls import path
from api.views import generate_sudoku, validate_sudoku

urlpatterns = [
    path('api/sudoku/generate/', generate_sudoku),
    path('api/sudoku/validate/', validate_sudoku),
]
