# spEuler.py
An (in-progress!) implementation of spEuler! 

Kehlbeck, R., Görtler, J., Wang, Y., & Deussen, O. (2021). spEuler: Semantics-preserving Euler Diagrams. IEEE Transactions on Visualization and Computer Graphics, 28(1), 433-442.

A construction algorithm for Euler Diagrams. See the (beautifully-written!) paper for details.

The topology of these diagrams is determined by constructing a rank-based dual. At the current time a public implementation has not been provided. Additionally, the construction of the rank-based dual relies on the Consecutive Ones property of the corresponding adjacency matrix, and subsequent optimization on multiple possible permutations of the dual. 

Efficient construction algorithms for Consecutive Ones seem best facilitated by PQ-Trees or equivalently, PC-Trees. An implementation of PC-Trees is provided by N-Coder [here](https://github.com/N-Coder/pc-tree). For reasons of combinatorial efficiency, the referenced implementation does not generate all possible permutations expressed by the PC-Tree; moreover, its construction, while efficient, is still temporally significant, and the implementation is in C++, a language I am not overly familiar with :). 

Further exploration revealed that the requirement of monotone faces *and* stratification of the categories by rank and lexicographic groups essentially imposes an ordering that is determinstic. Moreover, this ordering can be derived directly from the fusion of consecutivve nodes in the previous rank. This opened up the avenue of using simple text-processing algorithms to define the dual, as can be found in this repository. The implementation has not been yet extensively tested (primarily on account of needing to find or build data sets), but works for the examples provided in the figures in the paper. The text-based nature of the processing also leaves much room for optimization.

