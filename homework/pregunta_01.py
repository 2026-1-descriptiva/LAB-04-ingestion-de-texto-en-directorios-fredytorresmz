# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


#def pregunta_01():
"""
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
             ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

     ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """




import os
import pandas as pd


def pregunta_01():
    """
    Construye los archivos train_dataset.csv y test_dataset.csv
    a partir de los archivos .txt organizados por clase.
    """

    # función que recorre la carpeta base y arma el dataset
    def construir_dataset(ruta_base):
        datos = []

        #print(f"\nIniciando lectura en: {ruta_base}")

        # Recorremos las carpetas de clase en orden
        for sentimiento in sorted(os.listdir(ruta_base)):
            ruta_sentimiento = os.path.join(ruta_base, sentimiento)

            # Solo seguimos si li carpeta válida
            if os.path.isdir(ruta_sentimiento):
                print(f"Carpeta encontrada: {ruta_sentimiento}")

                # Leemos los archivos .txt de esa carpeta
                for archivo in sorted(os.listdir(ruta_sentimiento)):
                    if archivo.endswith(".txt"):
                        ruta_archivo = os.path.join(ruta_sentimiento, archivo)

                        with open(ruta_archivo, "r", encoding="utf-8") as file:
                            frase = file.read().strip()

                        # Mostramos cómo se va cargando cada registro
                        print(f"  Archivo leído: {ruta_archivo}")
                        print(f"  Clase asignada: {sentimiento}")
                        print(f"  Frase cargada: {frase[:70]}...")

                        datos.append({
                            "phrase": frase,
                            "target": sentimiento
                        })

        print(f"Total de registros cargados desde {ruta_base}: {len(datos)}")
        return pd.DataFrame(datos)

    # Detectamos la ruta de trabajo
    if os.path.exists("./files/input/train"):
        ruta_train = "./files/input/train"
        ruta_test = "./files/input/test"
        ruta_output = "./files/output"
    else:
        ruta_train = "input/train"
        ruta_test = "input/test"
        ruta_output = "output"

    # Creamos la carpeta de salida
    os.makedirs(ruta_output, exist_ok=True)
    print(f"\nCarpeta de salida lista: {ruta_output}")

    # Construimos los datasets
    train_dataset = construir_dataset(ruta_train)
    test_dataset = construir_dataset(ruta_test)

    # Definimos las rutas finales de salida
    archivo_train = os.path.join(ruta_output, "train_dataset.csv")
    archivo_test = os.path.join(ruta_output, "test_dataset.csv")

    # Guardamos los CSV
    train_dataset.to_csv(archivo_train, index=False)
    test_dataset.to_csv(archivo_test, index=False)

    # Confirmamos si los archivos sí quedaron creados
    print(f"\nArchivo train guardado: {archivo_train}")
    print(f"¿Existe train_dataset.csv?: {os.path.exists(archivo_train)}")

    print(f"\nArchivo test guardado: {archivo_test}")
    print(f"¿Existe test_dataset.csv?: {os.path.exists(archivo_test)}")