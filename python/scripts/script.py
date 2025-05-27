lineDict = {
    "configs/__init__.py": [2, 6],
    "configs/database.py": [9, 18],
    
    "controllers/__init__.py": [21, 29],
    "controllers/admin_controller.py": [32, 188],
    "controllers/auth_controller.py": [191, 354],
    "controllers/customer_controller.py":[356,397],
    
    "databases/__init__.py":[399,410],
    "databases/order_data.py":[412,454],
    "databases/product_data.py":[456,543],
    "databases/session_data.py":[545,572],
    "databases/user_data.py": [574,612],
    
     "enums/__init__.py":[614,622],
     "enums/category.py":[625,633],
     "enums/order_status.py":[635,644],
     "enums/role.py":[646,654],
    
    "models/__init__.py":[656,664],
    "models/order.py":[666,693],
    "models/product.py":[694,721],
    "models/user.py":[722,751],
    
    "payloads/user.py":[752,761],
    "payloads/admin_login_request.py":[762,774],
    "payloads/customer_login_request.py":[775,784],
    "payloads/global_response.py":[785,807],
    
    "repositories/__init__.py":[808,815],
    "repositories/order_repo.py":[816,855],
    "repositories/user_repo.py":[856,906],
    
    "services/__init__.py":[907,916],
    "services/admin_service.py":[917,1019],
    "services/auth_service.py":[1020,1064],
    "services/customer_service.py":[1065,1316],
    
    "utils/__init__.py":[1317,1336],
    "utils/console.py":[1338,1348],
    "utils/validator.py":[1349,1410],
    "utils/random_number_generator.py":[1411,1423],
    
    "./main.py":[1424,1468],
    "payloads/__init__.py":[1469,1477],
    
    
}
 
with open('fileContent.txt', 'r') as f:
    lines = f.readlines()

for new_filename, (start, end) in lineDict.items(): 
    content_to_write = lines[start-1:end]
    import os
    os.makedirs(os.path.dirname(new_filename), exist_ok=True)
    with open(new_filename, 'w') as f:
        f.writelines(content_to_write)

    print(f"Wrote lines {start}-{end} to {new_filename}")
