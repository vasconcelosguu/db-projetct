from datetime import datetime

def generate_mailing(carteira, start_date, end_date):
    data = {
        'Email': [
            'lucas@example.com', 'fernanda@example.com', 'rafael@example.com',
            'maria@example.com', 'joao@example.com', 'ana@example.com',
            'pedro@example.com', 'carla@example.com', 'marcos@example.com',
            'julia@example.com'
        ],
        'Carteira': [carteira] * 10,
        'Dias Ligados por DU': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Ligações Atendidas': [5, 7, 6, 8, 9, 10, 11, 12, 13, 14],
        'Telefones': [
            '789456123', '123789456', '456789123', '789123456', '123456789',
            '456123789', '789456789', '123123123', '456456456', '789789789'
        ],
        'Hora de Geração': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')] * 10,
        'Endereço': [
            'Rua A, 123', 'Rua B, 456', 'Rua C, 789', 'Rua D, 101', 'Rua E, 112',
            'Rua F, 131', 'Rua G, 415', 'Rua H, 161', 'Rua I, 718', 'Rua J, 192'
        ],
        'Cidade': [
            'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Curitiba',
            'Salvador', 'Fortaleza', 'Brasília', 'Manaus', 'Recife'
        ],
        'Estado': [
            'SP', 'RJ', 'MG', 'RS', 'PR', 'BA', 'CE', 'DF', 'AM', 'PE'
        ]
    }
    return data

