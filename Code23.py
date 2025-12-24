🚀 Day 23/50 – DSA Problem-Solving Challenge

📌 Problem: Height of a Binary Search Tree
📍 Concepts: Tree Traversal | Recursion | DFS
🧩 Difficulty: Easy–Medium

💡 Approach Used
✔ Identified the root as the node that never appears as a child
✔ Used Depth-First Search (DFS) to traverse the tree
✔ Calculated height using:
    height = 1 + max(left_subtree, right_subtree)
✔ Handled edge cases like an empty tree (n = 0)
✔ Counted nodes (not edges) along the longest root-to-leaf path

✨ Key Learnings
🔹 Difference between height and depth in trees
🔹 Why recursion is a natural fit for tree problems
🔹 How tree structure (balanced vs skewed) affects height
🔹 Importance of base cases in recursive solutions

📈 Result
A perfectly balanced BST with 3 levels → Height = 3
