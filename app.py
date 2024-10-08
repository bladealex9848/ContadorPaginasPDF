import streamlit as st
import tempfile
import logging
from typing import List, Tuple
from datetime import datetime
import io

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Importación condicional de las bibliotecas necesarias
def import_pdf_libraries():
    libraries = {}
    try:
        import PyPDF2
        libraries['PyPDF2'] = PyPDF2
    except ImportError:
        logging.warning("PyPDF2 no está instalado.")

    try:
        import pikepdf
        libraries['pikepdf'] = pikepdf
    except ImportError:
        logging.warning("pikepdf no está instalado.")

    try:
        from pdfminer.pdfparser import PDFParser
        from pdfminer.pdfdocument import PDFDocument
        libraries['pdfminer'] = (PDFParser, PDFDocument)
    except ImportError:
        logging.warning("pdfminer.six no está instalado.")

    return libraries

# Importar las bibliotecas
pdf_libraries = import_pdf_libraries()

# Función para contar páginas de PDF
def get_pdf_pages(file_path: str, password: str = None) -> int:
    """
    Intenta contar las páginas de un PDF utilizando múltiples métodos.
    
    Args:
    file_path (str): Ruta al archivo PDF.
    password (str, optional): Contraseña del PDF, si está protegido.
    
    Returns:
    int: Número de páginas del PDF, o -1 si no se pudo determinar.
    """
    methods = [
        ('PyPDF2', get_pdf_pages_pypdf2),
        ('pikepdf', get_pdf_pages_pikepdf),
        ('pdfminer', get_pdf_pages_pdfminer),
    ]

    for method_name, method in methods:
        if method_name in pdf_libraries:
            try:
                pages = method(file_path, password)
                if pages > 0:
                    logging.info(f"Éxito usando {method_name}: {pages} páginas")
                    return pages
            except Exception as e:
                logging.warning(f"Error en {method_name}: {str(e)}")

    logging.error(f"No se pudo determinar el número de páginas para {file_path}")
    return -1

# Funciones específicas para cada biblioteca
def get_pdf_pages_pypdf2(file_path: str, password: str = None) -> int:
    PyPDF2 = pdf_libraries['PyPDF2']
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        if pdf_reader.is_encrypted:
            pdf_reader.decrypt(password or '')
        return len(pdf_reader.pages)

def get_pdf_pages_pikepdf(file_path: str, password: str = None) -> int:
    pikepdf = pdf_libraries['pikepdf']
    with pikepdf.Pdf.open(file_path, password=password or '') as pdf:
        return len(pdf.pages)

def get_pdf_pages_pdfminer(file_path: str, password: str = None) -> int:
    PDFParser, PDFDocument = pdf_libraries['pdfminer']
    with open(file_path, 'rb') as file:
        parser = PDFParser(file)
        document = PDFDocument(parser, password=password or '')
        return len([0 for _ in document.get_pages()])

# Configuración de la página
st.set_page_config(
    page_title="Contador de Páginas PDF",
    page_icon="📄",
    layout="wide"
)

# Título y descripción
st.title("📄 Contador de Páginas PDF Multimétodo")

st.write("""
[![ver código fuente](https://img.shields.io/badge/Repositorio%20GitHub-gris?logo=github)](https://github.com/bladealex9848/ContadorPaginasPDF)
![Visitantes](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fcontadorpaginaspdf.streamlit.app&label=Visitantes&labelColor=%235d5d5d&countColor=%231e7ebf&style=flat)
""")

st.markdown("""
Esta aplicación te permite contar el número de páginas en archivos PDF, incluso si están protegidos o firmados electrónicamente.
Simplemente sube tus archivos y obtén el conteo de páginas de forma rápida y sencilla.
""")

# Carga de archivos
uploaded_files = st.file_uploader("Carga tus archivos PDF", type=["pdf"], accept_multiple_files=True)

# Contraseña opcional para PDFs protegidos
password = st.text_input("Contraseña (opcional para PDFs protegidos)", type="password")

if st.button("Procesar PDFs"):
    if uploaded_files:
        st.write("Procesando archivos...")
        results: List[Tuple[str, int]] = []
        
        # Crear un directorio temporal
        with tempfile.TemporaryDirectory() as tmpdirname:
            for uploaded_file in uploaded_files:
                # Guardar el archivo en el directorio temporal
                temp_file_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf", dir=tmpdirname).name
                with open(temp_file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Contar páginas
                pages = get_pdf_pages(temp_file_path, password if password else None)
                results.append((uploaded_file.name, pages))
        
        # Mostrar resultados
        st.subheader("Resultados")
        for name, pages in results:
            if pages > 0:
                st.success(f"📁 **{name}**: {pages} páginas")
            else:
                st.error(f"📁 **{name}**: No se pudo determinar el número de páginas")
        
        # Generar informe en memoria
        report_content = io.StringIO()
        report_content.write("Informe de Conteo de Páginas\n")
        report_content.write(f"Generado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for name, pages in results:
            report_content.write(f"{name}: {'No determinado' if pages < 0 else pages} páginas\n")
        
        # Crear botón de descarga
        st.download_button(
            label="Descargar Informe",
            data=report_content.getvalue(),
            file_name=f"informe_conteo_paginas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )
    else:
        st.warning("Por favor, sube al menos un archivo PDF.")

# Información adicional
st.sidebar.title("Información")
st.sidebar.info("""
Esta aplicación utiliza múltiples métodos para contar las páginas de los PDFs:
- PyPDF2
- pikepdf
- pdfminer.six

Si un método falla, la aplicación intentará con el siguiente hasta obtener un conteo exitoso.
""")

# Mostrar bibliotecas disponibles
st.sidebar.subheader("Bibliotecas disponibles:")
for lib in pdf_libraries:
    st.sidebar.success(f"✅ {lib}")
for lib in set(['PyPDF2', 'pikepdf', 'pdfminer']) - set(pdf_libraries.keys()):
    st.sidebar.error(f"❌ {lib}")

# Footer
st.markdown("---")
st.markdown("Desarrollado por Alexander Oviedo Fadul | [GitHub](https://github.com/bladealex9848)")