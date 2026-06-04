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

### 3. Les étapes (steps)

Chaque job est découpé en **étapes** qui s'exécutent dans l'ordre.

```yaml
steps:
  - name: Récupérer le code
    uses: actions/checkout@v4

  - name: Installer les dépendances
    run: npm install

  - name: Lancer les tests
    run: npm test

  - name: Publier le site
    run: npm run build
```

## Le schéma complet

```
git push
   │
   ▼
GitHub détecte le push
   │
   ▼
Workflow déclenché
   │
   ▼
Une machine virtuelle démarre
   │
   ▼
Les étapes s'exécutent dans l'ordre
   │
   ▼
✅ Succès → site publié
❌ Échec  → on est prévenu, rien n'est publié
```

!!! info "Les GitHub Actions"

    Chaque étape peut utiliser une **Action** toute faite, partagée par la communauté. Par exemple `actions/checkout@v4` récupère automatiquement le code du projet. On n'a pas besoin de tout recoder soi-même.
