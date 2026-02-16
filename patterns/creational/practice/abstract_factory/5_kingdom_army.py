"""
Abstract Factory Pattern - Practice Problem 5 (Expert)
=======================================================

Kingdom Army Generator (Simulation)
-----------------------------------

A strategy game has two factions: Elves and Orcs.
Each faction has a complete army hierarchy:
- Infantry (ElfWarrior vs OrcGrunt)
- Archer (ElfRanger vs OrcSniper)
- Mage (ElfWizard vs OrcShaman)
- Siege (ElfBallista vs OrcCatapult)

We need to generate complete armies for a battle simulation.

Requirements:
1.  Design a highly extensible Abstract Factory system for creating army units.
2.  The client should be able to say "Create a Squad of 5 Infantry and 2 Archers"
    and the factory should produce the correct racial units.
3.  Bonus: Implement a generic `ArmyBuilder` that takes the generic factory
    and constructs a list of units based on a configuration.

Constraints & Tips:
- This combines Abstract Factory with a Builder-like usage in the client.
- The key challenge is maintaining the type consistency across a rigorous hierarchy.

Example Output:
---------------
Forming Elf Squad...
Created ElfWarrior
Created ElfWarrior
Created ElfRanger
Squad ready!
"""
