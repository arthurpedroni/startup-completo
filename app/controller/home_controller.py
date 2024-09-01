from flask import Blueprint, render_template
from app.model.category import Category
from app.model.product import Product

home_bp = Blueprint('home', __name__)

categories = [Category(1, "Eletrônicos"), Category(2, "Livros"), Category(3, "Outros")]
products = [
    Product(1, "EduCat AI", "Estudantes enfrentam dificuldades com métodos de aprendizado tradicionais, que muitas vezes não atendem às suas necessidades e estilos individuais.", "Uma plataforma de aprendizado personalizada que adapta o conteúdo e o ritmo de estudo para cada aluno, maximizando a retenção de conhecimento.", "contact@educatai.com", "No mundo atual, os métodos tradicionais de ensino frequentemente falham em atender às necessidades únicas de cada aluno. Com o EduCat AI, estamos revolucionando o aprendizado ao oferecer uma plataforma personalizada que adapta o conteúdo e o ritmo de estudo para cada estudante. Ao combinar inteligência artificial com metodologias pedagógicas avançadas, garantimos que cada aluno receba a atenção e os recursos necessários para maximizar sua retenção e sucesso acadêmico. EduCat AI não é apenas uma plataforma de aprendizado; é o futuro da educação personalizada."
    ),
    Product(2, "MindGuide", "Acesso limitado a suporte de saúde mental, especialmente em momentos de necessidade urgente, e estigmatização da busca por ajuda profissional.", "Um assistente virtual que oferece suporte emocional instantâneo e discreto, utilizando técnicas de terapia para ajudar na gestão de saúde mental", "support@mindguide.com", "A saúde mental é fundamental, mas muitos enfrentam dificuldades para encontrar suporte quando mais precisam. O MindGuide é um assistente virtual que oferece suporte emocional instantâneo e discreto, utilizando técnicas de terapia comprovadas para ajudar na gestão da saúde mental. Disponível 24/7, o MindGuide quebra o estigma e oferece um espaço seguro e acessível para todos que precisam de ajuda. Com o MindGuide, o apoio emocional está sempre ao seu alcance, quando você mais precisa."        "https://blog.geekhunter.com.br/wp-content/uploads/2020/08/livros-de-python.jpg",
    ),
    Product(3, "Action Figure Spider-Man", 29.95, 3, "Boneco articulado do Spider-Man, perfeito para colecionadores.", [
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
    ]),
    Product(4, "Carro Hot Wheels", 9.99, 3, "Carro Hot Wheels edição limitada, modelo esportivo.", [
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
    ]),
    Product(5, "Mouse Gamer RGB", 35.00, 3, "Mouse gamer com iluminação RGB e alta precisão.", [
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
    ]),
    Product(6, "Cadeira de Escritório Ergonômica", 189.99, 3, "Cadeira de escritório ergonômica com suporte lombar ajustável.", [
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
    ])
]

@home_bp.route('/')
def home():
    return render_template('index.html', categories=categories, products=Product.all_products)
