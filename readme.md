# 🛍️ Product Parser

Este proyecto es un parser de productos que procesa un archivo JSON, filtra los productos activos y genera instancias de la clase `Product` con información relevante, como el rating promedio, las imágenes mas grandes y el punto de encuentro.

## 🚀 Características

- **Filtrado de productos activos**: Solo procesa productos con el estado `ACTIVE`.
- **Cálculo de rating promedio**: Calcula el rating promedio basado en las reseñas de los productos.
- **Extracción de imágenes**: Obtiene la URL de la variante más grande de cada imagen.
- **Extracción del punto de encuentro**: Extrae el punto de encuentro de la descripción del producto.
- **Generación de JSON**: Convierte los productos procesados a formato JSON.

## 📦 Estructura del proyecto
```
.
├── main.py              # 🚀 Punto de entrada del programa
├── parser.py            # 🛠️ Lógica para parsear productos
├── product.py           # 🧩 Clase Product con validaciones
├── product_data.json    # 📂 Archivo JSON de ejemplo con datos de productos
├── README.md            # 📄 Este archivo (documentación del proyecto)
└── test_parser.py       # 🧪 Pruebas unitarias para el parser
```

## 🛠️ Requisitos

- Python 3.10.12 o superior.
- Dependencias: No se requieren dependencias externas.

## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/JavierTorres1193/python_test.git
  
2. Navega al directorio del proyecto:
   ```bash
   cd tu-repositorio

4. Ejecuta el script principal:
   ```bash
   python main.py

## 📄 Ejemplo de JSON de entrada

El archivo `product_data.json` debe tener la siguiente estructura:

```
{
  "products": [
    {
      "status": "ACTIVE",
      "reviews": {
        "reviewCountTotals": [
          { "rating": 1, "count": 1 },
          { "rating": 2, "count": 4 },
          { "rating": 3, "count": 8 },
          { "rating": 4, "count": 1 },
          { "rating": 5, "count": 2 }
        ]
      },
      "images": [
        {
          "variants": [
            { "width": 100, "url": "https://example.com/image1_small.jpg" },
            { "width": 500, "url": "https://example.com/image1_large.jpg" }
          ]
        }
      ],
      "description": "Meeting point: Park Central\n\nDetails here."
    }
  ]
}
```

## 📤 Salida esperada

El programa generará un JSON con la siguiente estructura para cada producto activo:

```

{
  "averageRating": 3.12,
  "images": [
    "https://example.com/image1_large.jpg"
  ],
  "meetingPoint": "Park central"
}
```

## 🧪 Pruebas

Para ejecutar las pruebas unitarias, usa el siguiente comando:

python -m unittest test_parser.py
