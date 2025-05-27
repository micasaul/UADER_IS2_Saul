import json
import sys
import os

class JSONLoaderSingleton:
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
            with open(jsonfile, 'r') as myfile:
                self._data = json.load(myfile)
        except json.JSONDecodeError:
            print(f"❌ Error: El archivo '{jsonfile}' no tiene formato JSON válido.")
            sys.exit(1)

    def get_value(self, key):
        if key not in self._data:
            print(f"⚠️ La clave '{key}' no existe en el archivo.")
            sys.exit(1)
        return self._data[key]

def main():
    if len(sys.argv) >= 2:
        jsonkey = sys.argv[1]
        if len(sys.argv) > 2:
            print("ℹ️ Advertencia: Se proporcionaron argumentos adicionales. Solo se usará el primero:", jsonkey)
    else:
        jsonkey = 'token1'

    loader = JSONLoaderSingleton()
    valor = loader.get_value(jsonkey)
    print(valor)

if __name__ == "__main__":
    main()
