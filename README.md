![Logo de ContadorPaginasPDF](https://github.com/bladealex9848/ContadorPaginasPDF/blob/main/assets/logo.jpg)

# Contador de Páginas PDF Multimétodo

## Tabla de Contenidos
1. [Descripción](#descripción)
2. [Características Principales](#características-principales)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Requisitos del Sistema](#requisitos-del-sistema)
5. [Instalación](#instalación)
6. [Uso](#uso)
   - [Versión de Línea de Comandos](#versión-de-línea-de-comandos)
   - [Versión Web](#versión-web)
7. [Configuración](#configuración)
8. [Manejo de PDFs Protegidos](#manejo-de-pdfs-protegidos)
9. [Solución de Problemas](#solución-de-problemas)
10. [Contribución](#contribución)
11. [Registro de Cambios](#registro-de-cambios)
12. [Preguntas Frecuentes](#preguntas-frecuentes)
13. [Créditos](#créditos)
14. [Licencia](#licencia)

## Descripción

El Contador de Páginas PDF Multimétodo es una herramienta robusta y versátil diseñada para contar el número de páginas en archivos PDF, incluyendo aquellos que están protegidos o firmados electrónicamente. Este proyecto responde a la necesidad de manejar diversos tipos de documentos PDF en entornos judiciales y administrativos, donde la precisión en el conteo de páginas es crucial para la gestión de expedientes electrónicos.

La aplicación utiliza múltiples bibliotecas de procesamiento de PDF para garantizar la máxima compatibilidad y precisión, adaptándose a diferentes tipos de documentos y niveles de protección.

## Características Principales

- **Múltiples Métodos de Conteo**: Utiliza PyPDF2, pikepdf y pdfminer.six para máxima compatibilidad.
- **Manejo de PDFs Protegidos**: Capacidad para procesar PDFs con contraseña o firmados electrónicamente.
- **Interfaz Dual**: 
  - Versión de línea de comandos para integración en scripts y automatizaciones.
  - Interfaz web intuitiva construida con Streamlit para uso fácil y accesible.
- **Procesamiento por Lotes**: Capacidad para contar páginas de múltiples PDFs simultáneamente.
- **Generación de Informes**: Crea informes descargables con los resultados del conteo.
- **Logging Detallado**: Sistema de registro para facilitar la depuración y el seguimiento de operaciones.
- **Manejo Robusto de Errores**: Intenta múltiples métodos antes de declarar un PDF como no procesable.
- **Visualización de Capacidades**: Muestra las bibliotecas disponibles en la interfaz web.

## Estructura del Proyecto

```
ContadorPaginasPDF/
│
├── main.py                   # Script principal para la versión de línea de comandos
├── app.py                    # Aplicación web Streamlit
├── requirements.txt          # Lista de dependencias
├── .gitignore                # Archivos y directorios ignorados por Git
├── README.md                 # Este archivo
└── CHANGELOG.md              # Registro de cambios del proyecto
└── assets/                   # Recursos estáticos como imágenes y logos
    ├── logo.jpg              # Logo del proyecto
```

## Requisitos del Sistema

- Python 3.7 o superior
- Bibliotecas Python especificadas en `requirements.txt`
- Acceso a internet para la instalación de dependencias

## Instalación

1. Clone el repositorio:
   ```
   git clone https://github.com/usuario/ContadorPaginasPDF.git
   cd ContadorPaginasPDF
   ```

2. Cree y active un entorno virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows use `venv\Scripts\activate`
   ```

3. Instale las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

### Versión de Línea de Comandos

1. Ejecute el script principal:
   ```
   python main.py
   ```

2. Siga las instrucciones en pantalla para procesar los archivos PDF.

### Versión Web

1. Inicie la aplicación Streamlit:
   ```
   streamlit run app.py
   ```

2. Abra su navegador y vaya a la dirección indicada por Streamlit (generalmente `http://localhost:8501`).

3. Use la interfaz web para cargar y procesar archivos PDF.

## Configuración

La aplicación no requiere configuración adicional para su funcionamiento básico. Sin embargo, puede ajustar los siguientes aspectos:

- **Logging**: Modifique el nivel de logging en `main.py` y `app.py` según sus necesidades de depuración.
- **Streamlit**: Puede personalizar la apariencia de la aplicación web editando el archivo `.streamlit/config.toml` (consulte la documentación de Streamlit para más detalles).

## Manejo de PDFs Protegidos

Para PDFs protegidos con contraseña:

1. En la versión de línea de comandos, se le solicitará la contraseña si es necesario.
2. En la versión web, hay un campo opcional para ingresar la contraseña antes de procesar los archivos.

Si no se proporciona una contraseña, la aplicación intentará procesar el PDF sin ella, lo cual puede funcionar para algunos tipos de protección.

## Solución de Problemas

- **Error: "X no está instalado"**: Asegúrese de haber instalado todas las dependencias listadas en `requirements.txt`.
- **No se puede determinar el número de páginas**: Intente con un método alternativo o verifique si el PDF está dañado.
- **La aplicación web no inicia**: Verifique que Streamlit esté instalado correctamente y que no haya conflictos de puertos.

Para problemas persistentes, consulte los logs o abra un issue en el repositorio de GitHub.

## Contribución

Las contribuciones son bienvenidas. Por favor, siga estos pasos:

1. Fork el repositorio.
2. Cree una nueva rama (`git checkout -b feature/AmazingFeature`).
3. Realice sus cambios y haga commit (`git commit -m 'Add some AmazingFeature'`).
4. Push a la rama (`git push origin feature/AmazingFeature`).
5. Abra un Pull Request.

Asegúrese de actualizar las pruebas según corresponda y de seguir las convenciones de código existentes.

## Registro de Cambios

Consulte el archivo [CHANGELOG.md](CHANGELOG.md) para ver el historial detallado de cambios del proyecto.

## Preguntas Frecuentes

**P: ¿Puede la aplicación procesar PDFs firmados digitalmente?**
R: Sí, la aplicación está diseñada para manejar varios tipos de PDFs, incluyendo aquellos con firmas digitales.

**P: ¿Qué hago si ninguno de los métodos puede contar las páginas de mi PDF?**
R: Asegúrese de que el PDF no esté corrupto. Si el problema persiste, podría tratarse de un PDF con protecciones avanzadas que nuestros métodos actuales no pueden procesar.

**P: ¿Es seguro usar esta aplicación con documentos confidenciales?**
R: La aplicación procesa los PDFs localmente y no envía información a servidores externos. Sin embargo, siempre se recomienda precaución al manejar documentos sensibles.

## Créditos

Desarrollado y mantenido por Alexander Oviedo Fadul, Profesional Universitario Grado 11 en el Consejo Seccional de la Judicatura de Sucre.

[GitHub](https://github.com/bladealex9848) | [Website](https://alexanderoviedofadul.dev/) | [Instagram](https://www.instagram.com/alexander.oviedo.fadul) | [Twitter](https://twitter.com/alexanderofadul) | [Facebook](https://www.facebook.com/alexanderof/) | [WhatsApp](https://api.whatsapp.com/send?phone=573015930519&text=Hola%20!Quiero%20conversar%20contigo!) | [LinkedIn](https://www.linkedin.com/in/alexander-oviedo-fadul/)

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - vea el archivo [MIT License](https://opensource.org/licenses/MIT) para más detalles.