"""
A problem from K*******s coding assessment.
"""


def solution(N, S, T):
    """
    This is a debugged version of the the string-wise process for ship cell coverage method.
    """
    def parse_positions(ships):
        """
        String-wise expanding the ship cells and group them properly with lists.
        Return the "ships" with a list contains all the ships (sublists).
        """
        ship_cells = list()
        for ship in ships.split(','):
            start, end = ship.split()
            # The tricky way to expand the ship covered cells by the start/end row and column
            start_row, start_col = int(start[:-1]), ord(start[-1]) - ord('A') + 1
            end_row, end_col = int(end[:-1]), ord(end[-1]) - ord('A') + 1
            ship_coverage_cell_list = list()
            for i in range(start_row, end_row + 1):
                for j in range(start_col, end_col + 1):
                    # generate the ship coverage cell properly.
                    ship_coverage_cell_list.append(f"{i}{chr(j + ord('A') - 1)}")
            # Append the ship into the ship list.
            ship_cells.append(ship_coverage_cell_list)
        return ship_cells

    def parse_hits(hits):
        """
        Process the hit coordinates string-wise.
        """
        positions = list()
        for hit in hits.split():
            row, col = int(hit[:-1]), ord(hit[-1]) - ord('A') + 1
            positions.append(f"{row}{chr(col + ord('A') - 1)}")
        return positions
    
    # Render the ship and hit data.
    ships = parse_positions(S)
    hit_positions = parse_hits(T)
    print(ships)
    print(hit_positions)

    sunk_count = 0
    hit_not_sunk_count = 0

    # Determine if the ship covered cells are all covered by hit cells.
    # Sunk if all cells are all covered by hit, not-sunk if not all cells are covered.
    for ship in ships:
        if all(cell in hit_positions for cell in ship):
            sunk_count += 1
        elif any(cell in hit_positions for cell in ship):
            hit_not_sunk_count += 1

    return f"{sunk_count},{hit_not_sunk_count}"

# Test case
print(solution(4, "1B 2C,2D 4D", "2B 2D 3D 4D 4A"))  # Output: "1,1"
print(solution(3, "1A 1B,2C 2C", "1B"))  # Output: "0,1"
