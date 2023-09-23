**ALGORITHME A\*** 

L’algorithme A\* est un algorithme heuristique qui permet de trouver très rapidement un plus court chemin entre deux points avec d’éventuels obstacles. Outre sa vitesse, cet algorithme est réputé pour garantir une solution en sortie. 

Cet algorithme est un cas d’application d’algorithme de Dijktra 

1) **Comment fonctionne-t-il ?** 

Illustrons le fonctionnement de cet algorithme par un exemple :  

Un individu cherche à se déplacer d’un point A à un point B en empruntant le chemin le plus court. La situation est représentée par les schémas ci-dessous : 

*Algorithme de Dijkstra ![](Aspose.Words.ac811430-2d60-44b3-bb64-15b1f248893f.001.png)![](Aspose.Words.ac811430-2d60-44b3-bb64-15b1f248893f.002.png)*

- Le point bleu représente le point de départ A  
- Le point vert représente le point d’arriver B.  
- Les cases bleues représentent les voisins visités 
2) **Installation** 
- Langage : Python3 
- Editeur : VS code 
- Bibliothèque : tkinter *(pip install tk)* 
3) **Cas d’utilisation détaillées** 
- Sélectionner un point de départ A et un point d’arriver B 
- Lorsque vous appuyez sur le bouton "Start", l'algorithme A\* est exécuté pour trouver le chemin le plus court entre le point de départ et le point d'arrivée. 
- L'algorithme A\* utilise une file d'attente pour explorer les nœuds de la grille. 
- Une fois le chemin trouvé, il est affiché en bleu. 
- Vous pouvez effacer la grille en appuyant sur le bouton "Clear". 
