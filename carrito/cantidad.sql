CREATE TABLE cantidad(
	quantity INTEGER NOT NULL,
    product_id_fk INTEGER NOT NULL,
    carrito_id_fk INTEGER NOT NULL,
	PRIMARY KEY (product_id_fk,carrito_id_fk)
    --FOREIGN KEY (customer_id_fk) REFERENCES cliente
);
