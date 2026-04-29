def main():
    lst = []
    print(f"Current list = {lst}")

    # append
    lst.append(1)
    lst.append("2")
    print(f"After append = {lst}")

    #extend
    lst2 = [3, 4, 5, 6, 7]
    lst.extend(lst2)
    print(f"After extend = {lst}")

    # insert
    lst.insert(5, "index = 5 insert")
    print(f"After insert = {lst}")

    # pop
    print(f"pop = {lst.pop()}")
    print(f"pop = {lst.pop(3)}")
    print(f"Atfer pop = {lst}")

    #clear
    lst.clear()
    print(f"After clear = {lst}")

    for i in range(0, 5):
        lst.append(i)
    
    #index
    print(f"After index = {lst.index(2)}")
    print(f"After index = {lst.index(3)}")

    #count
    print(f"lst 3 Count = {lst.count(3)}")

    for _ in range(3):
        lst.append(3)
    
    print(f"lst 3 Count = {lst.count(3)}")

    lst.sort()
    print(f"After sort = {lst}")

    #reverse
    lst.reverse()
    print(f"After reverse = {lst}")

    lst_copy = lst.copy()
    print(f"lst = {lst}")
    print(f"lst = {lst_copy}")

if __name__ == "__main__":
    main()