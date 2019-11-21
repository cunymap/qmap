---------------------------------------------------------------------------------------
-- Name - pullMajors.sql
-- Author - Evan Wu
-- Date Last Modified - 11-21-2019
-- Description - SQL File that obtains the various Majors within a institution.
--
-- Variables - institute_id - Contains value for the institute to pull majors from.
---------------------------------------------------------------------------------------

SET @institution_id = '17';

SELECT degree_descr
FROM MAPS_ACAD_PLAN
WHERE institution_id = @institution_id
GROUP BY degree_descr