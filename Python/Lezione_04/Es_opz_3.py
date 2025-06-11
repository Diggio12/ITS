from typing import Any

def create_product(name: str, price: float, quantity: int) -> dict[str, Any]:
    return {
        "name": name,
        "price": price,
        "quantity": quantity
    }

def add_product(cart: list[dict[str, Any]], product: dict[str, Any]) -> None:
    cart.append(product)

def remove_product(cart: list[dict[str, Any]], product_name: str) -> list[dict[str, Any]]:
    updated_cart: list[dict[str, Any]] = []
    for p in cart:
        if p['name'] != product_name:
            updated_cart.append(p)
    return updated_cart

def view_cart(cart: list[dict[str, Any]]) -> None:
    print("Shopping Cart Contents:")
    for product in cart:
        print(f"- {product['name']}: {product['quantity']} units at €{product['price']} each")

def calculate_total(cart: list[dict[str, Any]], discount_rate: float = 0.10) -> dict[str, float]:
    subtotal: float = sum(product['price'] * product['quantity'] for product in cart)
    discount: float = discount_rate
    tax: float = 0.22
    
    discounted_total: float = subtotal * (1 - discount)

    total: float = discounted_total * (1 + tax)

    return {
        "subtotal": subtotal,
        "discount": discount * 100,  
        "tax": tax * 100,            
        "total": total
    }

def print_summary(cart: list[dict[str, Any]]) -> None:
    
    view_cart(cart)
    print("\nDetailed Summary:")
    
    for product in cart:
        total_price: float = product['price'] * product['quantity']  # type: ignore
        print(f"{product['name']} - Quantity: {product['quantity']}, Unit Price: €{product['price']}, Total: €{total_price}")
    
    totals: dict[str, float] = calculate_total(cart)
    print("\nTotals:")
    print(f"Subtotal: €{totals['subtotal']}")
    print(f"Discount Applied: {totals['discount']}%")
    print(f"Tax: {totals['tax']}%")
    print(f"Final Total: €{round(totals['total'], 2)}")