SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[^AEIOUaeiou]|[^AEIOUaeiou]$';

-- Not '|' means or in regula expression