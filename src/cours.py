class Cours:
    """
    Class to create a Cours
    """
    def __init__(self, dateDebut, dateFin, matiere, enseignant, commentaire):
        """
            Constructor
                dateDebut
                eateFin
                matiere
                enseignant
                commentaire
        """
        self.dateDebut = dateDebut
        self.dateFin = dateFin
        self.matiere = matiere
        self.enseignant = enseignant
        self.commentaire = commentaire

    def __str__(self):
        return "date debut : " + self.dateDebut + "\ndate de fin : " + self.dateFin + "\nmatiere : " + self.matiere + "\nenseignant : " + self.enseignant + "\ncommentaire : " + self.commentaire + "\n"

    def __repr__(self):
        return "Cours()"
