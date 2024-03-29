from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_queue = deque(truck_weights)
    bridge_queue = deque([])
    time_table = []
    while True:
        weight_sum = 0
        if not truck_queue:
            if not bridge_queue:
                break
        answer += 1
        if bridge_queue:
            if bridge_queue[0][1] >= bridge_length:
                bridge_queue.popleft()
        if bridge_queue:
            for i in range(len(bridge_queue)):
                bridge_queue[i][1] += 1
        if bridge_queue:    
            for i in range(len(bridge_queue)):
                weight_sum += bridge_queue[i][0]
        if truck_queue:
            if len(bridge_queue)+1 <= bridge_length and (weight_sum+truck_queue[0]) <= weight:
                truck = truck_queue.popleft()
                bridge_queue.append([truck,1]) 
    return answer