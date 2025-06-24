#!/usr/bin/env bash

mkdir -p bin

# Descarga el AppImage directamente
curl -L -o bin/wkhtmltopdf https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.alpine3.17_amd64.AppImage

# Dale permisos de ejecución
chmod +x bin/wkhtmltopdf
