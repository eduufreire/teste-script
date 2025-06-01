import papermill as pm
import concurrent.futures

def executar_notebook():
    pm.execute_notebook(
        '../../opt/jupyter/notebook/limpeza-camera-visao-comp.ipynb',
        '../../opt/jupyter/notebook/limpeza-camera-visao-comp-exec.ipynb',
        parameters=dict(nome_arquivo="visao_computacional.csv")
    )

timeout_global = 300

with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    futuro = executor.submit(executar_notebook)
    try:
        resultado = futuro.result(timeout=timeout_global)
        print("Notebook executado com sucesso!")
    except concurrent.futures.TimeoutError:
        print('Timeout global de {timeout_global} segundos excedido! Abortando...')
