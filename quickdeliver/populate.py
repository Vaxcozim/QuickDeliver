from deliveries.models import Cliente, Entregador, Pedido

# Cria um cliente
cliente = Cliente.objects.create(
    nome="Maria Silva",
    telefone="11999999999",
    email="maria@email.com",
    endereco="Rua das Flores, 123"
)

# Cria um entregador
entregador = Entregador.objects.create(
    nome="João Motoboy",
    veiculo="Moto",
    disponibilidade=True,
    localizacao_atual="-23.5505, -46.6333"  # Exemplo: coordenadas de São Paulo
)

# Cria um pedido
pedido = Pedido.objects.create(
    cliente=cliente,
    entregador=entregador,
    endereco_entrega="Avenida Paulista, 1000",
    status="P",
    prioridade="N",
    produtos=[{"nome": "Remédio Y", "quantidade": 1}],
    valor_total=50.00
)

print("✅ Dados criados com sucesso!")