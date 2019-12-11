---------------------------------------------------------------------------------------
-- Name - findLatestMap.sql
-- Author - Evan Wu
-- Date Last Modified - 11-29-2019
-- Description - Finds the map_id of the most latest map for a particular degree at a institution.
-- 				Input for Degree and Start Year should be the full name. Can be adjusted if needed.
---------------------------------------------------------------------------------------


-- SET @institute_id = '';
-- SET @degree = 'Computer Science';
-- SET @input_start = 'SPRING 2022';

SET @institute_id = %s;
SET @degree = %s;
SET @input_start = %s;

-- This converts an input to something I can use to compare it.

SET @adjusted_start = SUBSTRING(@input_start, LOCATE (' ', @input_start) + 1, LENGTH(@input_start)) +
	CASE 
		WHEN SUBSTRING(@input_start, 1, LOCATE (' ', @input_start)  - 1) = 'Spring' THEN '0.1'			
		WHEN SUBSTRING(@input_start, 1, LOCATE (' ', @input_start)  - 1) = 'Fall' THEN '0.3'			
		ELSE '0.4'
	END;
    
SELECT map_id
FROM	(SELECT map_id, institute_id, degree,
				SUBSTRING(start_year, 4, 7) +
				CASE 
					WHEN SUBSTRING(start_year, 1, 3) = 'SP' THEN '0.1'			
					WHEN SUBSTRING(start_year, 1, 3) = 'FA' THEN '0.3'			
					ELSE '0.4'
				END AS converted
		FROM MAPS_DMAPS_META) AS A
WHERE converted <= @adjusted_start
ORDER BY converted DESC
LIMIT 1;
	