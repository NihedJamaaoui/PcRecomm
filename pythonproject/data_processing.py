# import numpy as np
# import re

# class DataProcessing:
#     @staticmethod
#     def prepare_dataset(products_title, products_reference, products_description, products_prices):
#         products = []
#         for title, ref, desc, price in zip(products_title, products_reference, products_description, products_prices):
#             p = price.text[0:price.text.find(',')]
#             p = "".join(p.split())
#             products.append({
#                 "product_name": title.text,
#                 "product_reference": ref.text,
#                 "product_desc": desc.text,
#                 "price": int(p)
#             })
#         return np.array(products)

#     @staticmethod
#     def classify_products(products, metadescription1, metadescription2):
#         classified_products = {'Ram8G': [], 'SupRam16G': []}
#         for product in products:
#             if re.search("8 Go", product['product_desc']):
#                 product['metadata'] = ' '.join(metadescription1)
#                 classified_products['Ram8G'].append(product)
#             else:
#                 product['metadata'] = ' '.join(metadescription2)
#                 classified_products['SupRam16G'].append(product)
#         return classified_products

#     @staticmethod
#     def check_user_description(user, classified_products):
#         accuracy_table = {'Ram8G': [], 'SupRam16G': []}
#         for ramtype in classified_products:
#             for product in classified_products[ramtype]:
#                 accuracy_value = 0
#                 user_text = user.description.lower().split(" ")
#                 for word in user_text:
#                     if re.search(word, product['product_desc'].lower()) or re.search(word, product['metadata']):
#                         accuracy_value += 1
#                 accuracy_table[ramtype].append(accuracy_value)
#         ramtype = 'Ram8G' if max(accuracy_table['Ram8G'], default=0) > max(accuracy_table['SupRam16G'], default=0) else 'SupRam16G'
#         index = accuracy_table[ramtype].index(max(accuracy_table[ramtype], default=0))
#         return index, ramtype

import numpy as np
import re

class DataProcessing:
    @staticmethod
    def prepare_dataset(products_title, products_reference, products_description, products_prices, products_graphics):
        products = []
        for title, ref, desc, price, graphics in zip(products_title, products_reference, products_description, products_prices, products_graphics):
            p = price.text[0:price.text.find(',')]
            p = "".join(p.split())
            products.append({
                "product_name": title.text,
                "product_reference": ref.text,
                "product_desc": desc.text,
                "price": int(p),
                "graphics": graphics.text.strip()  # Storing graphics card info
            })
        return np.array(products)

    @staticmethod
    def classify_products(products, metadescription1, metadescription2):
        classified_products = {'Ram8G': [], 'SupRam16G': []}
        for product in products:
            if re.search("8 Go", product['product_desc']):
                product['metadata'] = ' '.join(metadescription1)
                classified_products['Ram8G'].append(product)
            else:
                product['metadata'] = ' '.join(metadescription2)
                classified_products['SupRam16G'].append(product)
        return classified_products

    @staticmethod
    def check_user_description(user, classified_products, graphics_requirement):
        accuracy_table = {'Ram8G': [], 'SupRam16G': []}
        for ramtype in classified_products:
            for product in classified_products[ramtype]:
                accuracy_value = 0
                user_text = user.description.lower().split(" ")
                for word in user_text:
                    if re.search(word, product['product_desc'].lower()) or re.search(word, product['metadata']):
                        accuracy_value += 1
                # Adding graphics card matching to accuracy calculation
                if graphics_requirement.lower() in product['graphics'].lower():
                    accuracy_value += 1
                accuracy_table[ramtype].append(accuracy_value)
        
        ramtype = 'Ram8G' if max(accuracy_table['Ram8G'], default=0) > max(accuracy_table['SupRam16G'], default=0) else 'SupRam16G'
        index = accuracy_table[ramtype].index(max(accuracy_table[ramtype], default=0))
        return index, ramtype
