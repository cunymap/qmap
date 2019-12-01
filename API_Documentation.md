# API Documentation

Currently under development. 

Link to API: https://cs355map.herokuapp.com

## Endpoints

[/api/campuses](#campuses)

[/api/degrees](#degrees)

[/api/course](#course)

[/api/map](#map)

## <a name="campuses"></a> List Campuses
Get a list of campuses in CUNY.

**URL** : `/api/campuses/`

**Method** : `GET`

### Successful Response: 

* **Code** : `200 OK`
  
* **[Sample Response](response/campuses.json)**

## <a name="degrees"></a> List Degrees
Get a list of degrees offered at particular campus.

**URL** : `/api/degrees/{institute_id}`
where "institute_id" can be obtained from "/api/campuses"

**Method** : `GET`

### Successful Response: 

* **Code** : `200 OK`

* **[Response for example request "/api/degrees/QNS01"](response/degrees.json)**

### Error Response

**Condition** : If provided `institute_id` parameter is not correct.

**Code** : `404 NOT FOUND`

**Content** : `{}`

## <a name="course"></a> Course

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

### Search Courses 

There are two ways to search courses; by name or description of the course.

**URL** : `/api/course?q={search_string}&id={institute_id}&major={major}`

**Method** : `GET`

### Successful Response: 

* **Code** : `200 OK`

* **[Response for example request searching by description "/api/course/?q=Programming&id=17&major=computer%20science"](response/search_course_by_desc.json)**

* **[Response for example request searching by name "/api/course/?q=355&id=17&major=computer%20science"](response/search_course_by_name.json)**

### Error Response

**Condition** : If `q`, or `major`, or `id` are mispelled or not provided.

**Code** : `400 BAD REQUEST`

**Content** : `{'message' : 'invalid query parameter'}`

**Condition** : If no matches are found.

**Code** : `200 OK`

**Content** : `{ "message": "No matching courses found" }`

## <a name="map"></a> Map

### Get a map by map_id
**URL** : `/api/map/{map_id}`

**Method** : `GET`

### Successful Response: 

* **Code** : `200 OK`

* **[Response for example request "/api/map/2"](response/get_map_by_id.json)**

### Error Response

**Condition** : If `map_id` is not found.

**Code** : `404 NOT FOUND`

**Content** : `{ 'message' : 'map_id does not exist' }`

### Delete a map by map_id

**URL** : `/api/map/{map_id}`

**Method** : `DELETE`

### Successful Response: 

* **Code** : `204 NO CONTENT`

### Error Response

**Condition** : If `map_id` is not found.

**Code** : `404 NOT FOUND`

**Content** : `{ 'message' : 'map_id does not exist' }`


## TO BE IMPLEMENTED BY NEXT MILESTONE

### Endpoints:

GET /api/map/q?institute_id='17'&degree='Computer Science' : Search maps available for a campus and major

PUT /api/map/{map_id}:  Make changes to a map