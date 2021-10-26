

def exchange_money(budget, exchange_rate):
    
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills

def get_number_of_bills(budget, denomination):
    return int(budget / denomination)

def get_exchangeable_value(budget, exchange_rate, spread, denomination):
    exchange_rate = (exchange_rate / spread) + exchange_rate
    exchange_value = exchange_money(budget, exchange_rate)
    bills = get_number_of_bills(exchange_value, denomination)

    return get_value_of_bills(denomination, bills)
    

def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    exchange_rate = (exchange_rate / spread) + exchange_rate
    exchange_value = exchange_money(budget, exchange_rate)
    bills = get_number_of_bills(exchange_value, denomination)
    return int(exchange_value - get_value_of_bills(denomination, bills))

 


def compute(budget, exchange_rate, spread, denomination):
    print(get_exchangeable_value(budget, exchange_rate, spread, denomination))
    print(non_exchangeable_value(budget, exchange_rate, spread, denomination))

compute(127.25, 1.20, 10, 5)