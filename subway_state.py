import pandas as pd
import numpy as np
class environment:
    def load_station(self):
        stations = pd.read_excel("tnSubwayStatn.xlsx").to_numpy().tolist()
        return stations
    def make(self,start):
        ways = []
        for a in start:
        
            ways.append([0,a])
        return ways
    def right_station(self,current_station,stations):
        where = stations.index(current_station)
        if(len(stations)-1 == where):
            return current_station
        elif(current_station[2] != stations[where+1][2]):
            return current_station
        else:
            return stations[where+1]
    def left_station(self,current_station,stations):
        where = stations.index(current_station)
        if(0 == where):
            return current_station
        elif(current_station[2] != stations[where-1][2]):
            return current_station
        else:
            return stations[where-1]
    def start_station(self,where,stations):
        c = []
        for station in stations:
            if(station[1] == where):
                c.append(station)
        self.start = c
        return c
    def end_station(self,where,stations):
        for station in stations:
            if(station[1] == where):
                self.start = station
                return station
    def trasfer_station(self,current_station,stations,transfer_line):
        if(current_station[2] == transfer_line):
            return current_station
        for station in stations:
            if(station[1] == current_station[1] and station[2] == transfer_line):
                return station
        print(current_station,transfer_line)
        assert 1==2        
    def mode(self,mode):
        self.mode = mode
    def score(self,action):
        if(self.mode == "station"):
            if(action == 2):
                return 0.1
            else:
                return 1
        if(self.mode == "transfer"):
            if(action == 2):
                return 1
            else:
                return 0
        if(self.mode == "half"):
            if(action == 2):
                return 2
            else:
                return 1
