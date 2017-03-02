## :hospital: Données sur les médecins du Québec (1930-2016)

Combien de nouveaux médecins y a-t-il chaque année, au Québec?

Combien de ces nouveaux médecins sont des femmes? Des spécialistes?

Difficile de répondre à ces questions, puisqu'on n'avait pas de données sur le nombre de médecins qui intègrent chaque année la profession médicale. En fait, les données sont là, mais difficilement accessibles.

En effet, chaque médecin a un numéro de permis de cinq chiffres. Les deux premiers chiffres désignent l'année à laquelle il ou elle est devenu.e membre du Collège des médecins. Le premier ministre Philippe Couillard, par exemple, a le numéro de permis **80244**. Cela signifie donc qu'il a intégré le Collège des médecins en 1980.

Mais comment compter tous les médecins dont le numéro de permis commence par 80? La seule façon est de vérifier tous les numéros de permis possibles entre 80001 et 80999 dans le [bottin du Collège des médecins du Québec](http://www.cmq.org/bottin/index.aspx?lang=fr&a=1). Le faire manuellement, pour toutes les années entre 1930 et 2016, serait fastidieux puisqu'il faudrait entrer près de 86&nbsp;000 numéros dans l'outil de recherche du bottin.

Le fichier **md.py** est un script python qui fait ce travail automatiquement.

Les données qu'il permet de recueillir, et qui donnent un portrait inédit de l'évolution de la profession médicale au Québec du dernier siècle, sont colligées dans le fichier **cmq-total.csv**.

Travail réalisé dans le cadre d'un projet pour... [Nouveau projet](http://edition.atelier10.ca/nouveau-projet).
