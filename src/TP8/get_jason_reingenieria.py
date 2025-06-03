# -----------------------------------------------------------
# Copyright UADER FCyT-IS2©2024 - Todos los derechos reservados
# Este programa lee una clave desde la línea de comandos,
# busca su valor en un archivo JSON y lo imprime.
# Usa una estrategia de "Branching by Abstraction" para permitir
# alternar entre una versión simple y una refactorizada con Singleton.
# -----------------------------------------------------------

"""
Este módulo obtiene claves desde un archivo JSON usando una estructura con el patrón Singleton.
Copyright UADER FCyT-IS2©2024 todos los derechos reservados.
"""

import json
import sys
import os

VERSION = "1.2"

class SelectorDeCuenta:
    """
    Singleton que carga el JSON y mantiene estado de tokens.
    """
    _instance = None

    def __new__(cls, jsonfile='sitedata.json'):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_json(jsonfile)
        return cls._instance

    def _load_json(self, jsonfile):
        if not os.path.exists(jsonfile):
            print(f"❌ Error: El archivo '{jsonfile}' no existe.")
            sys.exit(1)
        try:
            with open(jsonfile, 'r', encoding='utf-8') as f:
                self._data = json.load(f)
        except json.JSONDecodeError:
            print(f"❌ Error: El archivo '{jsonfile}' no tiene formato JSON válido.")
            sys.exit(1)

    def obtener_saldo(self, token):
        return self._data[token]["saldo"]

    def obtener_clave(self, token):
        return self._data[token]["clave"]

    def descontar_saldo(self, token, monto):
        self._data[token]["saldo"] -= monto
        return True

# Abstract Handler
class AbstractHandler:
    def __init__(self, nxt):
        self._nxt = nxt

    def handle(self, request):
        if not self.process_request(request) and self._nxt:
            self._nxt.handle(request)

    def process_request(self, request):
        raise NotImplementedError

# Token Handler
class TokenHandler(AbstractHandler):
    def __init__(self, token_name, selector, nxt=None):
        super().__init__(nxt)
        self.token_name = token_name
        self.selector = selector
        self.pagos_realizados = []

    def process_request(self, request):
        numero_pedido, monto = request
        saldo = self.selector.obtener_saldo(self.token_name)
        if saldo >= monto:
            clave = self.selector.obtener_clave(self.token_name)
            self.selector.descontar_saldo(self.token_name, monto)
            self.pagos_realizados.append({
                "numero_pedido": numero_pedido,
                "token": self.token_name,
                "monto": monto
            })
            print(
                f"✅ Pedido # {numero_pedido} procesado con token '{self.token_name}'. "
                f"Clave: {clave}. "
                f"Saldo restante: {self.selector.obtener_saldo(self.token_name)}"
            )
            return True
        return False

    def listado_pagos(self):
        for pago in self.pagos_realizados:
            yield pago

# Default Handler
class DefaultHandler(AbstractHandler):
    def __init__(self, nxt=None):
        super().__init__(nxt)
        self.pagos_realizados = []

    def process_request(self, request):
        numero_pedido, monto = request
        print(f"⚠️ Pedido # {numero_pedido} no pudo ser procesado: saldo insuficiente.")
        self.pagos_realizados.append({
            "numero_pedido": numero_pedido,
            "token": None,
            "monto": monto
        })
        return True

    def listado_pagos(self):
        for pago in self.pagos_realizados:
            yield pago

# Iterador para recorrer pagos
class PagoIterator:
    def __init__(self, pagos):
        self._pagos = pagos
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._pagos):
            pago = self._pagos[self._index]
            self._index += 1
            return pago
        raise StopIteration

# Clase User que arma la cadena
class User:
    def __init__(self, selector):
        self.selector = selector
        self.contador_pedidos = 1
        # Armo la cadena con los tokens conocidos
        self.handler = TokenHandler(
            "token1", selector,
            TokenHandler(
                "token2", selector,
                DefaultHandler()
            )
        )

    def agent(self, request):
        if isinstance(request, (int, float)):
            request = (self.contador_pedidos, float(request))
            self.contador_pedidos += 1
        self.handler.handle(request)

    def listado_general(self):
        pagos = []
        actual = self.handler
        while actual:
            if hasattr(actual, "listado_pagos"):
                pagos.extend(list(actual.listado_pagos()))
            actual = actual._nxt
        return pagos

def main():
    if len(sys.argv) < 2:
        print("❌ Error: Debe ingresar un monto como argumento.")
        sys.exit(1)

    argumento = sys.argv[1]

    if argumento == "-v":
        print(f"get_jason_reingenieria.py - versión {VERSION}")
        sys.exit(0)

    if len(sys.argv) > 2:
        print(f"ℹ️ Advertencia: Se ingresaron argumentos adicionales."
              f"Solo se usará el primero: {argumento}"
        )

    selector = SelectorDeCuenta()
    user = User(selector)

    if argumento == "-test":
    # Generar 5 pedidos de $500
        pedidos = [(i, 500) for i in range(1, 6)]
        for pedido in pedidos:
            user.agent(pedido)

        # Mostrar listado general usando iterador
        print("\n📋 Listado de pagos realizados (orden cronológico):")
        pagos = user.listado_general()
        for pago in PagoIterator(pagos):
            token = pago["token"] if pago["token"] else "Ninguno"
            print(f"- Pedido #{pago['numero_pedido']}: Token = {token}, Monto = ${pago['monto']}")

    try:
        monto = float(argumento)
        if monto < 0:
            print("❌ Error: El monto no puede ser negativo.")
            sys.exit(1)
    except ValueError:
        print("❌ Error: El argumento debe ser un número válido.")
        sys.exit(1)

    user.agent(monto)

if __name__ == "__main__":
    main()
