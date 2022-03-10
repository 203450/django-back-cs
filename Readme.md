# Ambientación de back Django

## Instalación de los recursos de restframework
```bash
pip install djangorestframework
```
```bash
pip install markdown
```
```bash       
pip install django-filter  
```
```bash
pip install Pillow
```
```bash
pip install django-cors-headers
```

## Agregar librería a INSTALLED_APPS en settings
```bash 
'rest_framework',
'rest_framework.authtoken',
'corsheaders',
```

## Libreria para variables de entornno
```bash
'pip install python-dotenv',

```
## Agregar en settings: MIDDLEWARE

```bash
'corsheaders.middleware.CorsMiddleware',
```

## Agregar en settings
```bash
'http://localhost:3000',
```
