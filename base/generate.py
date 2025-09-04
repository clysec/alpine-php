import os
import sys

dir = os.path.dirname(__file__)
phpver = [f.path for f in os.scandir(os.path.join(dir, 'php')) if f.is_dir() and f.name.startswith('8.')]

args = "-".join(sys.argv)

if os.path.exists(os.path.join(dir, 'patched')):
    print('Already patched')
    exit(0)

for folder in phpver:
    alpver = [f.path for f in os.scandir(folder) if f.is_dir() and f.name.startswith('alpine')]
    
    for alp in alpver:
        with open(os.path.join(alp, 'cli', 'Dockerfile'), 'r') as f:
            data = f.read()
            
        data = data.replace('sqlite-dev', 'sqlite-dev zlib-dev jpeg-dev freetype-dev libwebp-dev icu-dev libpng-dev openssl-dev libzip-dev mariadb-dev krb5-dev')
        data = data.replace('--enable-option-checking=fatal', '--enable-option-checking=fatal --enable-embed --enable-gd --enable-intl --with-pdo-mysql --with-mysqli --enable-opcache --with-zip --enable-bcmath --with-kerberos --with-imap-ssl --with-freetype --with-jpeg --with-webp')
        
        if "devcontainer" in args:
            data = data.replace(f'FROM alpine:{alp}', f'FROM mcr.microsoft.com/devcontainers/base:alpine-{alp}')
        
        with open(os.path.join(alp, 'cli', 'Dockerfile'), 'w') as f:
            f.write(data)
        
        print(f'Patched {os.path.join(alp, "cli", "Dockerfile")}')

with open(os.path.join(dir, 'patched'), 'w') as f:
    f.write('Patched\n')