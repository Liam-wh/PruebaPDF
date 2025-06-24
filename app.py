from flask import Flask, render_template, url_for, make_response
import pdfkit
import os

app = Flask(__name__)

# Datos simulados
clientes = [
    {'nombre': 'Juan Pérez', 'documento': '123456', 'correo': 'juan@example.com', 'telefono': '71234567'},
    {'nombre': 'Ana Gómez', 'documento': '654321', 'correo': 'ana@example.com', 'telefono': None},
]

@app.route('/')
def index():
    return render_template('cliente/index.html', clientes=clientes)

@app.route('/pdf')
def generar_pdf():
    # Ruta absoluta a la imagen en el sistema de archivos
    modelo_path = os.path.join(app.root_path, 'static', 'img', 'modelo_pdf.jpg')
    modelo_url = 'file://' + modelo_path  # Ruta local para wkhtmltopdf

    html = render_template('pdf/cliente_pdf.html', clientes=clientes, modelo_url=modelo_url)
    options = {
        'enable-local-file-access': '',
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'margin-top': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'margin-right': '0mm',
        'no-outline': None,
    }

    # Usar wkhtmltopdf instalado globalmente, sin configuración personalizada
    pdf = pdfkit.from_string(html, False, options=options)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=clientes.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)
