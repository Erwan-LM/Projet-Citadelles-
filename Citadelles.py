# Constantes pour définir le nombre de chaque type de carte
NB_CARTES_PERSONNAGE = 8
NB_CARTES_QUARTIER = 69
NB_CARTES_AIDE_JEU = 7

# Classe pour représenter une carte de quartier
class CarteQuartier:
  def __init__(self, couleur, cout, effet):
    self.couleur = couleur
    self.cout = cout
    self.effet = effet

# Classe pour représenter une carte personnage
class CartePersonnage:
  def __init__(self, nom, effet):
    self.nom = nom
    self.effet = effet

# Classe pour représenter une carte d'aide de jeu
class CarteAideJeu:
  def __init__(self, nom, effet):
    self.nom = nom
    self.effet = effet

# Classe pour représenter une pièce d'or
class PieceOr:
  def __init__(self, valeur):
    self.valeur = valeur

# Classe pour représenter une cité
class Cite:
  def __init__(self, joueur):
    self.joueur = joueur
    self.quartiers = []
    self.or = 2

# Classe pour représenter un joueur
class Joueur:
  def __init__(self, nom):
    self.nom = nom
    self.cite = Cite(self)
    self.cartes_personnage = []
    self.cartes_aide_jeu = []

# Fonction pour initialiser le jeu
def initialiser_jeu():
  # Créer les cartes de quartier
  cartes_quartier = []
  for i in range(NB_CARTES_QUARTIER):
    couleur = "violet" if i % 2 == 0 else "blanc"
    cout = i + 1
    effet = "Effet de la carte {}".format(i)
    cartes_quartier.append(CarteQuartier(couleur, cout, effet))

  # Mélanger les cartes de quartier
  shuffle(cartes_quartier)

  # Créer les cartes personnage
  cartes_personnage = []
  for i in range(NB_CARTES_PERSONNAGE):
    nom = "Personnage {}".format(i)
    effet = "Effet du personnage {}".format(i)
    cartes_personnage.
