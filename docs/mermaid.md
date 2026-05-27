---
icon: lucide/workflow
---

# Mermaid

Mermaid permet de créer des diagrammes directement en Markdown.

## Diagramme de flux

=== "Exemple"

    ````markdown
    ```mermaid
    graph LR
      A[Départ] --> B{Erreur ?};
      B -->|Oui| C[Corriger];
      C --> B;
      B -->|Non| D[Succès];
    ```
    ````

=== "Résultat"

    ```mermaid
    graph LR
      A[Départ] --> B{Erreur ?};
      B -->|Oui| C[Corriger];
      C --> B;
      B -->|Non| D[Succès];
    ```

## Diagramme de séquence

=== "Exemple"

    ````markdown
    ```mermaid
    sequenceDiagram
      Client->>Serveur: Requête GET /api
      Serveur-->>Client: Réponse 200 OK
    ```
    ````

=== "Résultat"

    ```mermaid
    sequenceDiagram
      Client->>Serveur: Requête GET /api
      Serveur-->>Client: Réponse 200 OK
    ```
