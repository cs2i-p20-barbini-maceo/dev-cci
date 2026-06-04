---
icon: lucide/settings-2
---

# Comment fonctionnent-ils ?

## Un fichier YAML

Un workflow GitHub est simplement un **fichier texte** écrit dans un langage appelé YAML. Ce fichier se range dans un dossier précis de ton projet :

```
mon-projet/
└── .github/
    └── workflows/
        └── mon-workflow.yml   ← c'est ici
```

Dès que GitHub voit ce fichier, il sait qu'il doit l'exécuter selon les règles qu'on y a écrites.

## Les 3 éléments clés

### 1. Le déclencheur (trigger)

C'est **ce qui lance** le workflow. On lui dit : "démarre quand...".

```yaml
on:
  push:
    branches:
      - main
```

> Ici : "Lance-toi à chaque fois que quelqu'un pousse du code sur la branche `main`."

D'autres déclencheurs possibles : à heure fixe, quand on ouvre une Pull Request, manuellement...

### 2. Les jobs

Un workflow contient un ou plusieurs **jobs** (tâches). Chaque job est un ensemble d'étapes qui s'exécutent sur une machine virtuelle fournie par GitHub.

```yaml
jobs:
  deploiement:
    runs-on: ubuntu-latest
```

> `runs-on: ubuntu-latest` signifie : "utilise une machine Linux toute neuve".


