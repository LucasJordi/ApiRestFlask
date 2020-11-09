<h1> Api Rest Feita em Flask</h1>



<h2>Descrição </h2>


<p> O objetivo deste código foi criar uma API REST para simular uma loja virutal. Contendo cadastro de clientes, produtos e pedidos.</p>


<h2>Organização de arquivos</h2>


<p> Para a confecção do projeto foi adotado o conceito de mcv(model, controller e view) para a organização das pastas e dos arquivos.O arquivo "run.py" é o qe inicia a aplicação.Dentro da pasta "app"  dentro de "controllers" foi onde os arquivos de rotas e tabela(tables) foram disponibilizados </p>





<h2>Utilização</h2>

<p>Antes de iniciar a aplicação lembre-se de puxar as dependências do requirements.txt com o pip. Para dar inicio a aplicação basta apenas executar o arquivo "run.py". Após executar o arquivo "run.py" ao acessar o locashost http://127.0.0.1:4000/  é preciso visualizar a seguinte mensagem:</p>



<pre><code> 
  http://127.0.0.1:4000/


{
  "message": "Everything ok!"
}
</code></pre>



<p>Após a conclusão do teste vamos as funcionalidades da api</p>

<h3>Clientes</h3>

<p>Na pasta "tables" em "controllers" estão aramazenados alguns arquivos com dados pré-armazenados para teste. As rotas para a interação com clientes estão todas armazenadas no arquivo "clientsroutes.py". Para ter a visualização dos cadastros disponíveis vá até a rota "/clients"</p>



<pre> <code>
  http://127.0.0.1:4000/clients
  
  {
  "Clients": [
    {
      "email": "jse@gmmail.com", 
      "id": 1, 
      "name": "Josu\u00e9 Almeida", 
      "number": "71222222", 
      "password": "123"
    }, 
    {
      "email": "amandapache@gmmail.com", 
      "id": 2, 
      "name": "Amanda Pacheco", 
      "number": "71222342", 
      "password": "123"
    }, 
    {
      "email": "luans@gmmail.com", 
      "id": 3, 
      "name": "Luan Serra", 
      "password": "123", 
      "telefone": "71222222"
    }, 
    {
      "email": "luana@gmmail.com", 
      "id": 4, 
      "name": "Luana Souza", 
      "number": "71228722", 
      "password": "123"
    }, 
    {
      "email": "ric.ant@gmmail.com", 
      "id": 5, 
      "name": "Ricardo Ant\u00f4nio", 
      "number": "71672222", 
      "password": "123"
    }
  ], 
  "message": "Clients List"
}
</code></pre>

<p>Para ter acesso a um cliente em específico basta ir para a rota /clients/id_do_cliente</p>


<code><pre>
  http://127.0.0.1:4000/clients/2
  [
  {
    "email": "amandapache@gmmail.com", 
    "id": 2, 
    "name": "Amanda Pacheco", 
    "number": "71222342", 
    "password": "123"
  }
]
</code></pre>

<h4>Adicionar,atualizar dados e deletar clientes na lista</h4>

<p>Para adicionar algum cliente a lista basta utilizar o método 'POST' na rota "/clients". Caso deseje modificar algum dado de cliente na lista utilize a rota "/clients/id_cliente" com o método 'PUT'. Para deletar o cliente da lista basta utilizar a mesma rota /clients/id_cliente", mas com o método 'DELETE'. </p>




<h3>Produtos</h3>

<p>A forma como o código interage com os produtos segue a mesma lógica da manipulação de clientes. A única mudança são as rotas:</p>

<code><pre>
  <p>#Acessando a lista de produtos</p>
  
    http://127.0.0.1:4000/products
    
    
    
    {
  "message": "Products List", 
  "products": [
    {
      "brand": "Samsung", 
      "id": 1, 
      "name": "monitor", 
      "price": 1000, 
      "quantity": 10
    }, 
    {
      "brand": "Dell", 
      "id": 2, 
      "name": "laptop", 
      "price": 5000, 
      "quantity": 22
    }, 
    {
      "brand": "Razer", 
      "id": 3, 
      "name": "mouse", 
      "price": 120, 
      "quantity": 30
    }, 
    {
      "brand": "Razer", 
      "id": 4, 
      "name": "mouse", 
      "price": 120, 
      "quantity": 30
    }, 
    {
      "brand": "Razer", 
      "id": 5, 
      "name": "keyboard", 
      "price": 200, 
      "quantity": 2
    }
  ]
}
  
</code></pre>

<h4>Acessar um produto específico</h4>
<code><pre>

  http://127.0.0.1:4000/products/1
  
  
[
  {
    "brand": "Samsung", 
    "id": 1, 
    "name": "monitor", 
    "price": 1000, 
    "quantity": 10
  }
]  



</code></pre>

<p>Da mesma forma como é feito em clientes é possível adicionar,atualizar ou deletar os dados manipulando as rotas com seus respectivos métodos 'GET' ,'PUT', 'DELETE'.</p>

<h3>Ordens de compra</h3>

<p>Para a manipulação das ordens de compra foi feito um interação junto com os dados de produtos cadastrados.Para acessar a lista de ordens basta ir para a rota "/orders/all". Como nenhuma ordem foi feita a lista retorna vazia.</p>



<code><pre>

  http://127.0.0.1:4000/orders/all
  
  []
</code></pre>

<p>Para começarmos a inserir produtos a ordem é preciso acessar a rota "/orders/createorder/id_do_produto_escolhido". Junto com a lista de produtos é possível ver o total da compra. Vamos fazer um teste de ordem com os produtos de id 1, 2 e 3:</p>


<code><pre>

  http://127.0.0.1:4000/orders/createorder/1
  http://127.0.0.1:4000/orders/createorder/2
  http://127.0.0.1:4000/orders/createorder/3
  
  
{
  "Order number": 1, 
  "Products": [
    {
      "id": 1, 
      "name": "monitor", 
      "price": 1000, 
      "product_id": 1
    }, 
    {
      "id": 2, 
      "name": "laptop", 
      "price": 5000, 
      "product_id": 2
    }, 
    {
      "id": 3, 
      "name": "mouse", 
      "price": 120, 
      "product_id": 3
    }
  ], 
  "Total price": 6120.0
}  

  
</code></pre>



<p>Para finalizar a compra basta acessar a rota "/orders/createorder/submit". Se recebeu a mensagem abaixo significa que está tudo ok:</p>

<code><pre> 
  http://127.0.0.1:4000/orders/createorder/submit
  
  Submit!

  
</code></pre>

<p>Agora entrando na rota "/orders/all" é possível ver a nossa ordem cadastrada:</p>


<code><pre>

http://127.0.0.1:4000/orders/all

[
  [
    {
      "id": 1, 
      "name": "monitor", 
      "price": 1000, 
      "product_id": 1
    }, 
    {
      "id": 2, 
      "name": "laptop", 
      "price": 5000, 
      "product_id": 2
    }, 
    {
      "id": 3, 
      "name": "mouse", 
      "price": 120, 
      "product_id": 3
    }
  ]
]



</code></pre>




