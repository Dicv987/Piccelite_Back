# 📦 Sistema de Inventarios - API

Este proyecto es una API RESTful desarrollada con **FastAPI** y **Supabase** para gestionar un sistema de inventarios completo con módulos de productos, sucursales, compras, ventas, arqueos y más.

## 🚀 Tecnologías
- **FastAPI**: framework principal de backend.
- **Supabase**: base de datos y autenticación.
- **Python 3.10+**

## 📁 Estructura del Proyecto
```bash
app/
├── controllers/         # Lógica y acceso a base de datos por módulo
├── models/              # Modelos Pydantic (validador de datos)
├── routes/              # Endpoints organizados por entidad
├── routes.py            # Router principal que une todas las rutas
├── main.py              # Punto de entrada de la aplicación
```

## 📚 Documentación
La documentación completa de la API, con rutas, parámetros y ejemplos está disponible en el siguiente PDF:
👉 [API_Profesional_Inventarios_v2.pdf](./API_Profesional_Inventarios_v2.pdf)

## 📦 Módulos disponibles
Cada uno cuenta con su propio CRUD y lógica interna:
- Productos
- Sucursales
- Órdenes de Compra + Detalles
- Ventas + Detalles
- Inventario
- Arqueos + Detalles

## 🛠️ Ejecución del proyecto
1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/inventarios-api
```
2. Instala dependencias:
```bash
pip install -r requirements.txt
```
3. Configura tus variables de entorno en `.env`
4. Ejecuta FastAPI:
```bash
uvicorn app.main:app --reload
```

## ✅ Endpoints base
La mayoría de rutas están bajo el prefijo:
```
/api/
```

Ejemplo:
```
GET /api/productos
```

## ✍️ Autor
Hecho con 💙 por Diego Cano y Atzin Cruz