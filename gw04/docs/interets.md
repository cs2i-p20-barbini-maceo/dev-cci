---
icon: lucide/star
---

# Quels sont leurs intérêts ?

## Gagner du temps

Sans workflow, chaque mise en ligne d'un site demande plusieurs étapes manuelles : tester, construire, publier, vérifier... Avec un workflow, tout ça se fait en un seul `git push`. Ce qui prenait 15 minutes se fait en 2 minutes, sans rien toucher.

## Éviter les erreurs humaines

Quand on répète les mêmes gestes tous les jours, on finit par en oublier un. Avec un workflow, les étapes sont toujours les mêmes, dans le même ordre, sans exception.

!!! warning "Sans automatisation"

    "Oups, j'ai oublié de lancer les tests avant de publier... et maintenant le site est cassé."

!!! success "Avec un workflow"

    Le workflow refuse automatiquement de publier si les tests échouent. Le site ne peut pas partir en production cassé.

## Travailler en équipe plus sereinement

Quand plusieurs personnes modifient le même projet, les workflows vérifient automatiquement que chaque modification ne casse rien pour les autres. C'est essentiel dans une équipe.

## Avoir un historique de tout

Chaque exécution d'un workflow est enregistrée sur GitHub. Tu peux voir exactement ce qui s'est passé, quand, et pourquoi ça a réussi ou échoué.

> C'est comme un journal de bord automatique de tout ce qui a été fait sur le projet.

## En résumé

| Sans workflow | Avec workflow |
|---------------|---------------|
| Tâches manuelles et répétitives | Tout est automatisé |
| Risque d'oubli ou d'erreur | Toujours les mêmes étapes |
| Long à mettre en production | Déploiement en quelques secondes |
| Pas de filet de sécurité | Tests automatiques avant publication |
