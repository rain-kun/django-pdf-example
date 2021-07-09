from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import uuid
from django.conf import settings

def save_pdf(params:dict):
    template = get_template('pdf_constructor/pdf_style.html')

    html = template.render(params)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), response)
    pdf_name = uuid.uuid4()


    try:
        with open(str(settings.BASE_DIR) + f'/static/{pdf_name}.pdf', 'wb+') as output:
            pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), output)

    except Exception as e:
        print(e)

    if pdf.err:
        return '', False

    return pdf_name, True