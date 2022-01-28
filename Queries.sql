-- 1) It took 30 min
select top 3 c.Brand
from Car c, Sale s
where month(s.DateTimee) <= 3 or month(s.DateTimee) >= 7 and month(s.DateTimee) <= 9 and year(s.DateTimee) = 2015
group by c.Brand
order by count(c.Brand) desc


-- 2) It took more minutes than I thought

DECLARE @qB INT = 1;
DECLARE @qE INT = 3;
DECLARE @year INT = 2012;

WHILE @year <= 2015
BEGIN
	SET @qB = 1;
	SET @qE = 3;

	WHILE @qE <= 12
	BEGIN
			select top 3 c.Color COLOR_, year(s.DateTimee) YEAR_
			from Car c, Sale s
			where month(s.DateTimee) >= @qB and month(s.DateTimee) <= @qE and year(s.DateTimee) >=2012 and year(s.DateTimee) <=2015
			group by c.Color, year(s.DateTimee)
			order by count(c.Color) desc	
		SET @qB = @qB + 3;
		SET @qE = @qE + 3;
	END;

	SET @year = @year + 1;
END;
