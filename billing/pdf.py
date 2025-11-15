from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse

def generate_invoice_pdf(invoice):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.invoice_number}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    y = 750

    p.drawString(50, y, f"Invoice Number: {invoice.invoice_number}")
    y -= 20
    p.drawString(50, y, f"Customer: {invoice.customer.name}")
    y -= 20
    p.drawString(50, y, f"Email: {invoice.customer.email}")
    y -= 20

    for item in invoice.items.all():
        y -= 30
        p.drawString(50, y, f"{item.description} - {item.quantity} × {item.unit_price}")

    y -= 40
    p.drawString(50, y, f"Total: ${invoice.total}")

    p.showPage()
    p.save()
    return response
