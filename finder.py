def greedy(way,next_station,best):
    if not (next_station[1] in best.keys()):
        return 1
    elif way[0] <= best.get(next_station[1]):
        return 1
    return 0
from random import *
from subway_state import *
env = environment()
stations = env.load_station()
start = env.start_station(input("출발지를 입력해 주세요 : "),stations)
end = env.end_station(input("도착지를 입력해 주세요 : "),stations)
mode = env.mode(input("모드를 입력해 주세요 (trasnfer/station): "))
ways = env.make(start)
temp_way = []
best = {}
while 1:
    for way_index in range(len(ways)):
        way = ways[way_index]
        if(way[-1][1] == end[1]):
            if not way in temp_way:
                temp_way.append(way)
            continue
        for action in range(3):
            new_way = ways[way_index].copy()
            if(action == 0):
                next_station = env.left_station(current_station=way[-1],stations=stations)
                new_way[0] += round(env.score(action),1)
                if not next_station in way and greedy(new_way,next_station,best):
                    new_way.append(next_station)
                    temp_way.append(new_way)
                    if not (next_station[1] in best.keys()):
                        best[next_station[1]] = new_way[0]
                    elif new_way[0] < best.get(next_station[1]):
                        best[next_station[1]] = new_way[0]
            elif(action == 1):
                next_station = env.right_station(current_station=way[-1],stations=stations)
                new_way[0] += env.score(action)
                if not next_station in way and greedy(new_way,next_station,best):
                    new_way.append(next_station)
                    temp_way.append(new_way)            
                    if not (next_station[1] in best.keys()):
                        best[next_station[1]] = new_way[0]
                    elif new_way[0] < best.get(next_station[1]):
                        best[next_station[1]] = new_way[0]
            #transfer
            elif(action == 2):
                if(way[-1][4] == "환승역"):
                    possible_transfer_lines = str(way[-1][5]).split("+")
                    for possible_transfer_line in possible_transfer_lines:
                        new_way = ways[way_index].copy()
                        next_station = env.trasfer_station(current_station=way[-1],stations=stations,transfer_line=possible_transfer_line) 
                        new_way[0] += round(env.score(action),1)
                        if not next_station in way and greedy(way,next_station,best):
                            if len(way) >= 4 and not(way[-1][1] == way[-2][1] and way[-1][1] == next_station[1]):
                                new_way.append(next_station)
                                temp_way.append(new_way)
                                if not (next_station[1] in best.keys()):
                                    best[next_station[1]] = new_way[0]
                                elif new_way[0] < best.get(next_station[1]):
                                    best[next_station[1]] = new_way[0]
                            elif len(way) < 4:
                                new_way.append(next_station)
                                temp_way.append(new_way)
                                if not (next_station[1] in best.keys()):
                                    best[next_station[1]] = new_way[0]
                                elif new_way[0] < best.get(next_station[1]):
                                    best[next_station[1]] = new_way[0]
                        del new_way
                        del next_station
                        new_way = []
                        next_station = []
            del new_way
            del next_station
            new_way = []
            next_station = []
    # print(temp_way,"\n\n")
    # print(best,"\n\n")
    # print(temp_way,"\n\n")
    # time.sleep(5)
    ways = temp_way
    temp_way = []
    if(all(wayk[-1] == end for wayk in ways)):
        break
if(env.mode == "transfer"):
    min_thing = 100
    for way_index in range(len(ways)):
        way = ways[way_index]
        min_thing = min(min_thing,way[0])
    ways = [way for way in ways if way[0] == min_thing]
for j in range(len(ways)):
    print("\n")
    way = ways[j]
    print(j+1,"번 경로","(",way[0],")")
    print("출발 : ",way[1][1],way[1][3])
    for station_index in range(1,len(way)-1):
        station = way[station_index]
        if(station[2] != way[station_index+1][2]):
            print(station[1],station[3],"->",way[station_index+1][3])
    print("도착 : ",way[len(way)-1][1],way[len(way)-1][3])