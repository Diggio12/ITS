def find_disappeared_numbers(nums: list[int]) -> list[int]:
    numeri_mancanti: list[int] = []
    lung_lst= len(nums)
    for i in range (1, lung_lst + 1):
        if i not in nums:
            numeri_mancanti.append(i)
    return numeri_mancanti