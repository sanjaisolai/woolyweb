
$(".product-image").attr("src", localStorage.getItem('productImage'));
$(".product-name").html(localStorage.productName);
$(".product-price").html(localStorage.productPrice);
$(".total").html(localStorage.productPrice);

$(".delivery-option-input").on("click", function() {
    if (this.id == 1) {
        $(".shipping-charge").html("$0.00");
        $(".delivery-date").html("Delivery date: Tuesday, June 21");
    } else if (this.id == 2) {
        $(".shipping-charge").html("$4.99");
        $(".delivery-date").html("Delivery date: Wednesday, June 15");
    } else if (this.id == 3) {
        $(".shipping-charge").html("$9.99");
        $(".delivery-date").html("Delivery date: Monday, June 13");
    }
    initPrice();});
initPrice();
function initPrice() {
    var total = parseFloat($(".total").html().slice(1));
    var shippingCharge = parseFloat($(".shipping-charge").html().slice(1));
    $(".total-before-tax").html("$" + (total + shippingCharge).toFixed(2));
    var totalBeforeTax = parseFloat($(".total-before-tax").html().slice(1));
    var taxValue = (10/100) * totalBeforeTax;
    $(".tax").html("$" + taxValue.toFixed(2));
    var tax = parseFloat($(".tax").html().slice(1));
    var orderTotalValue = totalBeforeTax + tax;
    $(".order-total").html("$" + orderTotalValue.toFixed(2));
    var orderTotal = parseFloat($(".order-total").html().slice(1));}
