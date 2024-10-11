
// Function to load the product data from the JSON file
async function loadProductData() {
    const response = await fetch('/static/data/products_data.json');  // Fetch the JSON file
    const productsData = await response.json();  // Parse it into an object
    return productsData;
}

// Function to load the content dynamically based on the menu selection
async function loadContent(category) {

    const productsData = await loadProductData();  // Load the product data from JSON
    const productsContainer = document.getElementById('products');
    productsContainer.innerHTML = '';  // Clear existing content
    const products = productsData[category];
    const productListText = document.querySelector('#main-para');
    if (productListText) {
        productListText.style.display = 'none';  // Hide the initial message
    }
    products.forEach(product => {
        // Create HTML structure for each product
        const productCard = `
            <div class="product-card">
                <img src="${product.image}" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>${product.price}</p>
                 <button class="add-button" onclick="addToCart('${product.name}', '${product.price}')">Add</button>
            </div>
        `;
        productsContainer.innerHTML += productCard;  // Append the product card

    });
    highlightActiveCategory(category);
}
function highlightActiveCategory(category) {
    console.log("Highlighting category:", category);  // Debugging

    const sidebarLinks = document.querySelectorAll(".sidebar-link");
    
    // Remove 'active' class from all sidebar links
    sidebarLinks.forEach(link => {
        link.classList.remove("active");
    });

    // Find the link that matches the selected category and add 'active' class
    sidebarLinks.forEach(link => {
        console.log("Checking link:", link.dataset.category);  // Debugging
        if (link.dataset.category === category) {
            link.classList.add("active");
            console.log("Added active class to:", link.dataset.category);  // Debugging
        }
    });
}

// let count = 0;
// document.getElementById("counting").innerText = data;
// function increment(item){
    
// }
// function addToCart(item, price) {

//     alert(item + " added to cart!");
// }
// Function to get CSRF token from the cookie
function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, 10) === 'csrftoken=') {
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
}

function addToCart(itemName, itemPrice) {
    $.ajax({
        url: '/add-to-cart/',
        method: 'POST',
        data: {
            'item_name': itemName,
            'item_price': itemPrice,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(response) {
            if (response.success) {
                // Display the current quantity in an alert
                alert(response.quantity + " " + response.item_name + " are added to cart!");
            } else {
                alert("Failed to add " + itemName + " to cart. Please try again.");
            }
        },
        error: function(xhr, status, error) {
            alert("Error: Unable to add " + itemName + " to cart.");
        }
    });
}
