from data_extraction import DataExtraction
from data_processing import DataProcessing
from user_interaction import UserInteraction
from voice_processing import VoiceProcessing
from flask import Flask

def create_app():
    # Créez l'application Flask ici
    app = UserInteraction.app

    # Extraire les données
    soup = DataExtraction.fetch_data("https://www.tunisianet.com.tn/681-pc-portable-gamer")
    products_title, products_reference, products_description, products_prices, products_graphics = DataExtraction.extract_products(soup)

    # Traiter les données
    metadescription1 = [
    'movie', 'movies', 'watching', 'media', 'word', 'excel', 
    'presentations', 'music', 'videos', 'old', 'games', 'studying', 
    'simple', 'tasks', 'browsing', 'emails', 'office', 'homework', 
    'reading', 'streaming', 'light', 'work', 'children', 'school'
    ]
    metadescription2 = [
    'movie', 'movies', 'watching', 'media', 'art', 'games', 'modeling', 
    'word', 'excel', 'presentations', 'music', 'videos', 'new', 'games', 
    'design', '3d', 'ai', 'development', 'studying', 'heavy', 'tasks', 
    'projects', 'gaming', 'programming', 'editing', 'rendering', 'virtual', 
    'reality', 'simulation', 'data', 'science', 'machine', 'learning', 
    'deep', 'learning', 'animation', 'coding', 'engineering', 'production', 
    'video', 'processing'
    ]

    all_products = DataProcessing.prepare_dataset(products_title, products_reference, products_description, products_prices, products_graphics)
    classified_products = DataProcessing.classify_products(all_products, metadescription1, metadescription2)

    # Passer les données traitées à l'application Flask
    UserInteraction.classified_products = classified_products

    @app.route('/turnmic')
    def turn_mic():
        # Appeler la fonction de traitement vocal
        return VoiceProcessing.record_voice()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=80)
