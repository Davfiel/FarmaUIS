CREATE DATABASE farmaUIS_DB;
USE farmaUIS_DB;

CREATE TABLE Usuario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Administrador (
    id INT PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES Usuario(id) ON DELETE CASCADE
);

CREATE TABLE Empleado (
    id INT PRIMARY KEY,
    cargo VARCHAR(50) NOT NULL,
    FOREIGN KEY (id) REFERENCES Usuario(id) ON DELETE CASCADE
);

CREATE TABLE Reporte (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    datos TEXT NOT NULL,
    usuarioId INT NOT NULL,
    administradorId INT,
    FOREIGN KEY (usuarioId) REFERENCES Usuario(id),
    FOREIGN KEY (administradorId) REFERENCES Administrador(id)
);

CREATE TABLE Categoria (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);

CREATE TABLE Producto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    categoriaId INT,
    FOREIGN KEY (categoriaId) REFERENCES Categoria(id)
);
CREATE TABLE Medicamento (
    id INT PRIMARY KEY,
    principio_activo VARCHAR(100) NOT NULL,
    dosis VARCHAR(50) NOT NULL,
    fecha_vencimiento DATE NOT NULL,
    venta_libre BOOLEAN DEFAULT TRUE,
    laboratorio VARCHAR(100),
    lote VARCHAR(50),
    FOREIGN KEY (id) REFERENCES Producto(id) ON DELETE CASCADE
);
CREATE TABLE Cliente (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100),
    telefono VARCHAR(20),
    direccion TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Venta (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(12,2) NOT NULL,
    empleado_id INT NOT NULL,
    cliente_id INT,
    estado ENUM('pendiente', 'completada', 'cancelada') DEFAULT 'pendiente',
    metodo_pago ENUM('efectivo', 'tarjeta', 'transferencia') NOT NULL,
    FOREIGN KEY (empleado_id) REFERENCES Empleado(id),
    FOREIGN KEY (cliente_id) REFERENCES Cliente(id)
);
CREATE TABLE DetalleVenta (
    id INT PRIMARY KEY AUTO_INCREMENT,
    venta_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(12,2) GENERATED ALWAYS AS (cantidad * precio_unitario) STORED,
    FOREIGN KEY (venta_id) REFERENCES Venta(id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES Producto(id)
);
CREATE TABLE Factura (
    id INT PRIMARY KEY AUTO_INCREMENT,
    venta_id INT NOT NULL,
    numero_factura VARCHAR(20) UNIQUE NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    subtotal DECIMAL(12,2) NOT NULL,
    impuestos DECIMAL(12,2) NOT NULL,
    total DECIMAL(12,2) NOT NULL,
    datos_fiscales TEXT,
    FOREIGN KEY (venta_id) REFERENCES Venta(id)
);
CREATE TABLE Proveedor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100),
    telefono VARCHAR(20),
    direccion TEXT,
    ruc VARCHAR(20),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Pedido (
    id INT PRIMARY KEY AUTO_INCREMENT,
    proveedor_id INT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    estado ENUM('pendiente', 'enviado', 'recibido', 'cancelado') DEFAULT 'pendiente',
    total DECIMAL(12,2),
    fecha_entrega_estimada DATE,
    empleado_id INT NOT NULL,
    FOREIGN KEY (proveedor_id) REFERENCES Proveedor(id),
    FOREIGN KEY (empleado_id) REFERENCES Empleado(id)
);
CREATE TABLE DetallePedido (
    id INT PRIMARY KEY AUTO_INCREMENT,
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES Pedido(id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES Producto(id)
);
