class Record:
    def __init__(self, record_id: int, parent_id: int):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.children = []
    
    def __repr__(self) -> str:
        return str((self.node_id, self.children))


def BuildTree(records: 'list[Record]'):
    if not records:
        return None

    records.sort(key=lambda x: x.record_id)

    if records[-1].record_id != len(records) -1:
        raise ValueError("Tree must be continuous.")
    if records[0].record_id != 0:
        raise ValueError("Tree must start with id 0.")

    nodes = {}
    for record in records:
        check_validity(record)
        node = Node(record.record_id) 
        # Add node to `nodes` dict
        nodes[record.record_id] = node
        # Also, add it to its parent's self.children
        # record_id 0 is excluded because it has no parent
        if record.record_id > 0:
            nodes[record.parent_id].children.append(node)
    
    # Return only nodes[0] because nodes[0] act as the root and contains the tree building as a whole
    # If you want to see the full value of nodes, uncomment the print below
    # print(nodes)
    return nodes[0]


def check_validity(record: Record):
    if record.record_id == 0 and record.parent_id != 0:
        raise ValueError("Root node cannot have a parent.")
    if record.record_id < record.parent_id:
        raise ValueError("Parent id must be lower than child id.")
    if record.record_id != 0 and record.record_id == record.parent_id:
        raise ValueError("Tree is a cycle.")