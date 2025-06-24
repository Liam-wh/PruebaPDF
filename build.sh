#!/usr/bin/env bash

mkdir -p bin

# 1. Descarga el AppImage
curl -L -o bin/wkhtmltopdf.appimage https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.alpine3.17_amd64.AppImage

# 2. Da permisos
chmod +x bin/wkhtmltopdf.appimage

# 3. Extrae el contenido
bin/wkhtmltopdf.appimage --appimage-extract

# 4. Mueve el ejecutable real a bin/wkhtmltopdf
mv squashfs-root/usr/local/bin/wkhtmltopdf bin/wkhtmltopdf

# 5. Limpieza (opcional)
rm -rf squashfs-root
rm bin/wkhtmltopdf.appimage
