# 🚘 MaxiAutosFinal

Proyecto final desarrollado con Django para la materia de Desarrollo Web.  
Incluye un sistema completo de gestión y visualización de vehículos, con múltiples funcionalidades avanzadas, diseño personalizado y panel de administración.

---

## 📌 Características principales

### 🔹 Navegación completa
- Menú superior con Inicio, Categorías, Listado y Favoritos.
- Botón minimalista para volver al inicio (solo visible fuera de la página principal).

### 🔹 Sistema de vehículos
- Carga y visualización de vehículos.
- Múltiples imágenes por vehículo.
- Carrusel tipo MercadoLibre en la vista de detalle.
- Miniaturas sincronizadas con la imagen principal.

### 🔹 Categorías
- Listado de categorías en tarjetas/botones.
- Filtrado por categoría.
- Búsqueda combinada con categoría.

### 🔹 Buscador avanzado
- Solo muestra resultados cuando se ingresa texto.
- Mensajes flotantes indicando resultados.

### 🔹 Sistema de favoritos
- Usuarios pueden agregar o quitar vehículos de favoritos.
- Solo disponible para usuarios logueados.
- Mensajes de confirmación.

### 🔹 Permisos
- Solo administradores pueden crear, editar o eliminar vehículos.
- Usuarios comunes solo pueden visualizar.

### 🔹 Panel de administración
- Gestión completa de vehículos, categorías e imágenes.
- Acceso mediante `/admin`.

---

## 🛠️ Instalación del proyecto

1. Clonar el repositorio:
```bash
git clone https://github.com/tuusuario/MaxiAutosFinal.git
cd MaxiAutosFinal
