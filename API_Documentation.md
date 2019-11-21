# API Documentation

Currently under development. Please use sample data provided.

## Endpoints

/api/campuses

/api/degrees

/api/course

/api/map

## List Campuses
Get a list of campuses in CUNY.

**URL** : `/api/campuses/`

**Method** : `GET`

### Successful Response: 

* **Code** : `200 OK`
  
* **[Sample Response](response/campuses.json)**

## List Degrees
Get a list of degrees offered at particular campus.

**URL** : `/api/degrees/{institutecode}`
where "institutecode" can be obtained from "/api/campuses"

**Method** : `GET`

### Successful Response: 

* **Code** : `200 OK`

* **[Response for example request "/api/degrees/QNS01"](response/degrees.json)**

### Error Response

**Condition** : If provided `institutecode` parameter is not correct.

**Code** : `404 NOT FOUND`

**Content** : `{}`

## Course

### Get a course by course ID

**URL** : `/api/course/{crse_id}`

**Method** : `GET`

### Successful Response: 

* **Code** : `200 OK`

* **[Response for example request "/api/degrees/C000737"](response/get_course_by_id.json)**

### Error Response

**Condition** : If `crse_id` is not found.

**Code** : `404 NOT FOUND`

**Content** : `{}`

## Map

### Get a map by map_id
**URL** : `/api/map/{map_id}`

**Method** : `GET`

### Successful Response: 

* **Code** : `200 OK`

* **[Response for example request "/api/map/1"](response/get_map_by_id.json)**

### Error Response

**Condition** : If `map_id` is not found.

**Code** : `404 NOT FOUND`

**Content** : `{}`

## TO BE IMPLEMENTED BY NEXT MILESTONE

### Endpoints:
GET /api/course/search/?desc='internet':  Search course by description

GET /api/course/search/?name='cs355':     Search course by name

GET /api/map/q?campus='qns01'&degree='ACCT-BA' : Search maps available for a campus and major

PUT /api/map/{map_id}:  Make changes to a map

DELETE /api/map/{map_id}:  Delete a map
