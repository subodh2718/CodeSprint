import os

def create_folder_structure():
    structure = {
        "Data Structures": [
            "Arrays", "Linked Lists", "Stacks", "Queues", "Hash Tables",
            "Trees", "Binary Search Trees", "Heaps", "Graphs", "Trie", "Union Find"
        ],
        "Algorithms": {
            "Sorting": [],
            "Searching": ["Linear Search", "Binary Search"],
            "Bit Manipulation": [],
            "Tree Traversal": ["in-order", "pre-order", "post-order"],
            "Graph Algorithms": ["DFS/BFS", "Topological Sort", "Shortest Path", "Minimum Spanning Tree"]
        },
        "Problem-Solving Techniques": [
            "Two Pointers", "Sliding Window", "Prefix Sum", "Fast and Slow Pointers",
            "Divide and Conquer", "Greedy", "Recursion", "Backtracking",
            "Dynamic Programming", "Top 'K' Elements"
        ]
    }

    for category, items in structure.items():
        os.makedirs(category, exist_ok=True)
        
        if isinstance(items, list):
            for item in items:
                os.makedirs(os.path.join(category, item), exist_ok=True)
        elif isinstance(items, dict):
            for subcategory, subitems in items.items():
                subcategory_path = os.path.join(category, subcategory)
                os.makedirs(subcategory_path, exist_ok=True)
                for subitem in subitems:
                    os.makedirs(os.path.join(subcategory_path, subitem), exist_ok=True)

    print("Folder structure created successfully!")

if __name__ == "__main__":
    create_folder_structure()