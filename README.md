# AI Recommendation Logic

This project is a simple recommendation system that matches user interests with item categories.

## How it works

- The user enters interests such as `technology`, `science`, or `fitness`.
- Each item has a list of tags.
- The engine calculates how many interests overlap with each item's tags.
- Items with the most matches are shown first.

## Run the app

```bash
c:/python313/python.exe recommendation_system.py
```

## Run the tests

```bash
c:/python313/python.exe -m pytest -q
```

## Example

If the user enters:

```text
technology, science
```

Then items matching those tags will rise to the top of the recommendation list.
