class Product:
    all_products = []  # Define all_products as a class attribute

    def __init__(self, id, name, problema, solucao, email, pitch):
        self.id = id
        self.name = name
        self.problema = problema
        self.solucao = solucao
        self.email = email
        self.pitch = pitch  # List of image URLs

        # Add this product instance to the class-wide list of all products
        Product.all_products.append(self)
