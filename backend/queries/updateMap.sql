---------------------------------------------------------------------------------------
-- Name - updateMap.sql
-- Author - Evan Wu
-- Date Last Modified - 11-29-2019
-- Description - SQL File that updates a map.
---------------------------------------------------------------------------------------

SET @map_id = '2';
SET @last_update_id = '';

UPDATE MAPS_DMAPS_META
SET last_update_id = @last_update_id,
	last_update_time = current_timestamp()
WHERE map_id = @map_id;

SET @sem1_class1 = '';
SET @sem1_class2 = '';
SET @sem1_class3 = '';
SET @sem1_class4 = '';
SET @sem1_class5 = '';
SET @sem1_class6 = '';
SET @sem1_class7 = '';
SET @sem2_class1 = '';
SET @sem2_class2 = '';
SET @sem2_class3 = '';
SET @sem2_class4 = '';
SET @sem2_class5 = '';
SET @sem2_class6 = '';
SET @sem2_class7 = '';
SET @sem3_class1 = '';
SET @sem3_class2 = '';
SET @sem3_class3 = '';
SET @sem3_class4 = '';
SET @sem3_class5 = '';
SET @sem3_class6 = '';
SET @sem3_class7 = '';
SET @sem3_class1 = '';
SET @sem3_class2 = '';
SET @sem3_class3 = '';
SET @sem3_class4 = '';
SET @sem3_class5 = '';
SET @sem3_class6 = '';
SET @sem3_class7 = '';
SET @sem4_class1 = '';
SET @sem4_class2 = '';
SET @sem4_class3 = '';
SET @sem4_class4 = '';
SET @sem4_class5 = '';
SET @sem4_class6 = '';
SET @sem4_class7 = '';
SET @sem5_class1 = '';
SET @sem5_class2 = '';
SET @sem5_class3 = '';
SET @sem5_class4 = '';
SET @sem5_class5 = '';
SET @sem5_class6 = '';
SET @sem5_class7 = '';
SET @sem6_class1 = '';
SET @sem6_class2 = '';
SET @sem6_class3 = '';
SET @sem6_class4 = '';
SET @sem6_class5 = '';
SET @sem6_class6 = '';
SET @sem6_class7 = '';
SET @sem7_class1 = '';
SET @sem7_class2 = '';
SET @sem7_class3 = '';
SET @sem7_class4 = '';
SET @sem7_class5 = '';
SET @sem7_class6 = '';
SET @sem7_class7 = '';
SET @sem7_class1 = '';
SET @sem7_class2 = '';
SET @sem7_class3 = '';
SET @sem7_class4 = '';
SET @sem7_class5 = '';
SET @sem7_class6 = '';
SET @sem7_class7 = '';
SET @sem8_class1 = '';
SET @sem8_class2 = '';
SET @sem8_class3 = '';
SET @sem8_class4 = '';
SET @sem8_class5 = '';
SET @sem8_class6 = '';
SET @sem8_class7 = '';

UPDATE MAPS_DMAPS_LISTS
SET course1 = @sem1_class1,
	course2 = @sem1_class2,
	course3 = @sem1_class3,
	course4 = @sem1_class4,
	course5 = @sem1_class5,
	course6 = @sem1_class6,
	course7 = @sem1_class7
WHERE semester_num = '1'
	AND map_id = @map_id;
    
UPDATE MAPS_DMAPS_LISTS
SET course1 = @sem2_class1,
	course2 = @sem2_class2,
	course3 = @sem2_class3,
	course4 = @sem2_class4,
	course5 = @sem2_class5,
	course6 = @sem2_class6,
	course7 = @sem2_class7
WHERE semester_num = '2'
	AND map_id = @map_id;
    
UPDATE MAPS_DMAPS_LISTS
SET course1 = @sem3_class1,
	course2 = @sem3_class2,
	course3 = @sem3_class3,
	course4 = @sem3_class4,
	course5 = @sem3_class5,
	course6 = @sem3_class6,
	course7 = @sem3_class7
WHERE semester_num = '3'
	AND map_id = @map_id;
    
UPDATE MAPS_DMAPS_LISTS
SET course1 = @sem4_class1,
	course2 = @sem4_class2,
	course3 = @sem4_class3,
	course4 = @sem4_class4,
	course5 = @sem4_class5,
	course6 = @sem4_class6,
	course7 = @sem4_class7
WHERE semester_num = '4'
	AND map_id = @map_id;
    
UPDATE MAPS_DMAPS_LISTS
SET course1 = @sem5_class1,
	course2 = @sem5_class2,
	course3 = @sem5_class3,
	course4 = @sem5_class4,
	course5 = @sem5_class5,
	course6 = @sem5_class6,
	course7 = @sem5_class7
WHERE semester_num = '5'
	AND map_id = @map_id;
    
UPDATE MAPS_DMAPS_LISTS
SET course1 = @sem6_class1,
	course2 = @sem6_class2,
	course3 = @sem6_class3,
	course4 = @sem6_class4,
	course5 = @sem6_class5,
	course6 = @sem6_class6,
	course7 = @sem6_class7
WHERE semester_num = '6'
	AND map_id = @map_id;
    
UPDATE MAPS_DMAPS_LISTS
SET course1 = @sem7_class1,
	course2 = @sem7_class2,
	course3 = @sem7_class3,
	course4 = @sem7_class4,
	course5 = @sem7_class5,
	course6 = @sem7_class6,
	course7 = @sem7_class7
WHERE semester_num = '7'
	AND map_id = @map_id;

UPDATE MAPS_DMAPS_LISTS
SET course1 = @sem8_class1,
	course2 = @sem8_class2,
	course3 = @sem8_class3,
	course4 = @sem8_class4,
	course5 = @sem8_class5,
	course6 = @sem8_class6,
	course7 = @sem8_class7
WHERE semester_num = '8'
	AND map_id = @map_id;
    