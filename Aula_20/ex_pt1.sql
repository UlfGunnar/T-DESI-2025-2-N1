# 1
select * from actor;

# 2
select
	title,
	description,
	release_year
from film;

# 3
select
	first_name,
	last_name,
    email
from customer;

#4
select distinct last_name from actor;

#5 
select concat(first_name, ' ', last_name) as Actor_Name from actor;

#6 
select
	title,
    rental_duration,
    rental_rate,
    rental_duration * rental_rate as total_rental_cost
from film;

#7
select * from actor
where first_name like 'JOE';

#8
select * from film
where description like "%DRAMA%";

#9
select * from customer
where active = 0 or last_name like "%M";

#10
select 
	country_id,
    country
from country
where country in ('Afghanistan', 'Bangladesh', 'China'); 

#11
select
	payment_id,
    amount,
    payment_date
from payment
where amount between 2.00 and 5.00;

#12
select
	payment_date,
	amount
from payment
order by amount desc
limit 20;

#13
select rating, count(rating) from film
group by rating;

#14
select
	avg(length),
    max(length),
    min(length)
from film;

#15
select
	customer_id,
    sum(amount) as amount
from payment
group by customer_id
having amount > 150;

#16
select 
	concat(cu.first_name, ' ', cu.last_name) as Nome_completo,
    ad.address,
    ci.city
from customer as cu
join address as ad on cu.address_id = ad.address_id
join city as ci on ad.city_id = ci.city_id;
    
#17
select
	a.first_name,
    a.last_name,
    f.title
from actor as a
join film_actor as fa on a.actor_id = fa.actor_id
join film as f on fa.film_id = f.film_id;

#18
select 
	f.title,
    f.description,
    f.release_year,
    f.rating,
    c.name
from film as f
join film_category as fc on f.film_id = fc.film_id
join category as c on fc.category_id = c.category_id;

#19
select first_name from customer

union

select first_name from actor;

#20
select 
	concat(cu.first_name, ' ', cu.last_name) 	as Cliente,
    cu.email 									as 'E-mail',
    count(re.rental_id)							as 'Totais Aluguéis',
    sum(pa.amount)									as 'Total gasto'
from customer as cu

join rental as re on cu.customer_id = re.customer_id
join payment as pa on re.rental_id = pa.rental_id

join address as ad on cu.address_id = ad.address_id
join city as ci on ad.city_id = ci.city_id
join country as co on ci.country_id = co.country_id

where co.country = 'Brazil' 
group by cu.customer_id, cu.first_name, cu.last_name, cu.email
having sum(pa.amount) > 100
order by 'Total gasto' desc;
    