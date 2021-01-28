from lib_vector import *

# Création de points...
a = Point(-2, 1)
b = Point(0, -3)
c = Point(1, 1)
d = Point(5, -3)

# ...Et création de vecteurs à partir de ces points
ac = make_vector_from_points(a, c)
ad = make_vector_from_points(a, d)
bc = make_vector_from_points(b, c)
db = make_vector_from_points(d, b)
fun_vector = Vector(5, 5) # (ou même directe, si vous aimez ce genre de choses)

print(a, ac) # Les points et vecteurs sont imprimés dans le format (x; y)

print(ac.norm()) # Calcul de la norme d'un vecteur 

print(det(ac, db)) # Calcul du déterminant de deux vecteurs...

# ...ou test direct pour déterminer si ils sont colinéaires !
if are_vectors_colinear(ac, db):
    print(f"Les vecteurs de coordonnées {ac}, {db} sont colinéaires !")

# Création de a2, image de a par la translation de vecteur ac 
a2 = apply_vector(a, ac) 

# Addition de deux vecteurs
db2 = add_vectors(db, db) 
