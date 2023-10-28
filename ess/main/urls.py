from django.urls import path
from main.views import generate_project_report_pdf_view


urlpatterns = [
    path(
        r'api/generate-project-report-pdf/<str:project_id>',
        generate_project_report_pdf_view,
        name='generate_project_pdf'
    ),
]
