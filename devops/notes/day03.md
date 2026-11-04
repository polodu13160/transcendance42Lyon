Exercice 1:

J'ai mis les env qui permette de creer un login et un mdp dans les env:
```bash
GF_SECURITY_ADMIN_USER=jojo
GF_SECURITY_ADMIN_PASSWORD=mdp42
```

Petit problème lors de la création d'un volume. En effet lorsque je fais un bind mount il n'y a pas les permissions sur le dossier du volume donc je ne peux pas écrire dessus.
Il faut soit faire un volume nommé soit (dans mon cas car je suis en rrotless sur les ordi de 42) je mets `0:0` en user car le root du container correspond à mon user réel sur l'hôte.
