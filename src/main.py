from models import Libro, Cliente
if __name__ == "__main__":
    # Imprime un mensaje inicial para indicar el comienzo de la simulación.
    print("--- Simulación del Sistema de Gestión de Librería ---")
     # 1. Crear algunos objetos Libro
    # Esta sección se dedica a crear instancias (objetos) de la clase Libro.
    # Cada línea crea un libro diferente con sus propios atributos.
    # Se utilizan los parámetros definidos en el método __init__ de la clase Libro.
    # 'stock': Cantidad inicial de copias disponibles para la venta.
    # 'precio_venta': Precio al que la librería venderá el libro.
    # 'precio_compra': Precio al que la librería compró el libro (opcional).
    # 'genero': Género del libro.
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", 3, 15.50, 8.00, "Realismo Mágico")
    libro2 = Libro("1984", "George Orwell", "978-0451524935", 1, 12.00, 6.00, "Distopía")
    # libro3 se crea con stock 0 para probar la funcionalidad de reserva más adelante.
    libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-8424119934", 0, 20.00, 10.00, "Novela Clásica")
    libro4 = Libro("El Hobbit", "J.R.R. Tolkien", "978-0345339683", 2, 10.00, 5.00, "Fantasía")

    # Imprime un encabezado para mostrar el estado inicial de los libros.
    print("\n--- Libros disponibles (estado inicial) ---")
    # Llama al método __str__ de cada objeto Libro para obtener una representación legible.
    print(libro1)
    print(libro2)
    print(libro3)
    print(libro4)