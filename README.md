===============================
 DETECTOR DE PLAGIO EN PDF
===============================

Este proyecto es una aplicación web en Python que compara dos documentos PDF utilizando técnicas de Procesamiento de Lenguaje Natural (PLN) para detectar posibles plagios. Incluye análisis léxico, comparación de n-gramas y visualización de las palabras más frecuentes.

---------------------
FUNCIONALIDADES
---------------------
- Subida de dos archivos PDF desde una interfaz web.
- Extracción y limpieza del texto.
- Eliminación de stopwords en español.
- Cálculo de la riqueza léxica por documento.
- Generación de n-gramas y comparación.
- Visualización con gráficos de las palabras más repetidas.
- Cálculo de porcentaje de similitud.

-----------------------------
 TECNOLOGÍAS UTILIZADAS
-----------------------------
- Python 3.x
- Flask
- NLTK
- matplotlib
- re (expresiones regulares)
- PyMuPDF (fitz)
- Bootstrap (opcional para interfaz)

---------------------
 INSTALACIÓN
---------------------
1. Clona el repositorio:
   git clone https://github.com/tu-usuario/detector-plagio-pdf.git
   cd detector-plagio-pdf

2. Crea y activa un entorno virtual (opcional):
   python -m venv venv
   venv\Scripts\activate     (en Windows)
   source venv/bin/activate  (en Linux/macOS)

3. Instala dependencias:
   pip install -r requirements.txt

4. Descarga recursos de NLTK:
   >>> import nltk
   >>> nltk.download('punkt')
   >>> nltk.download('stopwords')

5. Ejecuta la app:
   python app.py
   Accede desde http://127.0.0.1:5000

------------------------
 CÓMO FUNCIONA
------------------------
1. El usuario sube dos PDFs.
2. Se extrae y limpia el texto.
3. Se eliminan stopwords.
4. Se calcula la riqueza léxica.
5. Se comparan n-gramas.
6. Se muestran resultados:
   - % de similitud
   - Riqueza léxica
   - Palabras más frecuentes (gráfico)

--------------------------------------
 ESTRUCTURA SUGERIDA DEL PROYECTO
--------------------------------------
detector-plagio-pdf/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── wordcloud.png (o gráfico)
├── utils/
│   └── procesamiento.py
├── requirements.txt
└── README.txt

![image](https://github.com/user-attachments/assets/198718d8-9635-4768-a266-570b533e545b)
