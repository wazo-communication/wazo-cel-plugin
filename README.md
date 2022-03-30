# Wazo CEL API

This package adds an HTTP API for exposing Channel Event Logs (CEL) from Asterisk. Those can be analyzed to obtain call logs different from those available in Wazo Platform core in wazo-call-logd `/cdr`.

## Wazo Platform version

Wazo Platform version >= 20.15

## Installation

Connect to your stack and authenticate as user root. Then run the following command:

```shell
apt update
apt install wazo-plugind-cli
wazo-plugind-cli -c "install git https://github.com/wazo-communication/wazo-cel-plugin"
```

## Usage

See the OpenAPI specification for wazo-call-logd.

## Security

In order to use the API, the user must:
* have the `call-logd.cel.read` ACL

The tenant is determined from the token. If the tenant is the `master` tenant, all CEL will be listed. Else, only CELs from the token's tenant will be listed.
