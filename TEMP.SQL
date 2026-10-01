

CREATE TABLE cliente (
    id_cliente INTEGER,
    nome TEXT(100) NOT NULL,
    cidade TEXT(100),
    telefone TEXT(20),
	PRIMARY KEY("id_cliente" AUTOINCREMENT)
);


-- =========================================================
-- TABELA PRODUTO
-- =========================================================

CREATE TABLE produto (
    id_produto INTEGER,
    nome TEXT(100) NOT NULL,
    categoria TEXT(50),
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL,
    PRIMARY KEY ("id_produto" AUTOINCREMENT)
);


-- =========================================================
-- TABELA FORNECEDOR
-- =========================================================

CREATE TABLE fornecedor (
    id_fornecedor INTEGER,
    nome TEXT(100) NOT NULL,
    cidade TEXT(100),
    PRIMARY KEY("id_fornecedor" AUTOINCREMENT)
);


-- =========================================================
-- TABELA VENDA
-- =========================================================

CREATE TABLE venda (
    id_venda INTEGER,
    id_cliente INT NOT NULL,
    data_venda DATE NOT NULL,
    PRIMARY KEY ("id_venda" AUTOINCREMENT)

    FOREIGN KEY (id_cliente)
        REFERENCES cliente(id_cliente)
);


-- =========================================================
-- TABELA ITEM_VENDA
-- =========================================================

CREATE TABLE item_venda (
    id_venda INTEGER,
    id_produto INTEGER,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,

    PRIMARY KEY ("id_venda", "id_produto"),

    FOREIGN KEY (id_venda)
        REFERENCES venda(id_venda),

    FOREIGN KEY (id_produto)
        REFERENCES produto(id_produto)
);


-- =========================================================
-- TABELA ORDEM DE SERVIÇO
-- =========================================================

CREATE TABLE ordem_servico (
    id_ordem INTEGER,
    id_cliente INT NOT NULL,
    descricao TEXT(200),
    data_abertura DATE,
    status_os TEXT(20),
    PRIMARY KEY ("id_ordem" AUTOINCREMENT)
    FOREIGN KEY (id_cliente)
        REFERENCES cliente(id_cliente)
);


-- =========================================================
-- TABELA ENTREGA DE FORNECEDOR
-- =========================================================

CREATE TABLE entrega_fornecedor (
    id_entrega INTEGER,
    id_fornecedor INT NOT NULL,
    id_ordem INT NOT NULL,
    data_prevista DATE,
    status_entrega TEXT(20),
    PRIMARY KEY ("id_entrega" AUTOINCREMENT)

    FOREIGN KEY (id_fornecedor)
        REFERENCES fornecedor(id_fornecedor),

    FOREIGN KEY (id_ordem)
        REFERENCES ordem_servico(id_ordem)
);


-- =========================================================
-- DADOS DOS CLIENTES
-- =========================================================

INSERT INTO cliente (nome, cidade, telefone) VALUES
('Ana Souza', 'Feira de Santana', '75999990001'),
('Bruno Lima', 'Salvador', '71999990002'),
('Carla Santos', 'Feira de Santana', '75999990003'),
('Diego Alves', 'Santo Antônio de Jesus', '75999990004'),
('Eduardo Rocha', 'Feira de Santana', '75999990005'),
('Fernanda Costa', 'Salvador', '71999990006');


-- =========================================================
-- DADOS DOS PRODUTOS
-- =========================================================

INSERT INTO produto
(nome, categoria, preco, estoque)
VALUES
('Rolamento', 'Mecânica', 50.00, 30),
('Correia Dentada', 'Mecânica', 80.00, 20),
('Parafuso Industrial', 'Fixação', 5.00, 200),
('Filtro de Óleo', 'Filtros', 40.00, 15),
('Óleo Lubrificante', 'Lubrificantes', 35.00, 50),
('Sensor de Temperatura', 'Eletrônica', 120.00, 10),
('Junta de Vedação', 'Vedação', 25.00, 40);


-- =========================================================
-- DADOS DOS FORNECEDORES
-- =========================================================

INSERT INTO fornecedor (nome, cidade) VALUES
('Metalúrgica Alfa', 'Feira de Santana'),
('Autopeças Bahia', 'Salvador'),
('Industrial Nordeste', 'Camaçari'),
('Fornecedor Delta', 'Alagoinhas');


-- =========================================================
-- DADOS DAS VENDAS
-- =========================================================

INSERT INTO venda (id_cliente, data_venda) VALUES
(1, '2026-08-01'),
(1, '2026-08-10'),
(2, '2026-08-12'),
(3, '2026-08-15'),
(2, '2026-08-20'),
(4, '2026-08-22'),
(1, '2026-09-01'),
(5, '2026-09-05');


-- =========================================================
-- ITENS DAS VENDAS
-- =========================================================

INSERT INTO item_venda
(id_venda, id_produto, quantidade, preco_unitario)
VALUES

-- Venda 1 - Ana
(1, 1, 2, 50.00),
(1, 3, 10, 5.00),
(1, 5, 2, 35.00),

-- Venda 2 - Ana
(2, 2, 1, 80.00),
(2, 4, 1, 40.00),
(2, 5, 2, 35.00),

-- Venda 3 - Bruno
(3, 1, 1, 50.00),
(3, 4, 2, 40.00),
(3, 5, 1, 35.00),

-- Venda 4 - Carla
(4, 3, 20, 5.00),
(4, 5, 1, 35.00),

-- Venda 5 - Bruno
(5, 2, 2, 80.00),
(5, 6, 1, 120.00),

-- Venda 6 - Diego
(6, 1, 4, 50.00),
(6, 3, 5, 5.00),

-- Venda 7 - Ana
(7, 4, 3, 40.00),
(7, 5, 3, 35.00),

-- Venda 8 - Eduardo
(8, 6, 1, 120.00),
(8, 7, 2, 25.00);


-- =========================================================
-- ORDENS DE SERVIÇO
-- =========================================================

INSERT INTO ordem_servico
(id_cliente, descricao, data_abertura, status_os)
VALUES
(1, 'Troca de correia dentada', '2026-09-01', 'ABERTA'),
(2, 'Manutenção do sistema de lubrificação', '2026-09-02', 'ABERTA'),
(3, 'Substituição de sensor', '2026-09-03', 'FINALIZADA'),
(4, 'Troca de rolamentos', '2026-09-05', 'ABERTA'),
(5, 'Revisão preventiva', '2026-09-06', 'FINALIZADA');


-- =========================================================
-- ENTREGAS DOS FORNECEDORES
-- =========================================================

INSERT INTO entrega_fornecedor
(id_fornecedor, id_ordem, data_prevista, status_entrega)
VALUES
(1, 1, '2026-09-15', 'PENDENTE'),
(2, 1, '2026-09-14', 'ENTREGUE'),
(2, 2, '2026-09-18', 'PENDENTE'),
(3, 3, '2026-09-10', 'PENDENTE'),
(1, 4, '2026-09-20', 'PENDENTE'),
(4, 5, '2026-09-12', 'ENTREGUE');