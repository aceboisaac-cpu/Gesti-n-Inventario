# Planificación: Sistema de Gestión de Inventario (Monolito Django)

## Stack Tecnológico
- **Framework:** Django 5.x (Todo en Python: Lógica y Templates)
- **Base de Datos:** SQLite (Perfecto para desarrollo y pruebas técnicas)
- **Calidad de Código:** Ruff (Linter/Formatter), Pytest-django (Testing profesional)
- **CI/CD:** GitHub Actions (Validación automática de PRs)

---

## Fases del Desarrollo (Iterativo)

### Fase 1: Setup del Entorno y Estructura Django
- [x] Inicializar repositorio Git.
- [x] Crear entorno virtual (`venv`) e instalar `django`, `ruff` y `pytest-django`.
- [x] Crear el proyecto Django y la aplicación `inventory`.
- [x] Configurar herramientas de calidad y crear el pipeline de GitHub Actions (`.github/workflows/django-ci.yml`).

### Fase 2: Modelo de Datos y Migraciones
- [x] Definir el modelo `Product` en `models.py` (nombre, precio, stock, categoría).
- [x] Ejecutar migraciones para crear la base de datos SQLite.
- [x] **Extra Pro:** Registrar el modelo en el `admin.py` para tener un panel de control inmediato.

### Fase 3: Lógica de Formularios y Validaciones
- [ ] Crear `forms.py` usando `ModelForm`.
- [ ] Implementar las validaciones personalizadas (precio > 0, stock >= 0). Django ya maneja campos obligatorios por defecto.

### Fase 4: Vistas (CRUD) y URLs
- [ ] Configurar las URLs de la aplicación.
- [ ] Implementar las vistas (recomiendo usar **Class-Based Views** como `ListView`, `CreateView`, `UpdateView` y `DeleteView` para demostrar dominio del framework).
- [ ] Implementar la funcionalidad de búsqueda filtrando el QuerySet en la vista de listado.

### Fase 5: Frontend con Django Templates
- [ ] Crear una `base.html` para la estructura general y bloques de contenido.
- [ ] Crear los templates para cada acción (listado, creación, edición, confirmación de borrado).
- [ ] Aplicar estilos CSS (limpios y funcionales) aprovechando las etiquetas de Django.

### Fase 6: Testing y Refinado
- [ ] Escribir tests para los modelos y las vistas usando `pytest`.
- [ ] Asegurar que el sistema de búsqueda y las validaciones funcionan como se espera.
- [ ] Documentar el `README.md` con los pasos para ejecutar el servidor y crear un superusuario.
