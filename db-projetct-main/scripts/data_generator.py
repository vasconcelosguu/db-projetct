import importlib
import pandas as pd

def generate_mailing(carteira):
    try:
        data_module = importlib.import_module(f'scripts.carteiras.{carteira}')
        data = data_module.data
        
        print(f"Dados carregados para {carteira}: {data}")
        
        df = pd.DataFrame(data)
        
        html_data = df.to_html(index=False)

        print(f"Dados em HTML: {html_data}")
        
        return {"html_data": html_data}
    except ModuleNotFoundError:
        return {"error": f"Module {carteira} not found"}
    except Exception as e:
        return {"error": str(e)}

# Exemplo de chamada da função
if __name__ == "__main__":
    result = generate_mailing('vero')
    if 'html_data' in result:
        print(result['html_data'])
    else:
        print(result['error'])