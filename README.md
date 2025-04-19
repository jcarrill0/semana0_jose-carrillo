# 🛠️ Herramientas a instalar
Proyecto de backend con inteligencia artificial: Es fundamental instalar las siguientes herramientas: `Python 3.13`, `Ollama`, el modelo `deepseek-r1` y `Postman`.

## Python 3.13
**Descarga:** [Descargar Python 3.13](https://www.python.org/downloads/release/python-3130/)

**Instrucciones de instalación:**

1. Haz clic en el enlace de descarga y selecciona el instalador adecuado para tu sistema operativo (Windows, macOS o Linux).
2. Ejecuta el archivo descargado y sigue las instrucciones del asistente de instalación.
3. Asegúrate de marcar la opción `"Add Python to PATH"` para facilitar el uso de Python desde la terminal.

## Ollama

**Descarga:** [Descargar Ollama](https://ollama.com/download)

**Instrucciones de instalación:**

1. Descarga el archivo correspondiente para tu sistema operativo.
2. Comprime y extrae el contenido en una carpeta de tu elección.
3. Abre la terminal y navega a la carpeta de extracción, y ejecuta el comando de instalación personalizado proporcionado en su documentación.

## Modelo deepseek-r

**Instrucciones de instalación:**

1. Una vez que tengas Ollama instalado, abre la terminal.
2. Ejecuta el siguiente comando para descargar el modelo:

``` shell
ollama pull deepseek-r
```
3. Espera a que el modelo se descargue completamente antes de continuar.
## Postman

Descripción: Postman es una herramienta fundamental para probar APIs. Permite
enviar solicitudes HTTP y analizar respuestas de una manera intuitiva.

**Descarga:** [Descargar Postman](https://www.postman.com/downloads/)

**Instrucciones de instalación:**

1. Visita el enlace y selecciona el instalador apropiado.
2. Ejecuta el archivo descargado y sigue las instrucciones del instalador.
3. Al finalizar, abre Postman y crea una cuenta gratuita para acceder a todas las funcionalidades.  

# 📁 Estructura del Proyecto
A continuación, se describen los pasos para configurar el proyecto y la instalación de las librerías necesarias.

### Estructura de archivos del proyecto

semana0_nombre-pasante/  
│  
├── app/                # Carpeta principal del código    
│   ├── main.py         # Archivo principal para ejecutar la aplicación  
│           
├── .env                # Archivo para gestionar variables de entorno  
├── requirements.txt    # Archivo para las dependencias del proyecto  
└── README.md           # Documento explicativo del proyecto 

### Configuración del Entorno Virtual

La utilización de un entorno virtual es una buena práctica en el desarrollo de
Python, ya que te permite gestionar las librerías de manera independiente. Para
crear un entorno virtual, sigue los siguientes pasos:

1. Crear el entorno virtual: Ejecuta el siguiente comando en la terminal:

``` shell
python - m venv env
```
Esto creará un entorno virtual llamado env.

2. Activar el entorno virtual:
- Para Windows:

``` shell
.\env\Scripts\activate
```

- Para macOS o Linux:

``` shell
source env/bin/activate
```

Una vez activado, verás que el nombre del entorno aparece al inicio de la línea de
tu terminal.

#### Instalación de Librerías Necesarias

Ahora que tienes tu entorno virtual configurado, es momento de instalar las
librerías necesarias para el proyecto. Utiliza los siguientes comandos:

``` shell
pip install fastapi uvicorn requests python-dotenv ollama
```
### Descripción de Librerías:

- **FastAPI:** Framework para construir APIs de alta eficiencia.
- **Uvicorn:** Servidor ASGI para ejecutar tu aplicación FastAPI.
- **Requests:** Librería para realizar solicitudes HTTP.
- **Python-dotenv:** Permite trabajar con archivos .env para gestionar variables de entorno.
- **Ollama:** Herramienta para ejecutar modelos de IA localmente.


## Probar la API con Postman
#### Endpoint Preguntar

```http
  POST http://127.0.0.1:8000/preguntar
```
#### Body
```json
{
    "texto": "¿Cuál es la capital de Francia?"
}
``` 

| Attribute | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `texto` | `string` | **Required**. |

#### Response

```json
{
    "respuesta": "Esta es una respuesta simulada para: ¿Cuál es la capital de Francia?"
}
``` 
  
# 🔍 Investigación

## 1. ¿Qué es Ollama?
Ollama es una herramienta o framework diseñado para facilitar la ejecución y gestión de modelos de lenguaje grandes (LLM, por sus siglas en inglés) de manera local. Permite a los desarrolladores descargar, ejecutar y personalizar modelos como Llama, Mistral u otros, optimizando su uso en entornos locales o en servidores. Ollama simplifica el proceso de implementación al proporcionar una interfaz sencilla para interactuar con estos modelos, gestionar recursos y ajustar parámetros clave.

## 2. ¿Qué es FastAPI?
FastAPI es un framework moderno y rápido para construir APIs web en Python. Está diseñado para ser altamente eficiente y fácil de usar, aprovechando las ventajas de Python 3.7+ y sus características de tipado estático. FastAPI se destaca por su capacidad para manejar solicitudes asíncronas, lo que lo hace ideal para aplicaciones que requieren alto rendimiento, como APIs que consumen modelos de IA pesados. Además, genera automáticamente documentación interactiva (Swagger y ReDoc) basada en los endpoints definidos.

## 3. ¿Qué es el modelo deepseek-r1?
El modelo **deepseek-r1** es uno de los modelos de lenguaje desarrollados por DeepSeek, una empresa especializada en inteligencia artificial. Este modelo pertenece a la familia de modelos de lenguaje grandes (LLM) y está diseñado para tareas avanzadas de procesamiento del lenguaje natural (NLP), como generación de texto, traducción, resumen y más. El sufijo "r1" puede indicar una versión específica o una iteración del modelo, optimizada para ciertos casos de uso o mejoras en rendimiento.

## 4. Uso de peticiones con stream=True
El uso de `stream=True` en bibliotecas como `requests` de Python permite recibir respuestas de manera incremental, en lugar de esperar a que toda la respuesta esté disponible antes de procesarla. Esto es especialmente útil cuando se trabaja con APIs que generan datos en tiempo real o cuando se manejan respuestas grandes que podrían sobrecargar la memoria. Por ejemplo:

```python
import requests

# Realizar una solicitud con stream=True
response = requests.get('https://api.ejemplo.com/stream', stream=True)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Iterar sobre los fragmentos de la respuesta
    for chunk in response.iter_content(chunk_size=1024):  # Leer en bloques de 1 KB
        if chunk:  # Ignorar fragmentos vacíos
            print(chunk.decode('utf-8'))  # Decodificar y procesar el fragmento
else:
    print(f"Error: {response.status_code}")
```
En este caso, los datos se procesan en fragmentos (`chunks`), lo que mejora la eficiencia y reduce el uso de recursos.

## 5. ¿Cómo garantizar la escalabilidad de una API que consume modelos de IA pesados?
Para garantizar la escalabilidad de una API que consume modelos de IA pesados, se pueden implementar las siguientes estrategias:
- **Contenedores y orquestación :** Usar Docker para contenerizar las instancias del modelo y Kubernetes para gestionar la escalabilidad horizontal.
- **Caché :** Implementar sistemas de caché (como Redis) para almacenar respuestas frecuentes y reducir la carga en los modelos.
- **Colas de mensajes :** Utilizar colas como RabbitMQ o Kafka para manejar solicitudes de manera asincrónica y distribuir la carga.
- **Balanceo de carga :** Configurar un balanceador de carga (como NGINX o AWS ELB) para distribuir las solicitudes entre múltiples instancias del modelo.
- **Optimización de modelos :** Reducir el tamaño del modelo mediante técnicas como cuantización o pruning sin comprometer significativamente la calidad.
- **Autoscaling :** Implementar políticas de escalado automático basadas en métricas como CPU, memoria o latencia.

## 6. ¿Qué parámetros de Ollama (ej: num_ctx, temperature) afectan el rendimiento/calidad de respuestas?
Algunos de los parámetros clave de Ollama que afectan el rendimiento y la calidad de las respuestas incluyen:

- **num_ctx :** Define el tamaño máximo del contexto (en tokens) que el modelo puede considerar. Un valor más alto permite respuestas más contextualizadas pero aumenta el uso de recursos.
- **temperature :** Controla la aleatoriedad de las respuestas. Valores más bajos (cerca de 0) generan respuestas más deterministas y conservadoras, mientras que valores más altos (cerca de 1 o superior) producen respuestas más creativas pero menos predecibles.
- **top_k y top_p :** Filtran las opciones de salida del modelo. top_k limita el número de palabras candidatas, mientras que top_p selecciona las palabras basadas en la probabilidad acumulativa.
- **max_tokens :** Define el número máximo de tokens que el modelo generará en la respuesta. Un valor más alto permite respuestas más largas pero puede aumentar el tiempo de procesamiento.

## 7. ¿Qué estrategias usar para balancear carga entre múltiples instancias de Ollama?
Para balancear la carga entre múltiples instancias de Ollama, se pueden implementar las siguientes estrategias:

- **Balanceador de carga :** Usar herramientas como NGINX, HAProxy o AWS Elastic Load Balancer para distribuir las solicitudes entre las instancias.
- **Orquestación con Kubernetes :** Implementar Kubernetes para gestionar dinámicamente las instancias de Ollama, asegurando que las solicitudes se distribuyan equitativamente.
- **Colas de trabajo :** Utilizar sistemas de colas como Celery, RabbitMQ o Kafka para enviar solicitudes a diferentes instancias según su disponibilidad.
- **Health checks :** Configurar verificaciones de salud para detectar instancias no disponibles y redirigir el tráfico solo a las instancias activas.
- **Sharding :** Dividir las solicitudes según criterios específicos (por ejemplo, por tipo de tarea o usuario) para asignarlas a instancias específicas.

## 8. ¿Qué patrones de diseño (ej: CQRS, Singleton) son útiles para integrar modelos de IA en backend?
Algunos patrones de diseño útiles para integrar modelos de IA en backend incluyen:
- CQRS (Command Query Responsibility Segregation) : Separa las operaciones de lectura y escritura, permitiendo optimizar el procesamiento de consultas y comandos. Esto es útil cuando las consultas a modelos de IA son intensivas en recursos.
- **Singleton :** Asegura que solo exista una instancia del modelo de IA en memoria, reduciendo el consumo de recursos y mejorando la eficiencia.
- **Facade :** Proporciona una interfaz simplificada para interactuar con el modelo de IA, ocultando la complejidad de su implementación.
- **Observer :** Permite que múltiples componentes del sistema reaccionen a eventos generados por el modelo de IA, como la finalización de una tarea.
- **Pipeline :** Divide el procesamiento en etapas secuenciales, lo que facilita la gestión de flujos de trabajo complejos, como la preprocesamiento de datos, inferencia y postprocesamiento.
- **Adapter :** Convierte la interfaz del modelo de IA en una interfaz compatible con el resto del sistema, facilitando su integración.