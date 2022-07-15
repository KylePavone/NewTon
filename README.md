# NewTon
SQL tasks:

1.
    1) Создание таблицы:

        CREATE TABLE cars(
            id SERIAL PRIMARY KEY, 
            model_name VARCHAR(100) NOT NULL, 
            car_brand VARCHAR(100) NOT NULL, 
            year_of_manufacture INTEGER NOT NULL, 
            color VARCHAR(100), 
            price INTEGER NOT NULL
        );


    2)Все модели марки BMV:
        
        SELECT model_name
        FROM cars 
        WHERE car_brand = 'BMV';


    3)Вывода всех автомобилей в промежутке от 1960 по 1970 года выпуска стоимостью дороже 100000:

        SELECT * 
        FROM cars 
        WHERE (year_of_manufacture BETWEEN 1960 AND 1970) AND (price > 100000);

----------------------------------------------------------------------------------------------------
2.
    1)Есть две связанных таблицы – покупатели и заказы.
        
        CREATE TABLE customers(
            id serial PRIMARY KEY, 
            full_name varchar(255) NOT NULL, 
            city varchar(100) NOT NULL
        );

            CREATE TABLE orders(
            id SERIAL PRIMARY KEY, 
            customer_id INTEGER REFERENCES customers(id), 
            order_price INTEGER NOT NULL, 
            order_date DATE NOT NULL,
        );


    2)Вывода всех покупателей из города Минск:

        SELECT *
        FROM customers 
        WHERE city = 'Minsk';


    3)Вывода самого крупного заказа в городе Москва за 2020 год:

        SELECT MAX(order_price) 
        FROM orders 
        INNER JOIN customers 
        ON customers.id = orders.id 
        WHERE(order_date BETWEEN '2020-01-01' and '2020-12-31') AND city = 'Москва';
