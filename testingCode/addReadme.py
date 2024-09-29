import os

def create_folder_and_readme(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {path}")
    else:
        print(f"Folder already exists: {path}")
    
    readme_path = os.path.join(path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, 'w') as f:
            f.write(f"# {os.path.basename(path)}\n\nThis folder contains information about {os.path.basename(path)}.")
        print(f"Created README.md in: {path}")
    else:
        print(f"README.md already exists in: {path}")

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
        create_folder_and_readme(category)
        
        if isinstance(items, list):
            for item in items:
                create_folder_and_readme(os.path.join(category, item))
        elif isinstance(items, dict):
            for subcategory, subitems in items.items():
                subcategory_path = os.path.join(category, subcategory)
                create_folder_and_readme(subcategory_path)
                for subitem in subitems:
                    create_folder_and_readme(os.path.join(subcategory_path, subitem))

    print("Folder structure creation and README.md file addition completed!")

if __name__ == "__main__":
    create_folder_structure()