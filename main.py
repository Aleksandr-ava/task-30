from queue import Queue
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer:
    def __init__(self, number):
        self.number = number


class Cafe:
    def __init__(self, num_tables):
        self.tables = [Table(i) for i in range(1, num_tables + 1)]
        self.queue = Queue()
        self.customer_count = 0

    def customer_arrival(self):
        while self.customer_count < 5:
            sleep(1)
            self.customer_count += 1
            customer = Customer(self.customer_count)
            print(f'Посетитель {customer.number} прибыл.')
            self.queue.put(customer)

    def serve_customer(self):
        while True:
            for table in cafe.tables:
                if not table.is_busy:
                    customer = self.queue.get()
                    if table.is_busy is False:
                        print(table.is_busy)
                        print(f'Посетитель {customer.number} сел за стол {table.number}')
                        table.is_busy = True
                        sleep(5)
                        print(f'Посетитель {customer.number} покушал и ушёл со стола {table.number}.')
                        table.is_busy = False
                    else:
                        print(table.is_busy)
                        print(f'Посетитель номер {self.customer_count} ожидает свободный стол.')


cafe = Cafe(3)

arrival_thread = Thread(target=cafe.customer_arrival)
table_threads = Thread(target=cafe.serve_customer)

arrival_thread.start()
table_threads.start()

arrival_thread.join()
table_threads.join()

# Вывод на консоль (20 посетителей [ограничение выставить в методе customer_arrival]):
# Посетитель номер 1 прибыл
# Посетитель номер 1 сел за стол 1
# Посетитель номер 2 прибыл
# Посетитель номер 2 сел за стол 2
# Посетитель номер 3 прибыл
# Посетитель номер 3 сел за стол 3
# Посетитель номер 4 прибыл
# Посетитель номер 4 ожидает свободный стол
# Посетитель номер 5 прибыл
# Посетитель номер 5 ожидает свободный стол
# ......
# Посетитель номер 20 прибыл
# Посетитель номер 20 ожидает свободный стол
# Посетитель номер 17 покушал и ушёл.
# Посетитель номер 20 сел за стол N.
# Посетитель номер 18 покушал и ушёл.
# Посетитель номер 19 покушал и ушёл.
# Посетитель номер 20 покушал и ушёл.
