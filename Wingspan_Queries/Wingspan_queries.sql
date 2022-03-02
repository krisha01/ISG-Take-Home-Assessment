--defining the fastest bird as having wingspan between 150 to 220,having 2 or more habitats and 3 or more food options
SELECT * FROM Birds where Wingspan between 150 and 220 and habitat_count >= 2 and food_count >= 3;

--Duplicate data
select bird_name, sci_bird_name, count(*) as NumDuplicates
from Birds
group by bird_name,sci_bird_name
having count(*) > 1

--calculate all credits/points for each player
SELECT Player_id, SUM(Points) FROM Points GROUP BY Player_ID ORDER BY Player_ID ASC;
