import os
import logging
import subprocess

# Configuración del sistema de logging para registrar información y errores
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_pdf_pages(file_path, password=None):
    """
    Intenta obtener el número de páginas de un archivo PDF usando múltiples métodos.
    
    Args:
    file_path (str): Ruta al archivo PDF.
    password (str, optional): Contraseña del PDF, si está protegido.
    
    Returns:
    int: Número de páginas del PDF, o 1 si no se pudo determinar.
    """
    # Lista de métodos a intentar, en orden de preferencia
    methods = [
        get_pdf_pages_pypdf2,
        get_pdf_pages_pikepdf,
        get_pdf_pages_pdfminer,
        get_pdf_pages_pdftk
    ]

    # Intenta cada método en la lista hasta que uno tenga éxito
    for method in methods:
        try:
            pages = method(file_path, password)
            if pages > 0:
                logging.info(f"Éxito usando {method.__name__}: {pages} páginas")
                return pages
        except Exception as e:
            logging.warning(f"Error en {method.__name__}: {str(e)}")

    # Si todos los métodos fallan, registra un error y devuelve 1
    logging.error(f"No se pudo determinar el número de páginas para {file_path}")
    return 1

def get_pdf_pages_pypdf2(file_path, password=None):
    """
    Usa PyPDF2 para contar páginas en un PDF.
    
    Args:
    file_path (str): Ruta al archivo PDF.
    password (str, optional): Contraseña del PDF, si está protegido.
    
    Returns:
    int: Número de páginas del PDF.
    
    Raises:
    ImportError: Si PyPDF2 no está instalado.
    """
    try:
        import PyPDF2
    except ImportError:
        logging.error("PyPDF2 no está instalado. Instálalo con: pip install PyPDF2")
        return 0

    # Abre el archivo PDF
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        # Si el PDF está encriptado, intenta descifrarlo
        if pdf_reader.is_encrypted:
            if password:
                pdf_reader.decrypt(password)
            else:
                pdf_reader.decrypt('')
        # Devuelve el número de páginas
        return len(pdf_reader.pages)

def get_pdf_pages_pikepdf(file_path, password=None):
    """
    Usa pikepdf para contar páginas en un PDF.
    
    Args:
    file_path (str): Ruta al archivo PDF.
    password (str, optional): Contraseña del PDF, si está protegido.
    
    Returns:
    int: Número de páginas del PDF.
    
    Raises:
    ImportError: Si pikepdf no está instalado.
    """
    try:
        import pikepdf
    except ImportError:
        logging.error("pikepdf no está instalado. Instálalo con: pip install pikepdf")
        return 0

    # Abre el PDF con pikepdf y cuenta las páginas
    with pikepdf.Pdf.open(file_path, password=password) as pdf:
        return len(pdf.pages)

def get_pdf_pages_pdfminer(file_path, password=None):
    """
    Usa pdfminer.six para contar páginas en un PDF.
    
    Args:
    file_path (str): Ruta al archivo PDF.
    password (str, optional): Contraseña del PDF, si está protegido.
    
    Returns:
    int: Número de páginas del PDF.
    
    Raises:
    ImportError: Si pdfminer.six no está instalado.
    """
    try:
        from pdfminer.pdfparser import PDFParser
        from pdfminer.pdfdocument import PDFDocument
    except ImportError:
        logging.error("pdfminer.six no está instalado. Instálalo con: pip install pdfminer.six")
        return 0

    # Abre el archivo y crea un parser PDF
    with open(file_path, 'rb') as file:
        parser = PDFParser(file)
        document = PDFDocument(parser, password=password)
        # Cuenta las páginas iterando sobre ellas
        return len([0 for _ in document.get_pages()])

def get_pdf_pages_pdftk(file_path, password=None):
    """
    Usa pdftk (herramienta externa) para contar páginas en un PDF.
    
    Args:
    file_path (str): Ruta al archivo PDF.
    password (str, optional): Contraseña del PDF, si está protegido.
    
    Returns:
    int: Número de páginas del PDF.
    
    Nota: Requiere que pdftk esté instalado en el sistema.
    """
    try:
        # Prepara el comando pdftk
        cmd = ['pdftk']
        if password:
            cmd.extend(['input_pw', password])
        cmd.extend([file_path, 'dump_data'])
        
        # Ejecuta el comando y captura la salida
        output = subprocess.check_output(cmd, universal_newlines=True)
        
        # Busca la línea que contiene el número de páginas
        for line in output.split('\n'):
            if line.startswith('NumberOfPages:'):
                return int(line.split(':')[1])
    except subprocess.CalledProcessError:
        logging.error("Error al ejecutar pdftk. Asegúrate de que esté instalado en tu sistema.")
    except FileNotFoundError:
        logging.error("pdftk no está instalado en tu sistema.")
    return 0

def main():
    """
    Función principal para demostrar el uso del contador de páginas PDF.
    """
    # Lista de archivos PDF de ejemplo
    pdf_files = [
        'documento_normal.pdf',
        'documento_protegido.pdf',
        'documento_firmado.pdf'
    ]

    # Itera sobre cada archivo PDF
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            # Intenta contar las páginas (usa None como contraseña si no está protegido)
            pages = get_pdf_pages(pdf_file, password='contraseña')
            print(f"Archivo: {pdf_file}, Páginas: {pages}")
        else:
            print(f"El archivo {pdf_file} no existe.")

# Punto de entrada del script
if __name__ == "__main__":
    main()