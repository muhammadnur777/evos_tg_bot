from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from database.db_sqlite import Database
from pprint import pprint

baza = Database(path_to_db="main.sqlite3")


baza.create_category_table()
baza.create_users_table()
baza.create_products_table()
baza.create_orders_table()
baza.create_product_types_table()
baza.create_locations_table()


baza.add_category('Lavash', image_path='images/categories/Lavash.jpg')
baza.add_category('Trindwich', image_path='images/categories/Trindwich.jpg')
baza.add_category('Shaurma', image_path='images/categories/shaurma.jpg')
baza.add_category('Burger', image_path='images/categories/burger.jpg')
baza.add_category('Sub', image_path='images/categories/sub.jpg')
baza.add_category('Kartoshka', image_path='images/categories/kartoshka4.jpg')
baza.add_category('Hot Dog', image_path='images/categories/hot-dog.jpg')
baza.add_category('Sneklar', image_path='images/categories/senki.jpg')
baza.add_category('Salat, garnir, non', image_path='images/categories/salad.jpg')
baza.add_category('Souslar', image_path='images/categories/sause.jpg')
baza.add_category('Setlar', image_path='images/categories/sets.jpg')
baza.add_category('Desertlar', image_path='images/categories/desserts.jpg')
baza.add_category('Issiq ichimliklar', image_path='images/categories/hot drinks.jpg')
baza.add_category('Sovuq ichimliklar', image_path='images/categories/cold drinks.jpg')
baza.add_category('Combo', image_path='images/categories/combo.jpg')








baza.add_products(name='Trindwich chicken meat',image='images\Trindwich\Trindwich tovuq goshtidan.jpg',category_name='Trindwich')
baza.add_products(name='Trindwich beaf meat',image='images\Trindwich\Trindwich mol goshtidan.jpg',category_name='Trindwich')



baza.add_products(name='Chicken lavash',image='images\lavash/Tovuq goshtidan lavash.jpg',category_name='Lavash')
baza.add_products(name='Beaf lavash with cheese',image='images\lavash/Mol goshtidan pishloqli lavash.jpg',category_name='Lavash')
baza.add_products(name='Beaf spicy lavash ',image='images\lavash/Mol goshtidan qalampir lavash.jpg',category_name='Lavash')
baza.add_products(name='Chicken spicy lavash',image='images\lavash/Tovuq goshtidan qalampir lavash.jpg',category_name='Lavash')
baza.add_products(name='Chicken lavash with cheese',image='images\lavash/Tovuq goshtidan pishloqli lavash.jpg',category_name='Lavash')
baza.add_products(name='Fitter',image='images\lavash/Fitter.jpg',category_name='Lavash')

baza.add_products(name='Beaf spicy shaurma', image='images\shaurma/Mol goshtidan qalampir shaurma.jpg',category_name='Shaurma')
baza.add_products(name='Chicken shaurma', image='images\shaurma/Tovuq goshtidan shaurma.jpg',category_name='Shaurma')
baza.add_products(name='Chicken spicy shaurma', image='images\shaurma/Tovuq goshtidan qalampir shaurma.jpg',category_name='Shaurma')
baza.add_products(name='Beaf shaurma', image='images\shaurma/Mol goshtidan shaurma.jpg',category_name='Shaurma')

baza.add_products(name='Burger', image='images\Burger/Gamburger.jpg',category_name='Burgers')
baza.add_products(name='Doubleburger', image='images\Burger/Dablburger.jpg',category_name='Burgers')
baza.add_products(name='Cheeseburger', image='images\Burger/Chizburger.jpg',category_name='Burgers')
baza.add_products(name='Doublecheeseburger', image='images\Burger/Dablchizburger.jpg',category_name='Burgers')


baza.add_products(name='Chicken SUB with cheese', image='images\Sub/Tovuq goshtidan pishloqli sab.jpg',category_name='SUB')
baza.add_products(name='Beaf SUB with cheese', image='images\Sub/Mol goshtidan pishloqli sab.jpg',category_name='SUB')
baza.add_products(name='Chicken SUB', image='images\Sub/Tovuq goshtidan sab.jpg',category_name='SUB')
baza.add_products(name='Beaf SUB', image='images\Sub/Mol goshtidan sab.jpg',category_name='SUB')



baza.add_products(name='Village fries', image='images\Kartoshka/Jaydari kartoshka.jpg',category_name='French Fries')
baza.add_products(name='French fries', image='images\Kartoshka/kartoshka Fri.jpg',category_name='French Fries')
baza.add_products(name='Naggets 4', image='images\Kartoshka/Naggetslar, 4 dona.jpg',category_name='French Fries')
baza.add_products(name='Naggets 8', image='images\Kartoshka/Naggetslar, 8 dona.jpg',category_name='French Fries')

baza.add_products(name='Hot-Dog', image='images\Hot dog/Hot-dog.jpg',category_name='HotDogs')
baza.add_products(name='Double Hot-Dog', image='images\Hot dog/Hot-Dog-Dabl.jpg',category_name='HotDogs')
baza.add_products(name='Kids Hot-Dog', image='images\Hot dog/Bolalar uchun Hot-Dog.jpg',category_name='HotDogs')
baza.add_products(name='Mini Hot-Dog', image='images\Hot dog/Hot-Dog Mini.jpg',category_name='HotDogs')

baza.add_products(name='Smiles',image='images\Sneklar/Smayliki.jpg',category_name='Snacks')
baza.add_products(name='Strips',image='images\Sneklar/Strips.jpg',category_name='Snacks')


baza.add_products(name='Rice', image='image\Salat, garnir, non\Guruch.jpg', category_name='Salat, garnir, non')
baza.add_products(name='Bred', image='image\Salat, garnir, non\\Non.jpg', category_name='Salat, garnir, non')
baza.add_products(name='Salat', image='image\Salat, garnir, non\Salat.jpg', category_name='Salat, garnir, non')
baza.add_products(name='Salat Sezar', image='image\Salat, garnir, non\Sezar salat.jpg', category_name='Salat, garnir, non')
baza.add_products(name='Salat Grerchiski', image='image\Salat, garnir, non\Grecheskiy salat.jpg', category_name='Salat, garnir, non')

baza.add_products(name='Sezar sous', image='image\Souslar\Sezar sous.jpg', category_name='Souslar')
baza.add_products(name='Grecheskiy sous', image='image\Souslar\Grecheskiy sous.jpg', category_name='Souslar')
baza.add_products(name='Pishloqli sous', image='image\Souslar\Pishloqli sous.jpg', category_name='Souslar')
baza.add_products(name='Sarimsoqli sous', image='image\Souslar\Sarimsoqli sous.jpg', category_name='Souslar')
baza.add_products(name='Ketchup', image='image\Souslar\Ketchup.jpg', category_name='Souslar')
baza.add_products(name='Chili sous', image='image\Souslar\Chili sous.jpg', category_name='Souslar')
baza.add_products(name='Barbekyu sous', image='image\Souslar\Barbekyu sous.jpg', category_name='Souslar')
baza.add_products(name='Mayonez', image='image\Souslar\Mayonez.jpg', category_name='Souslar')

baza.add_products(name='Mol goshtidan donar', image='image\setlar\Mol goshtidan donar.jpg', category_name='Setlar')
baza.add_products(name='Tovuq goshtidan donar', image='image\setlar\Tovuq goshtidan donar.jpg', category_name='Setlar')
baza.add_products(name='Donar-box mol goshtli', image='image\setlar\Donar-box mol goshtli.jpg', category_name='Setlar')
baza.add_products(name='Donar-box tovuq goshtli', image='image\setlar\Donar-box tovuq goshtli.jpg', category_name='Setlar')











baza.add_product_type(product_type='default', price=23000, product_name="Trindwich chicken meat")
baza.add_product_type(product_type='default', price=2800, product_name='Trindwich beaf meat')
baza.add_product_type(product_type='default', price=15000, product_name='Smiles')
baza.add_product_type(product_type='default', price='20000', product_name='Strips')
baza.add_product_type(product_type="mini", price=23000, product_name='Chicken lavash')
baza.add_product_type(product_type="big", price=28000, product_name='Chicken lavash')
baza.add_product_type(product_type='mini', price=28000, product_name='Beaf lavash with cheese')
baza.add_product_type(product_type='big', price=33000, product_name='Beaf lavash with cheese')
baza.add_product_type(product_type='default', price=30000, product_name='Beaf spicy lavash ')
baza.add_product_type(product_type='default', price=28000, product_name='Chicken spicy lavash')
baza.add_product_type(product_type='mini', price=26000, product_name='Chicken lavash with cheese')
baza.add_product_type(product_type='big', price=31000, product_name='Chicken lavash with cheese')
baza.add_product_type(product_type='default', price=26000, product_name='Fitter')
baza.add_product_type(product_type='mini', price=24000, product_name='Beaf spicy shaurma')
baza.add_product_type(product_type='big', price=28000, product_name='Beaf spicy shaurma')
baza.add_product_type(product_type='mini', price=23000, product_name='Chicken shaurma')
baza.add_product_type(product_type='big', price=26000, product_name='Chicken shaurma')
baza.add_product_type(product_type='mini', price=23000, product_name='Chicken spicy shaurma')
baza.add_product_type(product_type='big', price=26000, product_name='Chicken spicy shaurma')
baza.add_product_type(product_type='mini', price=24000, product_name='Beaf shaurma')
baza.add_product_type(product_type='big', price=28000, product_name='Beaf shaurma')
baza.add_product_type(product_type='default', price=23000, product_name='Burger')
baza.add_product_type(product_type='default', price=35000, product_name='Doubleburger')
baza.add_product_type(product_type='default', price=25000, product_name='Cheeseburger')
baza.add_product_type(product_type='default', price=39000, product_name='Doublecheeseburger')
baza.add_product_type(product_type='default', price=18000, product_name='Kids_Kvadrich')
baza.add_product_type(product_type='default', price=20000, product_name='Chicken SUB with cheese')
baza.add_product_type(product_type='default', price=22000, product_name='Beaf SUB with cheese')
baza.add_product_type(product_type='default', price=18000, product_name='Chicken SUB')
baza.add_product_type(product_type='default', price=20000, product_name='Beaf SUB')
baza.add_product_type(product_type='default', price=16000, product_name='Village fries')
baza.add_product_type(product_type='default', price=15000, product_name='French fries')
baza.add_product_type(product_type='default', price=9000, product_name='Naggets 4')


baza.add_product_type(product_type='default', price=18000, product_name='Naggets 8')
baza.add_product_type(product_type='default', price=15000, product_name='Hot-Dog')
baza.add_product_type(product_type='default', price=22000, product_name='Double Hot-Dog')
baza.add_product_type(product_type='default', price=9000, product_name='Kids Hot-Dog')
baza.add_product_type(product_type='default', price=9000, product_name='Mini Hot-Dog')
baza.add_product_type(product_type='default', price=15000, product_name='Smiles')
baza.add_product_type(product_type='default', price=20000, product_name='Strips')
baza.add_product_type()


baza.add_pr_description('Fitter', 'ewfhnejvnerjvn')
baza.add_pr_description('Trindwich chicken meat', 'Нежное куриное мясо гриль, салат "Айсберг", кусочки спелого\n помидора и свежего огурца, мягкий сыр "Фетакса", легкий\n сливочный соус Эко в нежно-салатовом лаваше Фиттер\nЦена: 29 000 сум')
baza.add_pr_description('Trindwich beaf meat', '')
baza.add_pr_description('Chicken lavash', '')
baza.add_pr_description( 'Beaf lavash with cheese', '' )
baza.add_pr_description('Beaf spicy lavash', '')
baza.add_pr_description('Chicken spicy lavash', '')
# Chicken lavash with cheese

def sort_user_products(tg_id: int):
    data = baza.get_order(tg_id)
    for user_id, product_id, quantity in data:
        print(
            f"{user_id=}"
        )
        print(
            f"product name: {baza.get_product_name(product_id)[0]}"
        )
        print(
            f"{quantity=}"
        )

sort_user_products(1058730773)
