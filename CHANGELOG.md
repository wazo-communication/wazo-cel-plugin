# Changelog

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
