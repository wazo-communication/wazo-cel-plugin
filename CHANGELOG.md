# Changelog

## 2.4.0

* `/cel` now returns only CELs for the token's tenant. If the tenant is the `master` tenant, CELs of all tenants will be listed.

## 2.3.0

* `/cel` has a new parameter `call_log_id`

## 2.2.0

* `/cel` has a new parameter `uniqueid`

## 2.1.0

* Plugin was renamed from `wazo-cel` to `wazo-cel-plugin`

## 2.0.1

* Fix the OpenAPI documentation for `/cel` response body

## 2.0.0

This release includes breaking changes.

* Rename paramater `idbeg` to `after_id`
* Move the whole body of `/cel` (the list of CEL objects) under key `items`

## 1.3.0

* `/cel` has a new parameter `linkedid`

## 1.2.0

* Make `wazo-cel` compatible with later versions of Wazo

## 1.1.1

* Parameter `idbeg` now excludes the CEL with the given ID.

## 1.1.0

* `/cel` is only available to users in the master tenant.

## 1.0.0

* Add the CEL API
