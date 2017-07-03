We do this recursively.
- If the tree is empty, we return an empty string.
- We record each child as '(' + (string of child) + ')'
- If there is a right child but no left child, we still need to record '()' instead of empty string.
