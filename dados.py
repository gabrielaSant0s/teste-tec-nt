# informações country_long=2, name=3, capacity_mw=5, latitude=6 ,longitude=7, primary_fuel=8
# nome do arquivo -> pais_nome da usina_primary_fuel -> minuscula
import json

class Usina():
    def __init__(self, country_long, name, capacity_mw, latitude, longitude, primary_fuel) -> None:
        self.country_long = country_long
        self.name = name
        self.capacity_mw = capacity_mw
        self.latitude = latitude
        self.longitude = longitude
        self.primary_fuel = primary_fuel

    def __str__(self) -> str:
        return f'{self.name} ({self.country_long})'
    
    def salvar(self):
        dados_json = {
            "country_long" : self.country_long,
            "name":self.name,
            "capacity_mw":self.capacity_mw,
            "latitude":self.latitude,
            "longitude":self.longitude,
            "primary_fuel":self.primary_fuel
        }

        nome_do_arquivo = f'{self.country_long} {self.name} {self.primary_fuel}'.replace(" ","_").lower()

        with open(f'usinas/{nome_do_arquivo}.json', "w") as usinas:
            json.dump(dados_json, usinas)


with open("global_power_plant_database.csv", "r") as dados:
    linhas = dados.readlines()


lista_instancias = list()
for linha in linhas[1:]:
    split_linha = linha.split(",")
    
    classe_inst = Usina(
        country_long=split_linha[1],
        name=split_linha[2],
        capacity_mw=split_linha[4],
        latitude=split_linha[5],
        longitude=split_linha[6],
        primary_fuel=split_linha[7]
    )
    lista_instancias.append(classe_inst)
    
for instancia in lista_instancias:
    instancia.salvar()