---------------------------------------------------------------------------------------
-- Name - pullMajors.sql
-- Author - Evan Wu
-- Date Last Modified - 11-29-2019
-- Description - SQL File that obtains the various Majors within a institution.
---------------------------------------------------------------------------------------

SET @institute_id = '17';

SELECT DISTINCT degree_descr
FROM MAPS_ACAD_PLAN
WHERE institute_id = @institute_id 
	OR institute_id = 0