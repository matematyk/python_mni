Drzewo lewicowe jest kolejką priorotytową zaimplemntowaną z wariantem kopca binanergo. 

W przeciwieństwie do kopców binarnych, drzewa lewicowe są bardziej mniej zbalansowane. W nawiązaniu do własności kopców, drzewa lewicowe są rozwijane. 
* Min kopiec własność key(i) >= key(parent(i)) 
* Cieższy z lewej strony ```dist(right(i)) <= dist(left(i))```
zdefiniowana wzorem:
```
dist( i ) = 1 + dist( right( i ) ). 
```



![Drzewo_Lewicowe](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/leftist_tree.jpg)



Referencje:
* https://en.wikipedia.org/wiki/Leftist_tree
* https://cdncontribute.geeksforgeeks.org/wp-content/uploads/leftist_tree.jpg

