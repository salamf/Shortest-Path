""" CSC 225: Fall 2021
  ' Programming Assignment: Mictoria's Maze
  ' Name: Salam Fazil
  ' ID: V00935894
  ' :)
"""

import sys
from Graph import Graph


def main():
    # Read input from STDIN and store as an array of the lines in 'data'
    # (each line as separate element)
    data = sys.stdin.readlines()

    # Store the size of the city in 'num_lines' and remove from list.
    # If value error is given, exit code since non-valid input was given
    # Note: rows of city = columns of city,
    # So grid-size of city = num_lines * num_lines (num_lines^2)
    num_lines = get_size(data)

    # Remove all '\n' chars from data and
    # convert 'data' (list of input lines) into one string
    data = modify_input(data)

    # Create Graph 'city_graph' to insert city in
    city_graph = Graph()

    # Insert all vertices and edges into graph
    # (basically represent grid city in a graph data structure)
    insert_to_graph(data, city_graph, num_lines)

    # Get shortest path from A to B in 'city_graph' without obstruction ('#')
    # using the 'find_shortest_path' method (bfs, created in Graph.py class)
    shortest_path = city_graph.find_shortest_path(data, data.index('A'), data.index('B'))

    # Print output to STDOUT
    print_output(shortest_path)


def get_size(data):
    """ Get grid-size of city,
        exit code if non-valid input was given """

    try:
        return int(data.pop(0))

    except (ValueError, IndexError):

        print("Please enter valid input")
        print("exiting...")
        exit(-1)


def modify_input(data):
    """ Strip all '\n' chars from 'data' and convert 'data'
        from list of strings to one long string """

    strip_new_lines(data)
    data = ''.join(data)
    return data


def strip_new_lines(data):
    """ Remove '\n' chars from each string in 'data' """

    for index, line in enumerate(data):
        data[index] = line.strip()


def insert_to_graph(data, graph, num_lines):
    """ Insert all elements in 'data' into 'graph'
        and create edges between adjacent elements """

    for index, letter in enumerate(data):
        add_edges(index, num_lines, graph)


def add_edges(index, num_lines, graph):
    """ Add adjacent (top, left, right, and bottom) edges
        for a certain vertex if position exists """

    if check_top_exists(index, num_lines):
        graph.add_edge(index, index - num_lines)

    if check_left_exists(index, num_lines):
        graph.add_edge(index, index - 1)

    if check_right_exists(index, num_lines):
        graph.add_edge(index, index + 1)

    if check_bottom_exists(index, num_lines):
        graph.add_edge(index, index + num_lines)


def check_top_exists(index, size):
    """ Return true if top position exists, false otherwise """

    return index - size >= 0


def check_left_exists(index, size):
    """ Return true if left position exists, false otherwise """

    return index - 1 >= 0 and index % size != 0


def check_right_exists(index, size):
    """ Return true if right position exists, false otherwise """

    return index + 1 < size ** 2 and (index + 1) % size != 0


def check_bottom_exists(index, size):
    """ Return true if bottom position exists, false otherwise """

    return index + size < size ** 2


def print_output(shortest_path):
    """ Print 'shortest_path' (length of shortest path)
        and "IMPOSSIBLE" if 'shortest_path' = -1 (no path exists) """

    if shortest_path == -1:
        print("IMPOSSIBLE")
    else:
        print(shortest_path)


if __name__ == '__main__':
    main()
