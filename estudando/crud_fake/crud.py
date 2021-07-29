"""
inserindo dados com pandas
C - CREATE
R - READ
U - UPDATE
D - DELETE
"""
import pandas as pd

BASE_PATH = 'base.csv'


# CREATE
def post(dados: dict):
    df_antigo = pd.DataFrame(get())
    df_novo = pd.DataFrame(dados, index=[0])
    df = df_antigo.append(df_novo)

    df.to_csv(BASE_PATH, sep=',', index=False)


# READ
def get(id: int=None):
    try:
        df = pd.read_csv(BASE_PATH, sep=',')
        lista_dados = df.to_dict('records')

        if not id:
            return df.to_dict('records')  # [{"id":1 ...}, {"id": 2 ...}, ...]

        for dado in lista_dados:
            if dado['id'] == id:
                return [dado]
    except:
        return []


# UPDATE
def put(id: int, dados_alterar):
    lista_antiga = get()

    lista_dados_novos = []
    for dado in lista_antiga:
        if dado["id"] == id:
            dado = dados_alterar
        lista_dados_novos.append(dado)

    df = pd.DataFrame(lista_dados_novos)
    df.to_csv(BASE_PATH, sep=',', index=False)

    return


# DELETE
def delete(id: int):
    lista_antiga = get()

    lista_dados_novos = []
    for dado in lista_antiga:
        if not dado["id"] == id:
            lista_dados_novos.append(dado)

    df = pd.DataFrame(lista_dados_novos)
    df.to_csv(BASE_PATH, sep=',', index=False)

# DELETE ALL
def clear():
    df = pd.DataFrame([])
    df.to_csv(BASE_PATH)



if __name__ == '__main__':
    # dados_1 = {"id": 1, "nome": "eder", "profissao": "desenvoldedor"}
    # dados_2 = {"id": 2, "nome": "rivelton", "profissao": "desenvoldedor"}
    # dados_3 = {"id": 3, "nome": "lucas", "profissao": "desenvoldedor"}
    #
    # dados = [dados_1, dados_2, dados_3]
    # for dado in dados:
    #     post(dado)

    print("lista_antiga", get())
    post({"id": 1, "nome": "EDER", "profissao": "desenvoldedor", "endereco": "caruaru"})
    print("lista_nova", get())

