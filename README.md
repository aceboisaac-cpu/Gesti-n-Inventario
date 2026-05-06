# 📦 Sistema de Gestión de Inventario

Un sistema de gestión de inventario construido bajo la arquitectura MVT (Model-View-Template) de Django. Este proyecto fue desarrollado con un enfoque estricto en la calidad del código, integridad de datos y diseño UI/UX.

## ✨ Características Principales

- **CRUD Completo**: Creación, lectura, actualización y eliminación segura de productos.
- **Buscador en Tiempo Real**: Filtrado dinámico de productos por nombre (`icontains`).
- **Integridad de Datos**: Validaciones rigurosas a nivel de Modelo y Formulario (prevención de stock negativo, control de precisión decimal para precios).
- **Diseño (Glassmorphism)**: Interfaz de usuario moderna con efecto cristal, construida con CSS nativo y Bootstrap 5.
- **Panel de Control**: Sidebar lateral responsiva y navegación intuitiva.
- **Calidad Asegurada**: Cobertura de tests automatizados para reglas de negocio y vistas, además de cumplimiento estricto de estándares de código (Linting).

## 🛠️ Stack Tecnológico

- **Backend**: Python 3.12+, Django 6.0
- **Base de Datos**: SQLite (por defecto)
- **Frontend**: HTML5, CSS3 (Glassmorphism), Bootstrap 5 (CDN), FontAwesome
- **Testing & QA**: Pytest, Pytest-Django
- **Linter & Formatter**: Ruff

## 🚀 Instalación y Uso

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/Gestion-Inventario.git
cd Gestion-Inventario
```

### 2. Crear y activar entorno virtual
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones
```bash
python manage.py migrate
```

### 5. Crear superusuario (Opcional, para panel de Admin)
```bash
python manage.py createsuperuser
```

### 6. Levantar el servidor
```bash
python manage.py runserver
```
Visita `http://127.0.0.1:8000/` en tu navegador para ver la aplicación funcionando.

## 🧪 Testing y Calidad

El proyecto cuenta con una suite de pruebas automatizadas y herramientas de calidad de código.

**Para correr los tests:**
```bash
pytest
```

**Para verificar el estilo de código (Linter):**
```bash
python -m ruff check .
```

---
*Desarrollado con pasión y buenas prácticas de ingeniería de software.*
