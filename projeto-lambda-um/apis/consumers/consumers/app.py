from chalice import Chalice

app = Chalice(app_name='consumers')

users = {
    "users": [
        {"name": "usuário1", "phone": "11123456789"},
        {"name": "usuário2", "phone": "22123456789"},
        {"name": "usuário3", "phone": "33123456789"},
    ]    
}

companies = {
    "comapnies": [
        {"name": "empresa1", "telefone": "11123456789"},
        {"name": "empresa2", "telefone": "22123456789"},
        {"name": "empresa3", "telefone": "33123456789"},
    ]
}


@app.route('/consumers/person', methods = ['POST'])
def create_user():
    # Acessar o que o usuário está passando 
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} criado com sucesso!"    
        
        }
    return response

@app.route('/consumers/person', methods = ['PUT'])
def update_user():
    # Acessar o que o usuário está passando 
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} criado com sucesso!"    
        
        }
    return response

@app.route('/consumers/person', methods = ['DELETE'])
def delete_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} deletado com sucesso!"    
        
        }
    return response

@app.route('/consumers/person', methods = ['GET'])
def get_persons():
    response = {
        "statusCode": 200,
        "body": users    
        
        }
    return response

@app.route('/consumers/person/{id}', methods = ['GET'])
def get_persons(id):
    response = {
        "statusCode": 200,
        # Chumbado de exemplo
        "body": {id: {"name": "usuario1", "telefone": "11123456789"}}   
        }
    return response


# ---------------------------------------------------------------------


@app.route('/consumers/company', methods = ['POST'])
def create_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} criado com sucesso!"    
        
        }
    return response

@app.route('/consumers/company', methods = ['PUT'])
def update_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} criado com sucesso!"    
        
        }
    return response

@app.route('/consumers/company', methods = ['DELETE'])
def delete_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} deletado com sucesso!"    
        
        }
    return response

@app.route('/consumers/company', methods = ['GET'])
def get_companies():
    response = {
        "statusCode": 200,
        "body": companies    
        
        }
    return response

@app.route('/consumers/company/{id}', methods = ['GET'])
def get_company(id):
    response = {
        "statusCode": 200,
        # Chumbado de exemplo
        "body": {id: {"name": "empresa1", "telefone": "22123456789"}}   
        }
    return response