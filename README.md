# Word-Clustering
A Python 3 that returns semantic clusters out of a given text
# Clustering de palabras: Informe
----------------------------------------
## Introducción
--------------
El propósito de este trabajo fue probar una de las técnicas más primitivas del aprendizaje no supervisado aplicado la minería de datos de texto. Los algoritmos de _clustering_ (o agrupamiento) consisten en agrupar los vectores, en este caso correspondientes a las palabras con sus _features_, y según la distancia entre estas, agrupar en un mismo _cluster_ a aquellas más cercanas en la representación utilizada, que en este caso es una matriz de correlación.

## Recursos utilizados
----------------------------------------
### Corpus
Para el proyecto se utilizó el corpus compuesto por noticias extraídas de la página web del diario La Voz del Interior provisto por la cátedra.
### Script
Fue realizado mediante el lenguaje de programación Python 3 y las siguientes bibliotecas de código:
  - [__Sci-kit Learn__](http://scikit-learn.org) versión 0.19.0 para las tareas referidas a vectorización y aprendizaje automático.
  - [__Spacy__](http://scikit-learn.org) versión 1.7.0 para el preprocesamiento y tokenización del texto.
  - [__NLTK__](http://www.nltk.org) versión 3.2.5 por su diccionario de stop words, que dio mejores resultados que Spacy.
  - Bibliotecas internas de [Python__](https://docs.python.org/3/)

## Procedimiento
----------------------------------------
### Tokenización
Se utilizó el tokenizador de Spacy, eliminando signos de puntuación y stopwords basándonos en el corpus de stopwords de NLTK. Sin embargo, se pueden observar artículos en los clusters (esto se corregirá en el próximo release)
### Features y vectorización
Para formar los vectores se seleccionaron las siguientes features para cada palabra:
- El lema de la palabra.
- La estimación de su probabilidad logarítmica
- Su etiqueta POS
- La tripla de dependencia, conformada por función, palabra objetivo y núcleo
- El string de la palabra

Luego, se generaron los vectores utilizando [__DictVectorizer__](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html) de Sci-kit Learn
### K-Means
Se usó la implementación de Sci-kit Learn del algoritmo sobre la matriz obtenida en el paso anterior con los siguientes parámetros:
- Al principio se alternó entre cinco y diez para el número de clusters, pero se optó por diez ya que a mi parecer delimita mejor las categorías semánticas.
- Como método de inicialización se utilizó "k-means++", que, según su descripción, selecciona los centroides iniciales para los clusters de forma tal que agiliza la convergencia.

## Evaluación de los resultados
----------------------------------------
### Descargo
Para llegar a evaluar el clustering sobre el corpus, primero se realizó sobre un cuarto y luego la mitad de éste, obteniendo luego resultados similares en la totalidad del corpus. Debe aclararse que la evaluación se hizo "a ojo", por lo que los patrones descriptos en los clusters son puramente una opinión personal. En este [link](https://drive.google.com/file/d/0BzrjG-S-fb8MblV5YkwyNzRTam8/view?usp=sharing) se pueden apreciar los resultados iniciales y el resultado final.
### Visualización
Se optó por no graficar los resultados en un diagrama, sino imprimir los clusters directamente a un archivo de texto.
### Resultados
| Cluster       | Patrones      | Ejemplos  |
| ------------- |:-------------:| ---------:|
| 0     | Términos afectivos - Educación | (pareja, amor, separados, parejas, familia, casados), (educación, colegios, Ministerio, colegios, estudiantes, escuelas) |
| 1     | Política - Gobierno | (mestrismo, delasotismo, juecistas, vicentistas, riutoristas, giacominismo), (Sifcos, Fedecom, reestatizada, transparentó, retrotraigan) |
| 2 | Números - cuantificadores      | (dos, tres, cuatro, cinco, nueve, mil), (ambos, cientos, incontables, miles) |
| 3 | Empresas - Apellidos - Movimientos    | (Crese, Tamse, Mastellone, Apross, Eximbank), (Accastello, Passerini, Balbis, Pisoni, Osatinsky, Conci), (brahmanismo, troskos, anarcos, antikirchneristas, vecinalistas, alfonsinismo) |
| 4 | Verbos en pasado      | (conducía, iban, murieron, lograron, viajaron, informó) |
| 5 | Pueblos de Córdoba - Apellidos de políticos -  | (Salsipuedes, Caroya, Laboulaye, Cumbrecita, Totoral, Celman, Jovita), (Riutort, Aguad, Giacomino, Birri, Yasky)|
| 6 | No se observaron patrones      | - |
| 7 | Meses - Palabras en inglés    | (enero, febrero, marzo, junio, julio, agosto, septiembre, octubre, noviembre), (time, age, country, down, state, stock, line, web) |
| 8 | Palabras compuestas o con prefijos  | (inhabilitado, inmunoprevenibles, frutihortícola, acéfalo, despegados, desconfiados, interempresarial, incontrolables, reincorporado) |
| 9 | Ambientalismo - Relativo al Peronismo |(megaminería, polución, glifosato, desmontes, hídrico), (De la Sota, Schiaretti, FPV, Peronismo, Urtubey, Alperovich, Carlotto, Bonafini, justicialista, kirchnerista) |


## Conclusión
----------------------------------------
El clustering usando K-Means es una de las peores alternativas a la hora de procesar texto, sin embargo, cuando a priori no se tiene ningún otro método al alcance puede brindar cierta información con respecto a las categorías semánticas dentro del corpus. En este caso deberían haberse utilizado más clusters, pero por limitaciones (sobre todo de tiempo) se hizo el análisis en base a diez clusters, dándonos esto cierta delimitación entre las distintas categorías semánticas y/o sintácticas presentes en el corpus de La Voz del Interior. 



