"""
Abstract Factory Pattern - Practice Problem 3 (Intermediate)
=============================================================

Pizza Ingredient Factory (Simulation)
-------------------------------------

A pizza chain has stores in New York and Chicago.
Each region uses different ingredients for the same pizza components:
- Dough: ThinCrust vs ThickCrust
- Sauce: Marinara vs PlumTomato
- Cheese: Reggiano vs Mozzarella

We need to ensure that a NY store *always* uses NY ingredients.

Requirements:
1.  Create an `IngredientFactory` interface that creates Dough, Sauce, and Cheese.
2.  Implement `NYIngredientFactory` and `ChicagoIngredientFactory`.
3.  The client (a `PizzaStore`) should take a factory and use it to create
    ingredients for a pizza.
4.  Demonstrate preparing a pizza using the NY factory.

Constraints & Tips:
- Notice how the Factory abstracts the *source* of the ingredients.
- The `Pizza` class doesn't care which factory gave it the dough.

Example Output:
---------------
Preparing Pizza...
Tossing ThinCrust Dough
Adding Marinara Sauce
Adding Reggiano Cheese
"""
