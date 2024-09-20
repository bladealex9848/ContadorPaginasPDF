# Registro de Cambios

Todos los cambios notables en el proyecto Contador de Páginas PDF Multimétodo serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a [Versionado Semántico](https://semver.org/lang/es/).

## [1.2.0] - 2024-09-20

### Añadido
- Generación de informes en memoria utilizando `io.StringIO()`.
- Marca de tiempo única en el nombre de cada archivo de informe descargado.
- Uso de `tempfile.NamedTemporaryFile` para manejar archivos PDF temporales con la extensión correcta.

### Cambiado
- Reemplazado el método personalizado de descarga por `st.download_button` de Streamlit.
- Eliminados los estilos CSS personalizados para utilizar la apariencia predeterminada de Streamlit.
- Mejorado el manejo de archivos temporales para aumentar la seguridad y eficiencia.

### Eliminado
- Función `get_binary_file_downloader_html` obsoleta.
- Escritura de informes en archivos temporales en el servidor.

### Seguridad
- Mejorada la gestión de datos sensibles al procesar todo en memoria y no guardar nada en el servidor.

### Justificación de los cambios

1. Generación de informes en memoria:
   - Mejora la seguridad al evitar escribir datos sensibles en el sistema de archivos del servidor.
   - Reduce el riesgo de conflictos entre usuarios concurrentes.

2. Marca de tiempo en nombres de archivo:
   - Garantiza la unicidad de cada informe generado.
   - Facilita la organización y seguimiento de informes para los usuarios.

3. Uso de `tempfile.NamedTemporaryFile`:
   - Mejora la compatibilidad con diferentes bibliotecas de procesamiento de PDF.
   - Asegura la limpieza automática de archivos temporales.

4. Cambio a `st.download_button`:
   - Mejora la integración con Streamlit y su manejo nativo de descargas.
   - Simplifica el código y mejora la mantenibilidad.

5. Eliminación de estilos CSS personalizados:
   - Mejora la consistencia visual con otras aplicaciones Streamlit.
   - Facilita futuras actualizaciones y mantenimiento.

### Impacto esperado
- Mayor seguridad en el manejo de datos de los usuarios.
- Mejor experiencia de usuario con una interfaz más consistente y responsiva.
- Reducción de potenciales errores relacionados con la gestión de archivos temporales.
- Mejora en la escalabilidad de la aplicación para múltiples usuarios concurrentes.

### Próximos pasos
- Implementar pruebas automatizadas para los nuevos flujos de procesamiento en memoria.
- Explorar opciones para mejorar el rendimiento en el procesamiento de archivos PDF grandes.
- Considerar la adición de más formatos de informe (por ejemplo, CSV, JSON) según las necesidades de los usuarios.

## [1.1.0] - 2024-09-20

### Añadido
- Implementación de una interfaz web utilizando Streamlit.
- Capacidad para procesar múltiples archivos PDF simultáneamente.
- Generación de un informe descargable con los resultados del conteo.
- Visualización de bibliotecas disponibles en la barra lateral de la interfaz web.

### Cambiado
- Refactorización del código para soportar tanto la versión de escritorio como la web.
- Mejora en el manejo de errores y logging para una mejor depuración.
- Optimización del proceso de conteo de páginas para manejar PDFs protegidos sin contraseña.

### Eliminado
- Dependencia de pdftk como método de conteo debido a problemas de compatibilidad multiplataforma.

### Justificación de los cambios

1. Implementación de interfaz web:
   - Accesibilidad mejorada: Permite a los usuarios utilizar la herramienta sin necesidad de instalación local.
   - Experiencia de usuario mejorada: Proporciona una interfaz gráfica intuitiva y fácil de usar.

2. Procesamiento de múltiples archivos:
   - Eficiencia mejorada: Permite a los usuarios procesar lotes de PDFs en una sola operación.
   - Ahorro de tiempo: Reduce significativamente el tiempo necesario para procesar grandes volúmenes de documentos.

3. Informe descargable:
   - Mejor seguimiento: Facilita a los usuarios mantener un registro de los resultados del conteo.
   - Integración con flujos de trabajo: Permite incorporar fácilmente los resultados en otros procesos o sistemas.

4. Visualización de bibliotecas disponibles:
   - Transparencia: Informa a los usuarios sobre las capacidades actuales del sistema.
   - Facilita la resolución de problemas: Ayuda a identificar rápidamente si faltan dependencias necesarias.

5. Refactorización y mejoras en el manejo de errores:
   - Mantenibilidad mejorada: Facilita futuras actualizaciones y expansiones del sistema.
   - Robustez: Mejora la capacidad del sistema para manejar casos extremos y errores inesperados.

6. Optimización para PDFs protegidos:
   - Versatilidad: Mejora la capacidad del sistema para manejar una mayor variedad de tipos de PDF.
   - Experiencia de usuario mejorada: Reduce la necesidad de intervención manual para PDFs protegidos.

7. Eliminación de dependencia de pdftk:
   - Portabilidad mejorada: Facilita la instalación y uso del sistema en diferentes plataformas.
   - Simplificación: Reduce la complejidad de la instalación y configuración del sistema.

### Impacto esperado
- Mayor adopción del sistema debido a la facilidad de uso de la interfaz web.
- Incremento en la productividad de los usuarios al procesar grandes volúmenes de PDFs.
- Mejora en la capacidad de manejar una amplia variedad de tipos de PDF, incluyendo documentos protegidos.
- Reducción en los problemas de instalación y compatibilidad entre diferentes sistemas operativos.

### Próximos pasos
- Implementar pruebas automatizadas para garantizar la estabilidad en futuras actualizaciones.
- Explorar la posibilidad de añadir capacidades de OCR para mejorar la precisión en PDFs escaneados.
- Considerar la implementación de un sistema de caché para mejorar el rendimiento en procesamiento repetitivo.

### Notas adicionales
- Se recomienda a los usuarios actualizar a la última versión para beneficiarse de estas mejoras.
- Los usuarios que dependían de pdftk deben revisar la documentación actualizada para alternativas.

## [1.0.0] - 2024-09-15

### Añadido
- Implementación inicial del Contador de Páginas PDF Multimétodo.
- Soporte para PyPDF2, pikepdf y pdfminer.six como métodos de conteo.
- Interfaz de línea de comandos básica para procesar archivos PDF individuales.
- Sistema de logging para seguimiento de operaciones y errores.

### Justificación de la versión inicial
- Necesidad identificada de una herramienta robusta para contar páginas en diversos tipos de PDFs.
- Enfoque en la versatilidad al incorporar múltiples bibliotecas de procesamiento de PDF.
- Diseño inicial centrado en la funcionalidad core para validar el concepto y la demanda del mercado.

### Impacto esperado
- Proporcionar a los usuarios una herramienta confiable para el conteo de páginas en PDFs complejos.
- Establecer una base sólida para futuras expansiones y mejoras del sistema.

### Próximos pasos planificados
- Recopilar feedback de usuarios iniciales para informar el desarrollo futuro.
- Explorar la posibilidad de añadir una interfaz gráfica para mejorar la accesibilidad.
- Investigar métodos adicionales para manejar PDFs altamente protegidos o dañados.