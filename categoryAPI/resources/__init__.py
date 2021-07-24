from .categories import Categories
from .category import Category

ROUTES_MAP = [
  {"route": "/<int:category_id>", "resource": Category},
  {"route": "/", "resource": Categories}
]
