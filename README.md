# iza

Yet another authentication API specification, _iza_ being the malagasy word for _who_.

## Compliance

An iza-compliant API is an HTTP API that supports the two following calls:
* `GET /whoami`: tells the owner of a bearer token his `id` and `role`,
* `GET /whois/{userId}`: tells the owner of an API key the `id` and `role` of `userId`.

## Mock server

An iza-compliant mock server can be called [here](https://uzz59ld13f.execute-api.eu-central-1.amazonaws.com).

API key is `iza-api-key`, put it in `x-api-key` header as is standard.

Users are:

| name | role | bearer, put it in `authorization` header as is standard |
| --- | --- | --- |
| lita | student | bearer litaId |
| bema | teacher | bearer bemaId |
| bozy | teacher | bearer bozyId |
| lou | manager | bearer louId |
