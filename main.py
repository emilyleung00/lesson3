from typing import Tuple

class IKEAFurniture:
    def __init__(self, name, product_id, price, category, is_assembled,
                 package_dimension, package_weight, has_stock,
                 shipping_method):
        """
        Initialize an IKEA furniture item.

        Args:
            name (str): The name of the furniture item
            product_id (str): Unique product identifier
            price (float): Price of the furniture item
            category (str): Category of furniture (e.g., 'Chair', 'Table', 'Bed')
            is_assembled (bool, optional): Whether the furniture is pre-assembled. Defaults to False.
            package_dimension (dict, optional): Dimensions of the package in cm. Defaults to None.
                Example: {'length': 120, 'width': 80, 'height': 20}
            package_weight (float, optional): Weight of the package in kg. Defaults to None.
            has_stock (bool, optional): Whether the item is in stock. Defaults to True.
            shipping_method (str, optional): Shipping method for the item (e.g., 'Home Delivery', 'Click & Collect'). Defaults to None.
        """
        self.name: str = name
        self.product_id: str = product_id
        self.price: float = price
        self.category: str = category
        self.is_assembled: bool = True
        self.package_dimension: Tuple[float,float,float] = package_dimension  # (length, width, height) in cm
        self.package_weight: float = package_weight #in kg
        self.has_stock: bool = True
        self.shipping_method: str = shipping_method

from typing import Tuple

class IkeaCabinet(IKEAFurniture):
    def __init__(self, name, product_id, price,
                 is_assembled, package_dimension,
                 package_weight, has_stock, shipping_method,
                 num_shelves, with_door, color,
                 with_lock, width, depth, height, max_load, extra_options):
        """
        Initialize an IKEA cabinet furniture item.

        Args:
            name (str): The name of the cabinet
            product_id (str): Unique product identifier
            price (float): Price of the cabinet
            is_assembled (bool): Whether the furniture is pre-assembled
            package_dimension (Tuple[float, float, float]): Dimensions (length, width, height) in cm
            package_weight (float): Weight of the package in kg
            has_stock (bool): Whether the item is in stock
            shipping_method (str): Shipping method for the item
            with_door (bool)
            num_shelves (int): Number of shelves in the cabinet
            color (str): Color of the cabinet
            with_lock (bool): Whether the cabinet has a lock. Defaults to False.
        """
        super().__init__(name, product_id, price, "Cabinet", is_assembled,
                         package_dimension, package_weight, has_stock, shipping_method)
        self.num_shelves: int = num_shelves
        self.with_door: bool = True
        self.with_lock: bool = False
        self.color: str = color
        self.width: float = width
        self.depth: float = depth
        self.height: float = height
        self.max_load: float = max_load #in kg
        self.extra_options = []

from typing import Tuple

class IkeaChair(IKEAFurniture):
    def __init__(self, name, product_id, price,
                 is_assembled, package_dimension,
                 package_weight, has_stock, shipping_method,
                 material, color, has_armrests,
                 is_adjustable, width, depth,
                 height, seat_height, back_type, max_load, is_rolling, cushion_attached,
                 extra_options):
        """
        Initialize an IKEA chair furniture item.

        Args: (originally suggested by LLM)
            name (str): The name of the chair
            product_id (str): Unique product identifier
            price (float): Price of the chair
            is_assembled (bool): Whether the furniture is pre-assembled
            package_dimension (Tuple[float, float, float]): Dimensions (length, width, height) in cm
            package_weight (float): Weight of the package in kg
            has_stock (bool): Whether the item is in stock
            shipping_method (str): Shipping method for the item
            material (str): Material of the chair (e.g., "Wood", "Plastic", "Metal", "Fabric")
            color (str): Color of the chair
            has_armrests (bool): Whether the chair has armrests
            is_adjustable (bool): Whether the chair height is adjustable
            width (float): Width of the chair in cm
            depth (float): Depth of the chair in cm
            height (float): Height of the chair in cm
            seat_height (float): Height of the seat from the ground in cm
            max_load (float): Maximum weight capacity in kg
            extra_options (List[str]): Additional features of the chair
        """
        super().__init__(name, product_id, price, "Chair", is_assembled,
                         package_dimension, package_weight, has_stock, shipping_method)
        self.material: str = material
        self.color: str = color
        self.has_armrests: bool = True
        self.is_adjustable: bool = True
        self.width: float = width
        self.depth: float = depth
        self.height: float = height
        self.seat_height: float = seat_height
        self.back_type: list = 0 #0 = no back, 1 = low back, 2 = high back
        self.max_load: float = max_load  # in kg
        self.is_rolling: bool = False
        self.cushion_attached: bool = False
        self.extra_options = []

    def __repr__(self): #override __repr__, __str__
        return(f"{self.name} - {self.material} - ${self.price}")
    
from typing import Tuple

class IkeaDesk(IKEAFurniture):
    def __init__(self, name, product_id, price,
                 is_assembled, package_dimension,
                 package_weight, has_stock, shipping_method,
                 material, color, desk_type,
                 is_adjustable, width, depth,
                 min_height, max_height, max_load, num_drawers,
                 cable_management, surface_treatment, legs_type,is_folded,
                 extra_options):
        """
        Initialize an IKEA desk furniture item.

        Args: (originally suggested by LLM)
            name (str): The name of the desk
            product_id (str): Unique product identifier
            price (float): Price of the desk
            is_assembled (bool): Whether the furniture is pre-assembled
            package_dimension (Tuple[float, float, float]): Dimensions (length, width, height) in cm
            package_weight (float): Weight of the package in kg
            has_stock (bool): Whether the item is in stock
            shipping_method (str): Shipping method for the item
            material (str): Material of the desk (e.g., "Wood", "Particleboard", "Metal")
            color (str): Color of the desk
            desk_type (str): Type of desk (e.g., "Computer desk", "Standing desk", "Corner desk")
            is_adjustable (bool): Whether the desk height is adjustable
            width (float): Width of the desk in cm
            depth (float): Depth of the desk in cm
            height (float): Height of the desk in cm
            max_load (float): Maximum weight capacity in kg
            has_drawers (bool): Whether the desk has drawers
            num_drawers (int): Number of drawers
            cable_management (bool): Whether the desk has cable management features
            surface_treatment (str): Treatment applied to the surface (e.g., "Lacquer", "Veneer", "Laminate")
            legs_type (str): Type of legs (e.g., "4-legged", "Trestle", "Cabinet")
            extra_options (List[str]): Additional features of the desk
        """
        super().__init__(name, product_id, price, "Desk", is_assembled,
                         package_dimension, package_weight, has_stock, shipping_method)
        self.material: str = material
        self.color: str = color
        self.desk_type: str = desk_type
        self.is_adjustable: bool = is_adjustable
        self.width: float = width
        self.depth: float = depth
        self.min_height: float = min_height
        self.max_height: float = max_height
        self.max_load: float = max_load  # in kg
        self.num_drawers: int = num_drawers
        self.cable_management: bool = cable_management
        self.surface_treatment: str = surface_treatment
        self.legs_type: str = legs_type
        self.is_folded: bool = is_folded  # For foldable desks
        self.extra_options = []

# Creating 15 sample cabinet records
cabinet_samples = [
    # 1. BILLY Bookcase with doors
    {
        "name": "BILLY Bookcase with doors",
        "product_id": "992.873.74",
        "price": 159.99,
        "is_assembled": False,
        "package_dimension": (80.0, 28.0, 202.0),
        "package_weight": 41.2,
        "has_stock": True,
        "shipping_method": "Home Delivery",
        "num_shelves": 5,
        "with_door": True,
        "color": "White",
        "with_lock": False,
        "width": 80.0,
        "depth": 28.0,
        "height": 202.0,
        "max_load": 30.0,
        "extra_options": ["Adjustable shelves", "Tempered glass doors"]
    },

    # 2. BRIMNES Cabinet with doors
    {
        "name": "BRIMNES Cabinet with doors",
        "product_id": "804.098.85",
        "price": 129.99,
        "is_assembled": False,
        "package_dimension": (78.0, 41.0, 95.0),
        "package_weight": 34.5,
        "has_stock": True,
        "shipping_method": "Home Delivery",
        "num_shelves": 3,
        "with_door": True,
        "color": "Black",
        "with_lock": False,
        "width": 78.0,
        "depth": 41.0,
        "height": 95.0,
        "max_load": 25.0,
        "extra_options": ["Adjustable shelves"]
    },

    # 3. PAX Wardrobe
    {
        "name": "PAX Wardrobe",
        "product_id": "192.483.77",
        "price": 349.00,
        "is_assembled": False,
        "package_dimension": (201.0, 60.0, 236.0),
        "package_weight": 78.5,
        "has_stock": True,
        "shipping_method": "Home Delivery",
        "num_shelves": 6,
        "with_door": True,
        "color": "White oak effect",
        "with_lock": False,
        "width": 150.0,
        "depth": 60.0,
        "height": 236.0,
        "max_load": 75.0,
        "extra_options": ["Mirror doors", "Soft-closing hinges", "Built-in lighting"]
    },

    # 4. HEMNES Cabinet with panel/glass door
    {
        "name": "HEMNES Cabinet with panel/glass door",
        "product_id": "504.135.03",
        "price": 249.00,
        "is_assembled": False,
        "package_dimension": (90.0, 37.0, 197.0),
        "package_weight": 47.0,
        "has_stock": True,
        "shipping_method": "Home Delivery",
        "num_shelves": 4,
        "with_door": True,
        "color": "Dark gray stained",
        "with_lock": True,
        "width": 90.0,
        "depth": 37.0,
        "height": 197.0,
        "max_load": 30.0,
        "extra_options": ["Solid wood", "Adjustable shelves", "Glass doors"]
    },

    # 5. LIXHULT Cabinet
    {
        "name": "LIXHULT Cabinet",
        "product_id": "203.996.60",
        "price": 34.99,
        "is_assembled": False,
        "package_dimension": (60.0, 35.0, 35.0),
        "package_weight": 8.5,
        "has_stock": True,
        "shipping_method": "Click & Collect",
        "num_shelves": 1,
        "with_door": True,
        "color": "Red",
        "with_lock": True,
        "width": 35.0,
        "depth": 35.0,
        "height": 35.0,
        "max_load": 15.0,
        "extra_options": ["Metal", "Stackable"]
    },

    # 6. IVAR Cabinet with doors
    {
        "name": "IVAR Cabinet with doors",
        "product_id": "903.815.93",
        "price": 89.00,
        "is_assembled": False,
        "package_dimension": (80.0, 30.0, 83.0),
        "package_weight": 16.0,
        "has_stock": True,
        "shipping_method": "Home Delivery",
        "num_shelves": 2,
        "with_door": True,
        "color": "Pine",
        "with_lock": False,
        "width": 80.0,
        "depth": 30.0,
        "height": 83.0,
        "max_load": 40.0,
        "extra_options": ["Solid wood", "Untreated wood", "Customizable"]
    },

    # 7. BESTÅ Storage combination with doors
    {
        "name": "BESTÅ Storage combination with doors",
        "product_id": "692.076.44",
        "price": 179.00,
        "is_assembled": False,
        "package_dimension": (120.0, 40.0, 74.0),
        "package_weight": 53.0,
        "has_stock": True,
        "shipping_method": "Home Delivery",
        "num_shelves": 4,
        "with_door": True,
        "color": "White/Selsviken high-gloss",
        "with_lock": False,
        "width": 120.0,
        "depth": 40.0,
        "height": 74.0,
        "max_load": 50.0,
        "extra_options": ["Push-open function", "Soft-closing"]
    },

    # 8. GALANT Cabinet with doors
    {
        "name": "GALANT Cabinet with doors",
        "product_id": "303.651.36",
        "price": 249.00,
        "is_assembled": False,
        "package_dimension": (80.0, 45.0, 120.0),
        "package_weight": 45.0,
        "has_stock": False,  # Out of stock
        "shipping_method": "Home Delivery",
        "num_shelves": 3,
        "with_door": True,
        "color": "White",
        "with_lock": True,
        "width": 80.0,
        "depth": 45.0,
        "height": 120.0,
        "max_load": 60.0,
        "extra_options": ["10-year warranty", "Office use", "Lockable"]
    },

    # 9. EKET Cabinet
    {
        "name": "EKET Cabinet",
        "product_id": "903.321.26",
        "price": 44.99,
        "is_assembled": False,
        "package_dimension": (35.0, 35.0, 35.0),
        "package_weight": 7.5,
        "has_stock": True,
        "shipping_method": "Click & Collect",
        "num_shelves": 0,
        "with_door": True,
        "color": "Light blue",
        "with_lock": False,
        "width": 35.0,
        "depth": 35.0,
        "height": 35.0,
        "max_load": 15.0,
        "extra_options": ["Wall-mountable", "Stackable", "Combinable"]
    },

    # 10. HAVSTA Cabinet with plinth
    {
        "name": "HAVSTA Cabinet with plinth",
        "product_id": "404.151.92",
        "price": 179.00,
        "is_assembled": False,
        "package_dimension": (81.0, 37.0, 134.0),
        "package_weight": 39.0,
        "has_stock": True,
        "shipping_method": "Home Delivery",
        "num_shelves": 3,
        "with_door": True,
        "color": "Gray",
        "with_lock": False,
        "width": 81.0,
        "depth": 37.0,
        "height": 134.0,
        "max_load": 35.0,
        "extra_options": ["Solid wood", "Traditional style", "Adjustable shelves"]
    },

    # 11. METOD Wall cabinet
    {
        "name": "METOD Wall cabinet",
        "product_id": "902.056.31",
        "price": 79.99,
        "is_assembled": False,
        "package_dimension": (60.0, 38.0, 80.0),
        "package_weight": 16.5,
        "has_stock": True,
        "shipping_method": "Home Delivery",
        "num_shelves": 2,
        "with_door": True,
        "color": "White/Bodbyn green",
        "with_lock": False,
        "width": 60.0,
        "depth": 38.0,
        "height": 80.0,
        "max_load": 22.0,
        "extra_options": ["Kitchen series", "25-year warranty"]
    },

    # 12. KALLAX Shelf unit with doors
    {
        "name": "KALLAX Shelf unit with doors",
        "product_id": "892.783.96",
        "price": 114.99,
        "is_assembled": False,
        "package_dimension": (77.0, 39.0, 147.0),
        "package_weight": 34.0,
        "has_stock": True,
        "shipping_method": "Home Delivery",
        "num_shelves": 8,
        "with_door": True,
        "color": "Black-brown",
        "with_lock": False,
        "width": 77.0,
        "depth": 39.0,
        "height": 147.0,
        "max_load": 13.0,
        "extra_options": ["Square compartments", "Customizable with inserts"]
    },

    # 13. FJÄLLBO Cabinet
    {
        "name": "FJÄLLBO Cabinet",
        "product_id": "703.392.78",
        "price": 129.00,
        "is_assembled": False,
        "package_dimension": (81.0, 42.0, 122.0),
        "package_weight": 28.5,
        "has_stock": True,
        "shipping_method": "Home Delivery",
        "num_shelves": 2,
        "with_door": True,
        "color": "Black",
        "with_lock": False,
        "width": 81.0,
        "depth": 42.0,
        "height": 122.0,
        "max_load": 35.0,
        "extra_options": ["Metal and solid wood", "Industrial style", "Mesh doors"]
    },

    # 14. IDÅSEN Cabinet with doors and drawers
    {
        "name": "IDÅSEN Cabinet with doors and drawers",
        "product_id": "503.207.27",
        "price": 299.00,
        "is_assembled": False,
        "package_dimension": (80.0, 47.0, 119.0),
        "package_weight": 52.0,
        "has_stock": True,
        "shipping_method": "Home Delivery",
        "num_shelves": 2,
        "with_door": True,
        "color": "Beige",
        "with_lock": True,
        "width": 80.0,
        "depth": 47.0,
        "height": 119.0,
        "max_load": 45.0,
        "extra_options": ["Drawers", "10-year warranty", "Lockable", "Office series"]
    },

    # 15. KOLBJÖRN Cabinet
    {
        "name": "KOLBJÖRN Cabinet",
        "product_id": "304.092.94",
        "price": 119.00,
        "is_assembled": False,
        "package_dimension": (80.0, 35.0, 81.0),
        "package_weight": 23.0,
        "has_stock": False,  # Out of stock
        "shipping_method": "Click & Collect",
        "num_shelves": 1,
        "with_door": True,
        "color": "Green",
        "with_lock": False,
        "width": 80.0,
        "depth": 35.0,
        "height": 81.0,
        "max_load": 25.0,
        "extra_options": ["Indoor/outdoor use", "Metal", "Adjustable feet"]
    }
]

# Example of how to create IkeaCabinet objects from the dictionary data
# (Uncomment and use this if you need to convert back to objects)
"""
cabinet_objects = []
for cabinet_data in cabinet_samples:
    cabinet = IkeaCabinet(**cabinet_data)
    cabinet_objects.append(cabinet)
"""

# Example of how to print some information from the dictionary list
for i, cabinet in enumerate(cabinet_samples, 1):
    print(f"{i}. {cabinet['name']} - ${cabinet['price']:.2f} - {cabinet['color']}")

IkeaCabinet(*cabinet_samples[0])

cabinet_objects = [] # create a list for objects
for cabinet_data in cabinet_samples:
    cabinet = IkeaCabinet(**cabinet_data) # unpack and init
    cabinet_objects.append(cabinet)  # Add objects to the list using append

# After this change cabinet_objects will be a list of IkeaCabinet object
print(cabinet_objects[0].price) # then you can access price

cabinet_samples[2]["price"]
print(cabinet_samples[2]["price"])

