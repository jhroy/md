## :hospital: Données sur les médecins du Québec (1930-2016)

Combien de nouveaux médecins y a-t-il chaque année, au Québec?

Combien de ces nouveaux médecins sont des femmes? Des spécialistes?

Difficile de répondre à ces questions, puisqu'on n'avait pas de données sur le nombre de médecins qui intègrent chaque année la profession médicale. En fait, les données sont là, mais difficilement accessibles. 

Où se trouvent-elles, ces données? Sur le site web du [Collège des médecins](http://www.cmq.org/). Plus précisément, dans le [**Bottin des membres du Collège des médecins du Québec**](http://www.cmq.org/bottin/index.aspx?lang=fr&a=1).

Maintenant, comment ce Bottin peut-il nous permettre de compter le nombre de nouveaux médecins qui ont intégré la profession à chaque année? C'est chaque médecin a un numéro de permis à cinq chiffres. Les deux premiers chiffres désignent l'année à laquelle il ou elle est devenu.e membre du Collège. Le premier ministre Philippe Couillard, par exemple, a le numéro de permis **80244**. Cela signifie donc qu'il a obtenu le droit de pratiquer la médecine en 1980.

À partir de cela, comment est-il possible de compter tous les médecins dont le numéro de permis commence par 80? La seule façon est de faire des recherches dans le [Bottin](http://www.cmq.org/bottin/index.aspx?lang=fr&a=1) afin de vérifier tous les numéros de permis possibles entre 80001 et 80999. Il faut donc faire 999 recherches par année. Et si on s'intéresse à un intervalle plus grand, comme de 1930 à 2017, par exemple, il faut faire 86&nbsp;913 recherches!

Imaginez le temps que cela prendrait s'il fallait effectuer ces recherches à la main!

Le fichier [**md.py**](md.py) est un script python qui fait ce travail automatiquement. Quand un numéro était valide, les informations relatives au médecin en question (genre, spécialité, etc.) étaient copiées dans un fichier CSV. Celui-ci est reproduit dans le fichier [**cmq-total.csv**](cmq-total.csv), après avoir anonymisé les données (noms et prénoms ont été remplacés par une initiale). Ces données donnent un portrait jusqu'à présent inédit de l'évolution de la profession médicale au Québec depuis près d'un siècle.

Travail réalisé dans le cadre d'un projet pour... [Nouveau projet](http://edition.atelier10.ca/nouveau-projet).
