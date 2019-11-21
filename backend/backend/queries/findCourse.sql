---------------------------------------------------------------------------------------
-- Name - findCourse.sql
-- Author - Evan Wu
-- Date Last Modified - 11-21-2019
-- Description - SQL File that queries the MAPS_CRSE_CATALOG for majors within an institution.
-- 				First, it pulls all courses that fit the institution and subject.
--				Then the HAVING clauses searches based on input in both Catalog # and Course Description.
---------------------------------------------------------------------------------------

SET @institution_id = '17';
SET @major = 'Computer Science';
SET @search_input = 'Programming';

SELECT A.course_id, A.eff_date, A.institution_id, A.status, A.subject, A.catalog, A.descr, A.min_units, A.max_units, A.designation
		FROM MAPS_CRSE_CATALOG AS A
			INNER JOIN MAPS_ACAD_PLAN AS B
				ON A.subject = B.degree
        WHERE A.institution_id = @institution_id
			AND LOCATE(@major, B.degree_descr) > 0
GROUP BY course_id
HAVING A.catalog LIKE CONCAT('%',@search_input,'%') OR A.descr LIKE CONCAT('%', @search_input, '%')
ORDER BY course_id