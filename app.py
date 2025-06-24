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
    modelo_url = url_for('static', filename='img/modelo_pdf.jpg', _external=True)
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

    # ✅ Esta parte es clave para Render
    config = pdfkit.configuration(wkhtmltopdf=os.path.join(os.getcwd(), 'bin/wkhtmltopdf'))
    pdf = pdfkit.from_string(html, False, options=options, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=clientes.pdf'
    return response


if __name__ == '__main__':
    app.run(debug=True)
