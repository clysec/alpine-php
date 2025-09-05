# Alpine PHP Images
Alpine PHP images for Nginx Unit

## Base
- ghcr.io/clysec/alpine-php:8.2-alpine3.22
- ghcr.io/clysec/alpine-php:8.2-alpine3.22-devcontainer

This is a base PHP-CLI image for Alpine with the following additions:
- Embedding (for Nginx Unit)
- GD
- Intl
- PDO-mysql
- mysqli
- zip
- bcmath
- kerberos
- imap-ssl
- freetype
- jpeg
- webp


## Unit
This is a PHP image for Nginx Unit based on the base image above.

### Configuration Path
A default configuration is added to /docker-entrypoint.d/unit.json

### Default Document Root
/app
