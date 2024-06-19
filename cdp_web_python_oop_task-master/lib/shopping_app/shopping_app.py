from customer import Customer
from item import Item
from seller import Seller

seller = Seller("DICストア")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("メモリー", 13880, seller)
    Item("マザーボード", 28980, seller)
    Item("電源ユニット", 8980, seller)
    Item("PCケース", 8727, seller)
    Item("3.5インチHDD", 10980, seller)
    Item("2.5インチSSD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPUクーラー", 13400, seller)
    Item("グラフィックボード", 23800, seller)

print("🤖 Por favor, dime tu nombre")
customer = Customer(input())

print("🏧 Por favor, introduce la cantidad a cargar en tu billetera")
customer.wallet.deposit(int(input()))

print("🛍️ Comenzando la compra")
end_shopping = False
while not end_shopping:
    print("📜 Lista de productos")
    seller.show_items()

    print("️️⛏ Por favor, introduce el número del producto")
    number = int(input())

    print("⛏ Por favor, introduce la cantidad del producto")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 Total a pagar: {customer.cart.total_amount()}")

    print("😭 ¿Deseas finalizar la compra? (si/no)")
    end_shopping = input() == "si"

print("💸 ¿Deseas confirmar la compra? (si/no)")
if input() == "si":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultados ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️Propiedades de {customer.name}")
customer.show_items()
print(f"😱👛 Saldo en la billetera de {customer.name}: {customer.wallet.balance}")

print(f"📦 Estado del inventario de {seller.name}")
seller.show_items()
print(f"😻👛 Saldo en la billetera de {seller.name}: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items()
print(f"🌚 Total a pagar: {customer.cart.total_amount()}")

print("🎉 Fin del programa")
