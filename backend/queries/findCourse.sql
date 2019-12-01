---------------------------------------------------------------------------------------
-- Name - findCourse.sql
-- Author - Evan Wu
-- Date Last Modified - 11-29-2019
-- Description - SQL File that queries the MAPS_CRSE_CATALOG for majors within an institution.
---------------------------------------------------------------------------------------

SET @institute_id = %s;
SET @major = %s;
SET @search_input = %s;

SELECT *
FROM MAPS_CRSE_CATALOG AS A
	INNER JOIN ( 
		SELECT DISTINCT institute_id, degree, degree_descr
		FROM MAPS_ACAD_PLAN
		WHERE institute_id = @institute_id
		OR institute_id = '0') AS B
ON A.institute_id = B.institute_id
	AND A.subject = B.degree
WHERE LOCATE(@major, B.degree_descr) > 0 
	AND status = 'A'
HAVING A.catalog LIKE CONCAT('%',@search_input,'%') OR A.descr LIKE CONCAT('%', @search_input, '%')
ORDER BY course_id, eff_date
