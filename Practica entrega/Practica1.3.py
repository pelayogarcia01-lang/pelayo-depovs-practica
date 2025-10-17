class Producto:
    contador_id = 1

    def __init__(self, nombre, precio, stock):
        self.id = Producto.contador_id
        Producto.contador_id += 1
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def hay_stock(self, cantidad):
        return self.stock >= cantidad

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}"


class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        super().__init__(nombre, precio, stock)
        self.garantia = garantia

    def __str__(self):
        return f"Electrónico: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Garantía: {self.garantia} meses"


class ProductoRopa(Producto):
    def __init__(self, nombre, precio, stock, talla, color):
        super().__init__(nombre, precio, stock)
        self.talla = talla
        self.color = color

    def __str__(self):
        return f"Ropa: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Talla: {self.talla}, Color: {self.color}"


class Usuario:
    contador_id = 1

    def __init__(self, nombre, correo):
        self.id = Usuario.contador_id
        Usuario.contador_id += 1
        self.nombre = nombre
        self.correo = correo

    def is_admin(self):
        return False

    def __str__(self):
        return f"Usuario: {self.nombre}, Correo: {self.correo}"


class Cliente(Usuario):
    def __init__(self, nombre, correo, direccion):
        super().__init__(nombre, correo)
        self.direccion = direccion

    def __str__(self):
        return f"Cliente: {self.nombre}, Dirección: {self.direccion}"


class Administrador(Usuario):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)

    def is_admin(self):
        return True

    def __str__(self):
        return f"Administrador: {self.nombre}, Correo: {self.correo}"


class Pedido:
    contador_id = 1

    def __init__(self, cliente, productos):
        self.id = Pedido.contador_id
        Pedido.contador_id += 1
        self.cliente = cliente
        self.productos = productos  

    def calcular_total(self):
        return sum(prod.precio * cant for prod, cant in self.productos.items())

    def __str__(self):
        productos_str = ", ".join([f"{prod.nombre} x{cant}" for prod, cant in self.productos.items()])
        return f"Pedido: {self.id}, Cliente: {self.cliente.nombre}, Total: {self.calcular_total():.2f}, Productos: {productos_str}"


class TiendaService:
    def __init__(self):
        self.usuarios = {}
        self.productos = {}
        self.pedidos = []

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.id] = usuario

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def listar_productos(self):
        return list(self.productos.values())

    def realizar_pedido(self, cliente_id, productos_cant):
        cliente = self.usuarios.get(cliente_id)
        if not cliente or not isinstance(cliente, Cliente):
            print("Cliente no válido")
            return None

        seleccionados = {}
        for prod_id, cant in productos_cant.items():
            producto = self.productos.get(prod_id)
            if not producto or not producto.hay_stock(cant):
                print(f"Producto {prod_id} no disponible")
                return None
            seleccionados[producto] = cant

        for prod, cant in seleccionados.items():
            prod.actualizar_stock(-cant)

        pedido = Pedido(cliente, seleccionados)
        self.pedidos.append(pedido)
        return pedido

    def listar_pedidos_por_usuario(self, cliente_id):
        return [p for p in self.pedidos if p.cliente.id == cliente_id]


if __name__ == "__main__":
    tienda = TiendaService()


    cliente1 = Cliente("Ana", "ana@mail.com", "Calle A 123")
    cliente2 = Cliente("Luis", "luis@mail.com", "Calle B 456")
    admin = Administrador("Admin", "admin@mail.com")

    tienda.registrar_usuario(cliente1)
    tienda.registrar_usuario(cliente2)
    tienda.registrar_usuario(admin)

   
    p1 = ProductoElectronico("Móvil", 300, 10, 24)
    p2 = ProductoRopa("Camiseta", 20, 50, "M", "Rojo")
    p3 = Producto("Libro", 15, 100)

    tienda.agregar_producto(p1)
    tienda.agregar_producto(p2)
    tienda.agregar_producto(p3)

  
    for prod in tienda.listar_productos():
        print(prod)

  
    pedido = tienda.realizar_pedido(cliente1.id, {p1.id: 1, p2.id: 2})
    if pedido:
        print(pedido)


    for ped in tienda.listar_pedidos_por_usuario(cliente1.id):
        print(ped)