---------------------------------------------------------------------------------------
-- Name - checkExistingMap.sql
-- Author - Evan Wu
-- Date Last Modified - 11-29-2019
-- Description - Checks if an existing map already exists. If a map already exists, returns 1. If not, 0.
-- 				If a map already exists but is disabled, this still returns it. 
-- 				An admin should edit the existing disabled map.
---------------------------------------------------------------------------------------

SET @institute_id = '17';
SET @degree = 'Computer Science';
SET @input_start = 'Fall 2031';

-- Adjusts the full season to the format of the database.
SET @adjusted_start = CONCAT(
	CASE 
		WHEN SUBSTRING(@input_start, 1, LOCATE (' ', @input_start)  - 1) = 'Spring' THEN 'SP'			
		WHEN SUBSTRING(@input_start, 1, LOCATE (' ', @input_start)  - 1) = 'Fall' THEN 'FA'			
		ELSE 'WT'
		END,
	' ',
	SUBSTRING(@input_start, LOCATE (' ', @input_start) + 1, LENGTH(@input_start))
    );

SELECT 
    CASE
        WHEN (	SELECT COUNT(*)
				FROM MAPS_DMAPS_META
                WHERE institute_id = @institute_id
                        AND degree = @degree
                        AND start_year = @adjusted_start) > 1
        THEN '1'
        ELSE '0'
    END AS existingMap

