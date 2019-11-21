---------------------------------------------------------------------------------------
-- Name - deleteMaps.sql
-- Author - Evan Wu
-- Date Last Modified - 11-21-2019
-- Description - SQL File that contains query to delete from both Lists and Meta. 
-- 
-- Variables - to_delete - Set to the map ID that should be deleted.
---------------------------------------------------------------------------------------

SET @to_delete = '1';

DELETE FROM MAPS_DMAPS_LISTS
WHERE map_id = @to_delete;

DELETE FROM MAPS_DMAPS_META
WHERE map_id = @to_delete;

