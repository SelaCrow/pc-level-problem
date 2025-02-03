# Level Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in writing a function that returns which level in a binary tree has the most nodes. The root of the tree is considered level 0.

Our function should accept one argument, the root of the binary tree, and return an integer representing the level of the tree with the most nodes.

For example, given the root of this tree:

```
Level 0:             1
                   /    \
                  /      \
Level 1:         2        3
               /   \    /   \
Level 2:      4     5  6     7
             / \      /
Level 3:    8   9    10
```

The function should return 2 because level 2 has 4 nodes (4, 5, 6, 7) which is more than any of the other levels.

If the tree is empty, return -1.

## Examples

### Example 1

The level with the most nodes in the following tree is level 2.

```
             1
           /    \
          /      \
         2        3
       /   \    /   \
      4     5  6     7
     / \      / \
    8   9    10 11
```

### Example 2

The level with the most nodes in the following tree is level 0.

```
    1
```

### Example 3

The level with the most nodes in the following tree is level 1.

```
             1
           /   \
          /     \
         2       3
       /   \
      4     5
```

### Example 4

The level with the most nodes in the following tree is level -1.

```
    Empty tree
```

Note that an empty tree is denoted by a `None` root.
