from django.http import FileResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from utils.pdf import generate_project_report_pdf


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def generate_project_report_pdf_view(request, project_id):
    """View to generate a project report."""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    buffer = generate_project_report_pdf(project_id)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
