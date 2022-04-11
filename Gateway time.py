import random
queue = list(range(1,195))
trouble = [0, 1, 2, 3, 4, 5]
trouble_actual = random.choices(trouble, weights=(55, 75, 45, 35, 10, 10), k=1)
walking_speed = random.choice([2.1, 2.17, 2.3])
q_choice = [1, 0]
q_wrong_actual = random.choices(q_choice, weights=(80, 20), k=1)
priority = [1, 0]
priority = random.choices(priority, weights=(80, 20), k=1)
time_gate = 60 + 3**trouble_actual.pop(0) + (100/walking_speed)
seatrow_n = random.choice(list(range(1, 33)))  * 3
if q_wrong_actual == 1 and priority == 1:
    time_gate = time_gate
elif q_wrong_actual == 0 and priority == 1:
    queue.appendleft("person1")
    time_gate += 20
elif seatrow_n/105 >= .5 and q_wrong_actual == 0 and priority == 0:
    queue.append("person1")
    time_gate += 20
elif seatrow_n/105 <= .5 and q_wrong_actual == 0 and priority == 0:
    queue.insert(len(queue)//2, "person1")
    time_gate += 15
    
print(time_gate)

