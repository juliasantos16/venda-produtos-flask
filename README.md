### <small>Venda de Produtos API</small>

<small>API em Flask para gerenciamento, cadastro e busca de produtos.</small>

---

#### <small>Tecnologias</small>
<small>Python / Flask / SQLite / Redis / Pytest</small>

---

#### <small>Estrutura</small>
<small>

```text
.
├── src/
│   ├── data/
│   │   ├── product_creator.py
│   │   └── product_finder.py
│   ├── http_types/
│   │   ├── http_request.py
│   │   └── http_response.py
│   ├── main/
│   │   ├── composer/
│   │   │   ├── product_creator_composer.py
│   │   │   └── product_finder_composer.py
│   │   ├── routes/
│   │   │   └── products_routes.py
│   │   └── server/
│   │       └── server.py
│   └── models/
│       ├── redis/
│       │   ├── repository/
│       │   └── settings/
│       └── sqlite/
│           ├── repository/
│           └── settings/
├── tests/
│   └── products_repository_test.py
├── redis_raw.py
└── run.py
```

</small>

---

#### <small>Rotas da API</small>
<small>

* **`POST /products`** &mdash; Criação de um novo produto.
* **`GET /products/<product_name>`** &mdash; Busca de um produto pelo nome.

</small>

---

#### <small>Como Executar</small>
<small>

1. Configure e inicie as instâncias do SQLite e Redis.
2. Instale as dependências necessárias no ambiente virtual (`venv`).
3. Execute o servidor utilizando o comando:
   ```bash
   python run.py
   ```

</small>
