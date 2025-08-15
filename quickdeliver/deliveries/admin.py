from django.contrib import admin
from .models import Cliente, Entregador, Pedido, Lojista, Produto, AcompanhePedido, Avaliacao

admin.site.register(Cliente)
admin.site.register(Entregador)
admin.site.register(Pedido)
admin.site.register(Lojista)
admin.site.register(Produto)
admin.site.register(AcompanhePedido)
admin.site.register(Avaliacao)
# Register your models here.
