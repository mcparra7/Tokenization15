# Práctica NLTK análisis de frecuencia de palabras
import nltk
from nltk.tokenize import word_tokenize #Divide el texto en palabras
from nltk.corpus import stopwords # Elimina los conectores
from nltk.probability import FreqDist # Calcula la frecuencia de las palabras 

texto = """¿Cómo funciona la IA?
Las Inteligencias artificiales utilizan algoritmos y modelos matemáticos para procesar grandes cantidades de datos y tomar decisiones basadas en patrones y reglas establecidas a través del aprendizaje automático, que es la capacidad de una máquina para aprender de forma autónoma a partir de datos sin ser programada específicamente para hacerlo. De esta manera la IA puede mejorar su precisión y eficiencia con el tiempo.
Espero que esta informacion sobre la IA sea de gran apoyo para su formacion y aprendizaje"""

# Tokenizar el texto 
palabras = word_tokenize(texto,language='spanish')
print(palabras)

# Stopwords Eliminar los conectores

stopwords = set(stopwords.words('Spanish'))

# Filtramos las palabras que no estan en la lista de stop words 
palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stopwords and palabra.isalpha()]
print(palabras_filtradas)

# Analisis de frecuencia de palabras
frecuencia_palabras = FreqDist(palabras_filtradas)

# Mostrar la frecuencia de las 10 palabras más comunes 
print (frecuencia_palabras.most_common(10))


