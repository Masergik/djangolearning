
'use strict';


$(window).on('load', function() {

});

(function($) {
	/*------------------
		Last product Slider
	--------------------*/
	$('.product-slider').owlCarousel({
		loop: true,
		nav: true,
		dots: false,
		margin : 30,
		autoplay: true,
		navText: ['<i class="flaticon-left-arrow-1"></i>', '<i class="flaticon-right-arrow-1"></i>'],
		responsive : {
			0 : {
				items: 1,
			},
			480 : {
				items: 2,
			},
			768 : {
				items: 3,
			},
			1200 : {
				items: 4,
			}
		}
	});
})(jQuery);

	/*------------------
		Product Form
	--------------------*/
$(document).ready(function(){

	var form = $('#form_buy_product');
	console.log(form);

	function cartUpdating(product_id, quantity, size_value, is_delete) {
	    var data = {};
        data.product_id = product_id;
        data.quantity = quantity;
        data.size = size_value;
        var csrf_token = $('#header_find_prod [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete) {
            data["is_delete"] = true;
        }

        var url = form.attr("action");

        console.log(data)
        $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");
                 if (data.products_total_quantity || data.products_total_quantity == 0){
                    $('#cart_total_quantity').text(data.products_total_quantity);
                    console.log(data.products);
                    $('.cart-items ul').html("");
                    $.each(data.products, function(k, v){
                        $('.cart-items ul').append('<li>'+v.name+' (размер: '+v.size+'), '+v.quantity+' шт. по '+v.price_per_item+' грн  '+
                	    '<a href="" class="delete-item" data-product_id="'+v.id+' "> <i class="flaticon-cancel-1"></i></a>'+
                        '</li>');
                    });
                 }
             },
             error: function(){
                console.log("error");
             }
        });
	};

	form.on('submit', function(e){
	    e.preventDefault();
	    var quantity = $('#quantity').val();
        var size_value = $('.size_value:checked').val();
	    var submit_btn = $('#submit_btn');
	    var product_id = submit_btn.data("product_id");
	    var product_name = submit_btn.data("name");
	    var product_vendor_code = submit_btn.data("vendor_code");
	    var product_price = submit_btn.data("price");
	    var product_sale = submit_btn.data("sale");
	    var product_price_with_sale = submit_btn.data("price_with_sale");
	    console.log(product_id);
	    console.log(product_name);
	    console.log(product_vendor_code);
	    console.log(quantity);
	    console.log(size_value);
	    console.log(product_price);
	    console.log(product_sale);
	    console.log(product_price_with_sale);
	    var is_delete = false;

        cartUpdating(product_id, quantity, size_value, is_delete);

	});

// Отображение окна корзины при наведении на кнопку "Корзина" в Navbar
	$('.cart-container').mouseover(function(){
	    $('.cart-items').removeClass('d-none');
	});

	$('.cart-container').mouseout(function(){
	    $('.cart-items').addClass('d-none');
	});

     $(document).on('click', '.delete-item', function(e){
         e.preventDefault();
         var product_id = $(this).data("product_id");
         console.log(product_id);
         var quantity = 0;
         var size_value = $(this).data("size");
         var is_delete = true;

         cartUpdating(product_id, quantity, size_value, is_delete);
     });

/////////////////////////////////////////////////////////////
// Пофиксить обновление количества товаров в корзине
    function calculatingCartAmount(){
        var total_order_amount = 0;
        $('.product-total-price').each(function() {
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });
        console.log(total_order_amount);
        $('#total_order_amount').text(total_order_amount.toFixed(2));
    };

    $(document).on('change', ".quantity-input", function(){
        var current_quantity = $(this).val();
        console.log(current_quantity);

        var current_div = $(this).closest('span');
        var current_price = parseFloat(current_div.find('.product-price-per-item').text()).toFixed(2);
        console.log(current_price);
        var total_amount = parseFloat(current_quantity*current_price).toFixed(2);
        console.log(total_amount);
        current_div.find('.product-total-price').text(total_amount);

        calculatingCartAmount();
    });

    calculatingCartAmount();

///////////////////////////////////////////////////////////

})


