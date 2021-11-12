-- RUN IT IN DATABASE
-- // CREATING TABLES //

CREATE TABLE cliente (
    customer_id INTEGER NOT NULL,
	cliente_nombre VARCHAR(100),
    cliente_direccion VARCHAR(100),
	cliente_telefono DOUBLE,
	PRIMARY KEY (customer_id)
);

CREATE TABLE producto (
    product_id INTEGER NOT NULL,
	producto_nombre VARCHAR(100),
    producto_descripcion VARCHAR(100),
	producto_valor INTEGER,
	producto_cantidad INTEGER,
	PRIMARY KEY (product_id)
);

-- // INSERTING DATA //

INSERT INTO cliente (customer_id, cliente_nombre, cliente_direccion, cliente_telefono)
VALUES (1, 'Antonio Perez', 'Calle 40 8 30', 3154891100),
(2, 'Jose Villada', 'Call 20 39 20', 3154515200),
(3, 'Matby Yoslin', 'Cr 7 24 86', 3105500000);

INSERT INTO producto (product_id, producto_nombre, producto_descripcion, producto_valor, producto_cantidad)
VALUES (1, 'Arroz', 'Descripcion arroz', 3500, 10),
(2, 'Aceite', 'Descripcion aceite', 4500, 20),
(3, 'Leche', 'Descripcion leche', 5500, 30);