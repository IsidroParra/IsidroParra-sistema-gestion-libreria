# src/models.py

class Libro:
    def __init__(self, titulo, autor, isbn, stock, precio_venta, precio_compra=None, genero="Desconocido"):
        """
        Inicializa un nuevo objeto Libro para una librería de segunda mano.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            isbn (str): El ISBN único del libro.
            stock (int): La cantidad de copias disponibles para la venta.
            precio_venta (float): El precio al que se vende el libro.
            precio_compra (float, optional): El precio al que se compra el libro a un proveedor/donante.
                                            Puede ser None si es una donación pura.
            genero (str, optional): El género del libro. Por defecto es "Desconocido".
        """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.stock = stock  # Stock disponible para la venta
        self.precio_venta = precio_venta
        self.precio_compra = precio_compra
        self.genero = genero
        self.reservas_pendientes = 0 # Contador para reservas, puede ser >0 incluso con stock=0

    def vender(self, cantidad=1):
        """
        Intenta vender una o más copias del libro.
        Disminuye el stock si hay suficientes disponibles y no hay más reservas pendientes que stock.

        Args:
            cantidad (int): Número de copias a vender. Por defecto es 1.

        Returns:
            bool: True si la venta fue exitosa, False en caso contrario.
        """
        if self.stock >= cantidad and (self.stock - self.reservas_pendientes) >= cantidad:
            self.stock -= cantidad
            print(f"'{self.titulo}': {cantidad} unidad(es) vendida(s). Stock restante: {self.stock}.")
            return True
        elif self.stock < cantidad:
            print(f"No hay suficiente stock de '{self.titulo}'. Solo {self.stock} disponible(s).")
            return False
        else:
            print(f"'{self.titulo}' tiene {self.reservas_pendientes} reservas pendientes. No hay stock real disponible para venta inmediata.")
            return False

    def comprar(self, cantidad=1):
        """
        Registra la compra de nuevas copias del libro por parte de la librería.
        Aumenta el stock.

        Args:
            cantidad (int): Número de copias compradas. Por defecto es 1.
        """
        self.stock += cantidad
        print(f"'{self.titulo}': {cantidad} unidad(es) comprada(s) por la librería. Stock actual: {self.stock}")
        # Lógica para cumplir reservas si hay stock suficiente ahora
        if self.reservas_pendientes > 0 and self.stock > 0:
            print(f"    Hay {self.reservas_pendientes} reservas pendientes para '{self.titulo}'.")

    def aceptar_donacion(self, cantidad=1):
        """
        Registra la aceptación de donaciones de copias del libro.
        Aumenta el stock.

        Args:
            cantidad (int): Número de copias donadas. Por defecto es 1.
        """
        self.stock += cantidad
        print(f"'{self.titulo}': {cantidad} unidad(es) donada(s) y aceptada(s). Stock actual: {self.stock}")
        # Lógica para cumplir reservas si hay stock suficiente ahora
        if self.reservas_pendientes > 0 and self.stock > 0:
            print(f"    Hay {self.reservas_pendientes} reservas pendientes para '{self.titulo}'.")

    def reservar(self):
        """
        Permite reservar una copia del libro, incluso si el stock es 0.
        Incrementa el contador de reservas pendientes.
        """
        self.reservas_pendientes += 1
        print(f"'{self.titulo}' ha sido reservado. Reservas pendientes: {self.reservas_pendientes}. Stock actual: {self.stock}")
        if self.stock == 0:
            print("    (El libro está actualmente agotado, esta es una reserva anticipada).")

    def __str__(self):
        """
        Representación en cadena del objeto Libro para una fácil visualización.
        """
        estado_reservas = f", Reservas Pendientes: {self.reservas_pendientes}" if self.reservas_pendientes > 0 else ""
        return f"Título: {self.titulo}, Autor: {self.autor}, Stock: {self.stock}, Precio: {self.precio_venta}€, ISBN: {self.isbn}{estado_reservas}"


class Cliente:
    def __init__(self, nombre, apellido, id_cliente):
        """
        Inicializa un nuevo objeto Cliente.

        Args:
            nombre (str): El nombre del cliente.
            apellido (str): El apellido del cliente.
            id_cliente (str): El ID único del cliente.
        """
        self.nombre = nombre
        self.apellido = apellido
        self.id_cliente = id_cliente
        self.libros_adquiridos = [] # Una lista para guardar los objetos Libro que el cliente ha comprado/reservado

    def adquirir_libro(self, libro, es_reserva=False):
        """
        Permite a un cliente adquirir un libro (comprarlo o reservarlo).

        Args:
            libro (Libro): El objeto Libro que el cliente desea adquirir.
            es_reserva (bool): True si es una reserva, False si es una compra inmediata.

        Returns:
            bool: True si la adquisición fue exitosa, False en caso contrario.
        """
        if es_reserva:
            libro.reservar() # Llama al método reservar() del Libro
            self.libros_adquiridos.append(libro)
            print(f"Cliente {self.nombre} ha reservado '{libro.titulo}'.")
            return True
        else: # Intento de compra inmediata
            if libro.vender(): # Llama al método vender() del Libro
                self.libros_adquiridos.append(libro)
                print(f"Cliente {self.nombre} ha comprado '{libro.titulo}'.")
                return True
            else:
                print(f"Cliente {self.nombre} NO pudo comprar '{libro.titulo}' (sin stock o reservado).")
                return False

    def devolver_libro_comprado(self, libro):
        """
        Permite a un cliente devolver un libro que había adquirido (comprado).
        Esto incrementa el stock de la librería.

        Args:
            libro (Libro): El objeto Libro que el cliente desea devolver.

        Returns:
            bool: True si la devolución fue exitosa, False si el libro no fue adquirido por este cliente.
        """
        if libro in self.libros_adquiridos:
            libro.comprar() # La librería "compra" de vuelta el libro al cliente (aumenta stock)
            self.libros_adquiridos.remove(libro)
            print(f"Cliente {self.nombre} ha devuelto '{libro.titulo}'.")
            return True
        else:
            print(f"Cliente {self.nombre}: '{libro.titulo}' no está en su lista de libros adquiridos.")
            return False

    def __str__(self):
        """
        Representación en cadena del objeto Cliente.
        """
        titulos_adquiridos = [libro.titulo for libro in self.libros_adquiridos]
        return f"Cliente: {self.nombre} {self.apellido} (ID: {self.id_cliente}), Libros Adquiridos: {titulos_adquiridos}"
