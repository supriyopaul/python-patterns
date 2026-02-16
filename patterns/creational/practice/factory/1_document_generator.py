"""
Factory Pattern - Practice Problem 1 (Beginner)
================================================

Document Generator (Simulation)
-------------------------------

A company needs a system that produces different doctypes of documents.
The system should be able to generate invoices, reports, and letters.
"Generating" a document simply means returning a string describing itself.

The user provides the doctype of document they need, and the system
returns the appropriate document object.

Requirements:
1.  Define a base `Document` class/interface with a `show()` method.
2.  Create `Invoice`, `Report`, and `Letter` classes that implement `show()`.
    - `show()` should just print or return "I am an Invoice", etc.
3.  Create a `DocumentFactory` with a method `create_document(doctype)`.
    - It returns the correct object based on the input string.
4.  Demonstrate creating all three doctypes and calling `show()` on them.

Constraints & Tips:
- Do not use external libraries.
- Keep it simple: one file, multiple classes.
- Use simple `if/elif/else` in the factory.

Example Output:
---------------
I am an Invoice
I am a Report
I am a Letter
"""
from typing import Protocol

class DocumentFactory(Protocol):
    def show(self):
        pass

def create_document(doctype:str="Letter"): 
    docmap = {
        "Invoice": Invoice,
        "Report": Report,
        "Letter": Letter
    }
    doctypeclass = docmap.get(doctype)
    if doctypeclass: return doctypeclass()
    else: raise ValueError("Invalid doctype")

class Invoice:
    def show(self):
        return "This is a invoice"

class Report:
    def show(self):
        return "This is a report"

class Letter:
    def show(self):
        return "This is a letter"

if __name__ == '__main__':
    print(create_document(doctype="Invoice").show())
    print(create_document(doctype="Letter").show())
    print(create_document(doctype="Report").show())
    print(create_document(doctype="Xyz").show())
