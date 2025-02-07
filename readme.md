# 🛍️ Product Parser

Este proyecto es un parser de productos que procesa un archivo JSON, filtra los productos activos y genera instancias de la clase `Product` con información relevante, como el rating promedio, las imágenes mas grandes y el punto de encuentro.

## 🚀 Características

- **Filtrado de productos activos**: Solo procesa productos con el estado `ACTIVE`.
- **Cálculo de rating promedio**: Calcula el rating promedio basado en las reseñas de los productos.
- **Extracción de imágenes**: Obtiene la URL de la variante más grande de cada imagen.
- **Extracción del punto de encuentro**: Extrae el punto de encuentro de la descripción del producto.
- **Generación de JSON**: Convierte los productos procesados a formato JSON.

## 📦 Estructura del proyecto
.
├── main.py
├── parser.py
├── product.py
├── product_data.json ##
├── README.md
└── test_parser.py

## 🛠️ Requisitos

- Python 3.10.12 o superior.
- Dependencias: No se requieren dependencias externas.

## 🚀 Cómo ejecutar el proyecto

1### Clona el repositorio:
  git clone [[URL_DEL_REPOSITORIO]](https://github.com/JavierTorres1193/python_test.git
  
2### Navega al directorio del proyecto:
  cd tu-repositorio

3### Ejecuta el script principal:
  python main.py

## 📄 Ejemplo de JSON de entrada
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
## 📤 Salida esperada
{
  "averageRating": 3.12,
  "images": [
    "https://example.com/image1_large.jpg"
  ],
  "meetingPoint": "Park central"
}
## 🧪 Pruebas

Para ejecutar las pruebas unitarias, usa el siguiente comando:

python -m unittest test_parser.py
