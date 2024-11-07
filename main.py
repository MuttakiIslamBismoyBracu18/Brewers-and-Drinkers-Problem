def is_valid_state(brewers_left, drinkers_left, brewers_right, drinkers_right):
    if brewers_left > 0 and drinkers_left > brewers_left:
        return False
    if brewers_right > 0 and drinkers_right > brewers_right:
        return False
    return True

def boat_crossing(brewers, drinkers, capacity):
    initial_state = (brewers, drinkers, 0, 0, True)
    queue = [initial_state]
    visited = set()
    visited.add(initial_state)
    parent_map = {}

    while queue:
        state = queue.pop(0)
        B_left, D_left, B_right, D_right, boat_on_left = state

        if B_left == 0 and D_left == 0:
            path = []
            while state in parent_map:
                prev_state, move = parent_map[state]
                path.append(move)
                state = prev_state
            path.reverse()
            return path

        if boat_on_left:
            for b in range(1, min(B_left, capacity) + 1):
                for d in range(min(D_left, capacity - b) + 1):
                    new_state = (B_left - b, D_left - d, B_right + b, D_right + d, not boat_on_left)
                    if is_valid_state(*new_state[:4]) and new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
                        parent_map[new_state] = (state, (b, d))
            for d in range(1, min(D_left, capacity) + 1):
                new_state = (B_left, D_left - d, B_right, D_right + d, not boat_on_left)
                if is_valid_state(*new_state[:4]) and new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)
                    parent_map[new_state] = (state, (0, d))
        else:
            for b in range(1, min(B_right, capacity) + 1):
                for d in range(min(D_right, capacity - b) + 1):
                    new_state = (B_left + b, D_left + d, B_right - b, D_right - d, not boat_on_left)
                    if is_valid_state(*new_state[:4]) and new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
                        parent_map[new_state] = (state, (b, d))
            for d in range(1, min(D_right, capacity) + 1):
                new_state = (B_left + 0, D_left + d, B_right - 0, D_right - d, not boat_on_left)
                if is_valid_state(*new_state[:4]) and new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)
                    parent_map[new_state] = (state, (0, d))
    return []

def main():
    B = int(input("Enter number of Brewers (B): "))
    D = int(input("Enter number of Beer Drinkers (D): "))
    C = int(input("Enter Boat Capacity (C): "))

    result = boat_crossing(B, D, C)

    with open('boat_crossing_output.txt', 'w') as file:
        if result:
            for move in result:
                file.write(f"B={move[0]}, D={move[1]}\n")
        else:
            file.write("No solution found.\n")

main()
