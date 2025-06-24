#!/usr/bin/env bash

mkdir -p bin

# Descarga AppImage
curl -L -o bin/wkhtmltopdf https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.alpine3.17_amd64.AppImage

# Dale permisos de ejecución
chmod +x bin/wkhtmltopdf

# Monta AppImage una vez (esto la "extrae")
bin/wkhtmltopdf --appimage-extract

# Usa el ejecutable real
mv squashfs-root/usr/local/bin/wkhtmltopdf bin/wkhtmltopdf
