# API Documentation

Currently under development. Please use sample data provided.

## Endpoints

## List Campuses
Get a list of campuses in CUNY.

**URL** : `/api/campuses/`

**Method** : `GET`

### Successful Response: 

* **Code** : `200 OK`
  
* **[Sample Response](response/campuses.json)**

## List Majors
Get a list of majors offered at particular campus.

**URL** : `/api/majors/{institutecode}`
where "institutecode" can be obtained from "/api/campuses"

**Method** : `GET`

### Successful Response: 

* **Code** : `200 OK`

* **[Response for example request "/api/majors/QNS01"](response/majors.json)**

### Error Response

**Condition** : If provided `institutecode` parameter is not correct.

**Code** : `404 NOT FOUND`

**Content** : `{}`
