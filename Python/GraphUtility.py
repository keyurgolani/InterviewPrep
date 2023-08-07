import unittest

class GraphUtility:
    """You are given an adjacency list representation of a graph. For example,
    ```
    input = {
        "A": ["B", "D"],
        "B": ["C", "A"],
        "C": ["D", "B"],
        "D": ["A", "C"]
    }
    ```
    For example, this makes a graph that looks like this
    
    A - B
    |   |
    D - C
    
    Let's assume that our input will be in the form where the graph will always make a loop like this.
    Can you write a function that will take this input and return a stringified version of this graph?
    For example, the return value for above example, could be ABCD.
    Follow Up:
    Rather than when we said the input will always look like a loop of nodes, let's say there is no guarantee.
    What's the optimization you'd make to this code to weed out the invalid input that's not a clean cycle of nodes."""
    @staticmethod
    def stringifyLoopedGraph(graph):
        """Brute Force:
        For a very basic implementation for this, we would basically implement a graph traversal that would visit each node one by one and append to result for returning.
        Since we want the stringified version to be accurate to the graph's order of nodes, we would have to go deeper into the graph at each step.
        Hence, we could use depth first traversal and visit each element one by one until we run out of nodes that are not visited.
        Runtime: O(n) Space: O(n) --> This is because we will visit each node once. And breadth first will use a stack to manage traversal that will at max hold all the elements in graph.
        Optimized:
        A much better approach comes to mind when we make use of the given constraint that there will only ever be cycles of nodes in input graph. And all other graphs will be invalid.
        This means that, this will be a glorified doubly linked list that has a cycle and connects the last node to it's first node creating a loop.
        Meaning, we can employ much simpler linked list traversal logic here to follow the graph and stringify each node.
        Only that we won't have next and previous nodes in this case. So we won't be able to identify which node is next and which node is previous.
        Hence, we will have to identify what direction we are going in next, by maintaining a previous node that we came from.
        While traversing, instead of expecting a `None` value at the end, we expect the head node (the one that we started traversal from) to terminate our traversal.
        Hence, we will maintain this start node value as well.
        Since we identified that a valid input will be a structure similar to a doubly linked list joined from end to it's head, we will be able to weed out invalid input that is otherwise a perfectly acceptable graph, by verifying if each node only connects to two other nodes.
        Now, graphs with less than 3 nodes are still valid cycles but will be invalidated by our logic. So we handle those edge cases in the beginning.
        Realize that in cases of less than 3 nodes in graph, the order of nodes doesn't matter.
        Runtime: O(n) Space: O(1)"""
        # If graph is None, return an empty string
        if not graph:
            return ""
        # If graph is 2 nodes or less, it will be our edge case
        if len(graph.keys()) <= 2:
            # In case of empty graph, this will return empty string
            # In case of one node, this will return that node in the string
            # In case of two nodes, this will return them in any order which is fine
            return "".join(graph.keys())
        # Initiate empty result
        result = []
        # Randomly determine a starting point from the adjecency list
        # Also, initiate currentNode as the node that we are processing right now
        currentNode = startNode = list(graph.keys())[0]
        # Initiate prevNode as the node that we travarsed to currentNode from
        # Also initialize nextNode that we will traverse to
        nextNode = prevNode = None    # At the beginning we didn't come from anywhere
        while nextNode != startNode:
            # Process the currentNode
            result.append(currentNode)
            # Check if current node has only two connections else throw
            connections = graph[currentNode]
            if len(connections) != 2:
                # Ideally this would be a relevant exception type like `InvalidInputError` or something.
                raise Exception("Not a valid graph");
            # Determine nextNode to be the link that we didn't come from
            nextNode = connections[0] if connections[0] != prevNode else connections[1]
            prevNode = currentNode
            currentNode = nextNode
        return "".join(result)


class GraphUtilityTest(unittest.TestCase):
    def test_stringifyLoopedGraph(self):
        """Testing below inputs:
        None
        
        A
        
        A - B
        
        A - B
        |   |
        D - C
        
        A - B
        | /
        C
        
        A - B
        |   |
        D   C
        
        A - B - E
        |   |   |
        D - C - F
        
        A - B - E
        |   |
        D - C
        
        A - B - C - D - E
        |             /
        I - H - G - F
        """
        self.assertEqual(GraphUtility.stringifyLoopedGraph(None), "")
        self.assertEqual(GraphUtility.stringifyLoopedGraph({}), "")
        self.assertEqual(GraphUtility.stringifyLoopedGraph({
            "A": []
        }), "A")
        self.assertEqual(GraphUtility.stringifyLoopedGraph({
            "A": ["B"],
            "B": ["A"]
        }), "AB")
        self.assertEqual(GraphUtility.stringifyLoopedGraph({
            "A": ["B", "C"],
            "B": ["C", "A"],
            "C": ["A", "B"]
        }), "ABC")
        self.assertEqual(GraphUtility.stringifyLoopedGraph({
            "A": ["B", "D"],
            "B": ["C", "A"],
            "C": ["D", "B"],
            "D": ["A", "C"]
        }), "ABCD")
        self.assertRaises(Exception, GraphUtility.stringifyLoopedGraph, {
            "A": ["B", "D"],
            "B": ["C", "A"],
            "C": ["B"],
            "D": ["A"]
        })
        self.assertRaises(Exception, GraphUtility.stringifyLoopedGraph, {
            "A": ["B", "D"],
            "B": ["C", "A", "E"],
            "C": ["B", "D", "F"],
            "D": ["A", "C"],
            "E": ["B", "F"],
            "F": ["E", "C"]
        })
        self.assertRaises(Exception, GraphUtility.stringifyLoopedGraph, {
            "A": ["B", "D"],
            "B": ["C", "A", "E"],
            "C": ["B", "D"],
            "D": ["A", "C"],
            "E": ["B"],
        })
        self.assertEqual(GraphUtility.stringifyLoopedGraph({
            "A": ["B", "I"],
            "B": ["C", "A"],
            "C": ["B", "D"],
            "D": ["E", "C"],
            "E": ["D", "F"],
            "F": ["E", "G"],
            "G": ["H", "F"],
            "H": ["I", "G"],
            "I": ["A", "H"]
        }), "ABCDEFGHI")


if __name__ == "__main__":
    unittest.main()