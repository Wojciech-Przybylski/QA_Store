var addItemButton = document.getElementsByClassName('btn btn-outline-dark mt-auto');
for (var i = 0; i < addItemButton.length; i++){
    var button = addItemButton[i]
    button.addEventListener('click', addToBasketClicked)
}
console.log(addItemButton);

function addToBasketClicked(event){
    var button = event.target
    var shopItem = button.parentElement.parentElement.parentElement.parentElement.parentElement
    var itemName = shopItem.getElementsByClassName('fw-title')[0].innerText
    var itemPrice = shopItem.getElementsByClassName('price')[0].innerText
    var itemQ = shopItem.querySelector('input').value
        if(isNaN(itemQ) || itemQ <=0){
            itemQ = 1
        }
        else if(itemQ > 50){
            itemQ = 50
        }
        
    // var totalPerItem = `£${Math.round(((parseFloat(itemPrice.replace('£',''))*itemQ)*100)/100)}`
    console.log(itemName, itemPrice, itemQ)
    // addItemToBasket(itemName, itemPrice, itemQ)
}
// function addItemToBasket(itemName, itemPrice, itemQ, totalPerItem) {
//     var basketRow = document.createElement('div'); // Create a new container div
//     basketRow.classList.add('basket-item'); // Add a class to style the item
//     var basketRowContents = `
//         <div class="basket-col">${itemName}</div>
//         <div class="basket-col">${itemPrice}</div>
//         <div class="basket-col">${itemQ}</div>
//         <div class="basket-col">${totalPerItem}</div>`;
    
//     basketRow.innerHTML = basketRowContents;
    
//     var basketItems = document.querySelector('.table-rows'); // Use querySelector to get the container
//     if (basketItems) {
//         basketItems.appendChild(basketRow); // Append the row to the container
//     } else {
//         console.error("Container for basket items not found.");
//     }
// }


