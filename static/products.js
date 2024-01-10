$(".add-to-cart").on("click", function() {
    localStorage.clear();
    localStorage.setItem("productName", this.parentElement.querySelector(".product-name").innerHTML);
    localStorage.setItem("productPrice", this.parentElement.querySelector(".product-price").innerHTML);
    localStorage.setItem("productImage", this.parentElement.parentElement.querySelector(".product-image-row").querySelector(".product-image").src);

    window.location.href = "templates\checkout.html";
});

// Function to fetch data from the Flask endpoint
async function fetchData() {
    try {
        const response = await fetch('/get_data_market');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        displayData(data);
    } catch (error) {
        console.error('Error:', error);
    }
}

// Function to display the data on the page
function displayData(data) {
    const container = document.querySelector('.product-grid');
    container.innerHTML = ''; // Clear the container first
    
    data.forEach((item, index) => {
        const productHTML = `
        <div class="product-preview">
          <div class="product-image-row">
            <img class="product-image" src="${item.link}" alt="image">
          </div>
          <div class="product-description">
            <p class="product-name">${item.description}</p>
            <p class="product-price">$${parseFloat(item.price).toFixed(2)}</p>
            <button class="add-to-cart">Buy</button>
          </div>
        </div>
        `;
        
        container.innerHTML += productHTML;
    });
}

// Fetch data when the page loads
window.addEventListener('load', fetchData);
