class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carData = []
        fleets = 0
        bottle_neck = 0
        for i in range(len(position)):
            carData.append((position[i], speed[i]))
        carData.sort(reverse=True)
        for item in carData:
            pos = item[0]
            speed = item[1]
            time_destination = (target - pos)/speed
            if fleets == 0:
                fleets = 1
                bottle_neck = time_destination
            elif time_destination <= bottle_neck:
                # will catch up with the leader
                # and be in their fleet
                continue
            else:
                fleets += 1
                bottle_neck = time_destination
        return fleets
