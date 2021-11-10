CREATE TABLE producto (
    product_id INTEGER NOT NULL, 
	producto_nombre VARCHAR(100),
    producto_descripcion VARCHAR(100), 
	producto_valor INTEGER, 
	producto_cantidad INTEGER, 
	PRIMARY KEY (product_id)
)