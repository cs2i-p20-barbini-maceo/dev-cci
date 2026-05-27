---
icon: lucide/table
---

# Tableaux

Un tableau se construit avec des `|` pour séparer les colonnes et des `-` pour la ligne d'en-tête.

=== "Exemple"

    ```markdown
    | Langage    | Type        | Créé en |
    |------------|-------------|---------|
    | Markdown   | Balisage    | 2004    |
    | Python     | Programmation | 1991  |
    | JavaScript | Programmation | 1995  |
    ```

=== "Résultat"

    | Langage    | Type          | Créé en |
    |------------|---------------|---------|
    | Markdown   | Balisage      | 2004    |
    | Python     | Programmation | 1991    |
    | JavaScript | Programmation | 1995    |

## Alignement

On peut aligner le contenu des colonnes avec `:`.

=== "Exemple"

    ```markdown
    | Gauche  | Centre  | Droite  |
    |:--------|:-------:|--------:|
    | A       | B       | C       |
    | 1       | 2       | 3       |
    ```

=== "Résultat"

    | Gauche  | Centre  | Droite  |
    |:--------|:-------:|--------:|
    | A       | B       | C       |
    | 1       | 2       | 3       |
