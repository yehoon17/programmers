def str_to_min(time):
    hour, minute = time.split(":")
    return int(hour)*60 + int(minute)

def n_unit(extra_time, unit_time):
    if extra_time % unit_time == 0:
        return extra_time // unit_time
    return max(int(extra_time/unit_time) + 1, 0)


def get_fee(total_time, fees):
    base_time, base_fee, unit_time, unit_fee = fees
    extra_time = total_time - base_time
    extra_fee = n_unit(extra_time, unit_time)*unit_fee
    return base_fee + extra_fee

def solution(fees, records):
    history = {}
    
    for record in records:
        time, car, stat = record.split()
        if car not in history:
            history[car] = [stat, time, 0]
        else:
            if stat == "IN":
                history[car][1] = time
            else:
                history[car][2] += str_to_min(time) - str_to_min(history[car][1])
            history[car][0] = stat
            
    for car in history:
        if history[car][0] == "IN":
            history[car][2] += str_to_min("23:59") - str_to_min(history[car][1])
            
    cars = [car for car in history]
    cars.sort()
    payments = [get_fee(history[car][2], fees) for car in cars]
    
    return payments