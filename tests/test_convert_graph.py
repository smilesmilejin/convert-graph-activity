from activity.main import convert_graph
import pytest 

def test_convert_graph_two_edges():
    #Arrange
    edge_list = [
        [1,2],
        [2,3]
    ]

    #Act/Assert
    assert convert_graph(edge_list) == [
        [0, 0, 0, 0], 
        [0, 0, 1, 0], 
        [0, 0, 0, 1], 
        [0, 0, 0, 0]
    ]

def test_convert_graph_three_edges():
    #Arrange
    edge_list = [
        [1,2],
        [1,3],
        [4,2]
    ]

    #Act/Assert
    assert convert_graph(edge_list) == [
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0]
    ]

def test_convert_graph_five_edges():
    #Arrange
    edge_list = [
        [1,2],
        [2,3], 
        [3,4], 
        [4,5], 
        [5,1]
    ]

    assert convert_graph(edge_list) == [
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 1, 0], 
        [0, 0, 0, 0, 0, 1], 
        [0, 1, 0, 0, 0, 0]
    ]