class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        to_plant = n
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)-1):            
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                to_plant -= 1
                flowerbed[i] = 1
        return True if to_plant <= 0 else False

        