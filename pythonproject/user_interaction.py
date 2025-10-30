from flask import Flask, render_template, request
from data_processing import DataProcessing
from user import createUser  # Assurez-vous que cette importation est correcte

class UserInteraction:
    app = Flask(__name__)

    # Variable globale pour les produits classifiés
    classified_products = {}

    @staticmethod
    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/submit", methods=["POST", "GET"])
    def create_profile():
        # Récupérez les données de l'utilisateur à partir de la requête POST
        user_data = request.form  # Par exemple, si les données sont envoyées via un formulaire
        new_user = createUser(user_data)  # Créez un objet `new_user` à partir des données de l'utilisateur

        # Vérifiez la valeur de ramtype avant de procéder
        ramtype = new_user.graphics_requirement

        # Vérifiez que ramtype n'est pas None et existe dans classified_products
        if ramtype is not None and ramtype in UserInteraction.classified_products:
            # Appelez la fonction check_user_description pour obtenir l'index et ramtype
            index, ramtype = DataProcessing.check_user_description(new_user, UserInteraction.classified_products, ramtype)

            # Vérifiez si l'index est valide avant d'accéder à classified_products
            if index is not None:
                # Récupérez le produit sélectionné à partir de classified_products
                selected_product = UserInteraction.classified_products[ramtype][index]
                # Vous pouvez ajouter ici le processus que vous souhaitez effectuer avec selected_product
                print(f"Produit sélectionné: {selected_product}")
            else:
                print("Erreur: Aucune correspondance trouvée pour l'utilisateur.")
                selected_product = None
        else:
            # Si ramtype est invalide ou None, affichez un message d'erreur
            print(f"Erreur: ramtype '{ramtype}' est invalide ou None.")
            selected_product = None

        # Vous pouvez également retourner selected_product si nécessaire
        return selected_product

# Pour démarrer l'application Flask
if __name__ == "__main__":
    UserInteraction.app.run(debug=True)
