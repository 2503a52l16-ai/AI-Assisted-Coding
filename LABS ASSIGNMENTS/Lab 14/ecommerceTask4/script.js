// --- UTILITIES ---
function loadCart() {
  return JSON.parse(localStorage.getItem("cart")) || [];
}

function saveCart(cart) {
  localStorage.setItem("cart", JSON.stringify(cart));
}

// --- INDEX PAGE ---
const addButtons = document.querySelectorAll(".add-to-cart");
if (addButtons.length > 0) {
  let cart = loadCart();
  updateCartCount();

  addButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      const card = btn.closest(".product-card");
      const item = {
        id: card.dataset.id,
        name: card.dataset.name,
        price: parseFloat(card.dataset.price)
      };
      cart.push(item);
      saveCart(cart);
      updateCartCount();
      btn.textContent = "Added!";
      setTimeout(() => (btn.textContent = "Add to Cart"), 1000);
    });
  });
}

function updateCartCount() {
  const countEl = document.getElementById("cart-count");
  if (countEl) countEl.textContent = loadCart().length;
}

// --- CART PAGE ---
if (document.getElementById("cart-items")) {
  const cart = loadCart();
  const cartContainer = document.getElementById("cart-items");
  const totalEl = document.getElementById("cart-total");

  if (cart.length === 0) {
    cartContainer.innerHTML = "<p>Your cart is empty.</p>";
  } else {
    let total = 0;
    cartContainer.innerHTML = cart.map((item, index) => {
      total += item.price;
      return `
        <div class="cart-item">
          <span>${item.name} - $${item.price.toFixed(2)}</span>
          <button class="remove-btn" data-index="${index}">Remove</button>
        </div>`;
    }).join("");
    totalEl.textContent = total.toFixed(2);
  }

  document.querySelectorAll(".remove-btn").forEach(btn => {
    btn.addEventListener("click", (e) => {
      const index = e.target.dataset.index;
      cart.splice(index, 1);
      saveCart(cart);
      location.reload();
    });
  });
}

// --- CHECKOUT PAGE ---
const checkoutForm = document.getElementById("checkout-form");
if (checkoutForm) {
  checkoutForm.addEventListener("submit", (e) => {
    e.preventDefault();
    localStorage.removeItem("cart");
    window.location.href = "order.html";
  });
}
