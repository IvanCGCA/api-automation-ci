# 🚀 API Automation + CI/CD Pipeline (GitHub Actions)

Este proyecto implementa un flujo de **Integración Continua (CI)** profesional. No solo automatiza las pruebas de una API, sino que garantiza que cada cambio en el código sea validado automáticamente en la nube antes de ser aceptado.

## 🎯 Objetivo del Proyecto
Demostrar la capacidad de orquestar pruebas automatizadas en entornos efímeros (contenedores de Linux) utilizando **GitHub Actions**, asegurando que el "build" del software sea estable en todo momento.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.12
* **Testing Framework:** Pytest
* **API Client:** Requests
* **CI/CD Tool:** GitHub Actions (Workflows en YAML)
* **OS de Ejecución:** Ubuntu Latest (Cloud)

## 🏗️ Estructura del Pipeline
El flujo de trabajo (`main.yml`) realiza los siguientes pasos automáticamente en cada `push`:
1. **Checkout:** Descarga el código fuente en un servidor virtual.
2. **Setup:** Configura el entorno de Python 3.12.
3. **Dependencies:** Instala todas las librerías necesarias desde `requirements.txt`.
4. **Execution:** Corre la suite de pruebas y genera un reporte de éxito o fallo.

## 🧪 Pruebas Ejecutadas
- **Validación de Status Codes:** Asegura que los endpoints principales respondan correctamente (HTTP 200).
- **Integridad de JSON:** Verifica que la estructura de los datos devueltos coincida con las reglas de negocio.
- **Pruebas de Contrato:** Validación de IDs y tipos de datos en la respuesta de la API.

---
*Proyecto desarrollado por **Ivan Vega** - QA Backend Engineer*
