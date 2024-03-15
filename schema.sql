CREATE TABLE produto (
    codigo BIGINT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,

    PRIMARY KEY(codigo)
);

CREATE TABLE categoria (
    codigo BIGINT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,

    PRIMARY KEY (codigo)
);

CREATE TABLE categoria_produto (
    codigo_categoria BIGINT NOT NULL,
    codigo_produto BIGINT NOT NULL,

    PRIMARY KEY (codigo_categoria, codigo_produto),
    FOREIGN KEY (codigo_categoria) REFERENCES categoria (codigo),
    FOREIGN KEY (codigo_produto) REFERENCES produto (codigo)
);

CREATE TABLE fornecedor (
    cnpj VARCHAR(30) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),

    PRIMARY KEY (cnpj)
);

CREATE TABLE pedido (
    numero BIGINT NOT NULL AUTO_INCREMENT,
    data DATETIME NOT NULL,
    cnpj_fornecedor VARCHAR(20) NOT NULL,

    PRIMARY KEY (numero),
    FOREIGN KEY (cnpj_fornecedor) references fornecedor (cnpj)
);

CREATE TABLE item_pedido (
    numero_pedido BIGINT NOT NULL,
    codigo_produto BIGINT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,

    PRIMARY KEY (numero_pedido, codigo_produto),

    FOREIGN KEY (numero_pedido) references pedido (numero),
    FOREIGN KEY (codigo_produto) references produto (codigo)
);