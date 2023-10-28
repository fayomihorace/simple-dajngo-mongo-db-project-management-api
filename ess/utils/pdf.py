from io import BytesIO
from io import BytesIO
from django.utils.translation import gettext_lazy as _
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from rest_framework import serializers

from main.models import Project


# FIXME: this function is too long and doing several things. Split it.
def generate_project_report_pdf(project_id) -> BytesIO:
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist as e:
        raise serializers.ValidationError({"error": "Project not found"}) from e
    except ValueError as e:
        raise serializers.ValidationError({"error": "Invalid project ID"}) from e

    print("----request: ", project_id)

    # Create a PDF buffer
    buffer = BytesIO()

    # Create a PDF document
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Define title and styles
    title_text = _("Report of project {project}").format(project=str(project))
    title_style = getSampleStyleSheet()['Title']
    # title_style.textColor = colors.Color("#006600")
    # Create a title paragraph
    title = Paragraph(title_text, title_style)

    project_info = {
        _("Company name"): project.company_name,
        _("Start_date"): str(project.start_date),
        # _("Owner name"): project.owner_name,
        # _("Sector"): project.sector,
        # _("Country"): project.country,
        # _("Users"): ",".join([usr.username for usr in project.users.all()]),
    }

    project_info_paragraphs = []
    for field, value in project_info.items():
        # Create a centered paragraph for each field-value pair
        project_info_paragraph = Paragraph(
            f'<para align=center>{field}: {value}</para>', getSampleStyleSheet()['Normal']
        )
        project_info_paragraphs.append(project_info_paragraph)
    
    # project_info_paragraphs.append(Paragraph(f'<para><br></br></para>'))

    # Create data for the table
    data = [
        [_("Tasks"), _("Assigned user"), _("Start date"), _("Due date")],
    ]
    for task in project.tasks.all():
        data.append([
            task.name,
            task.assigned_user.username,
            str(task.start_date),
            str(task.due_date),
        ])

    # Create the table and add data
    table = Table(data, colWidths=100, rowHeights=30)

    # Define table styles, including borders
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Text alignment
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
        ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),  # Data background color
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),  # Table border
        ('GRID', (0, 0), (-1, 0), 1, (0, 0, 0)),  # Header-row border
        ('BOX', (0, 0), (-1, -1), 1, (0, 0, 0)),  # Table border
    ])

    table.setStyle(table_style)

    # Combine elements in the desired order
    elements = [title] + project_info_paragraphs + [table]

    # Build the PDF and write it to the buffer
    doc.build(elements)
    return buffer
