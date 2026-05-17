#1
# Iria fazer todas as junções possíveis, gerando muitas linhas desnecessárias

#2
select
	c.first_name,
	c.last_name,
    a.address
from customer as c

join address as a on c.address_id = a.address_id;

#3
select
	f.title,
    c.name
from film as f
left join film_category as fc on f.film_id = fc.film_id
left join category as c on fc.category_id = c.category_id;

#4
select * from customer
join payment using (customer_id);

#5
# pois ele vai juntar todas as colunas identicas, não só as chaves

#6
select * from rental
where return_date is NULL;

#7
select * from rental
where return_date is not null;

#8
# Porque NULL é considerado nada, então não é possivel usar em operações lógicas

#9
select * from film as f
left join inventory as i on f.film_id = i.film_id
where i.inventory_id is null;

#10
# Apenas uma, porque o único valor que aparece é o NULL

#11
select count(film_id) from film;

#12
select sum(amount) from payment;

#13
select
	avg(length) as duracao_media
from film;

#14
select
	max(rental_rate),
    min(rental_rate)
from film;

#15
select 
	count(distinct customer_id)
from payment;

#16
select
	customer_id,
    sum(amount)
from payment
group by customer_id;

#17
# staff_id deveria estar no group by, para dizer ao banco de dados em qual linha colocar o staff_id

#18
select
	customer_id,
    sum(amount)
from payment
group by customer_id
having sum(amount) > 150;

#19
select 
	staff_id,
	count(payment_id)
from payment
where amount > 2.00
group by staff_id;

#20
# Primeiro ele vai pro FROM para identificar a tabela principal
# Depois ele vai no INNER JOIN para juntar as tabelas com o category_id for iguais nas duas tabelas
# no WHERE ele vai filtrar, e mostrar todos os registros da coluna name, menos os que for Action ou Horror
# Em seguida ele vai agrupar o resultado pelo name
# Vai filtrar este agrupamento, onde só vai mostrar grupos que film_id seja maior que 50
# E por último vai ler o SELECT lendo a funções e os campos

