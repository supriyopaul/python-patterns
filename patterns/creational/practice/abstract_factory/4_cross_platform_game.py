"""
Abstract Factory Pattern - Practice Problem 4 (Advanced)
=========================================================

Cross-Platform Game (Simulation)
--------------------------------

A game engine needs to render assets (Sprites, Sounds) differently on
PC and Console platforms.

- PC: HighResSprite, WavSound
- Console: CompressedSprite, OggSound

Requirements:
1.  Design a system where the game loop can request assets without knowing
    the current platform.
2.  Each platform should have its own factory responsible for creating
    its specific assets.
3.  The "Game" class should be initialized with a factory and use it
    to load resources.

Constraints & Tips:
- Think about extensibility: How hard would it be to add a "Mobile" platform?
- Ensure the game logic remains platform-agnostic.

Example Output:
---------------
Loading PC Game...
Rendering HighRes Sprite
Playing Wav Sound
"""
