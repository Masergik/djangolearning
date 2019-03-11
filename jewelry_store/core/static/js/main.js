
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
	form.on('submit', function(e){
	    e.preventDefault();
	    console.log('123');
	    var quantity = $('#quantity').val();
	    console.log(quantity);
	    var submit_btn = $('#submit_btn');
	    var product_id = submit_btn.data("product_id");
	    var product_name = submit_btn.data("name");
	    var product_vendor_code = submit_btn.data("vendor_code");
	    var product_price = submit_btn.data("price");
	    var product_sale = submit_btn.data("sale");
	    var product_price_with_sale = submit_btn.data("price_with_sale");
	    console.log(product_id);
	    console.log(product_vendor_code);
	    console.log(product_name);
	    console.log(product_price);
	    console.log(product_sale);
	    console.log(product_price_with_sale);

            var data = {};
            data.product_id = product_id;
            data.quantity = quantity;
            var csrf_token = $('#form_buy_product [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;
            var url = form.attr("action");

        console.log(data)
        $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");
                 console.log(data.products_total_quantity);
                 if (data.products_total_quantity){
                    $('#cart_total_quantity').text(data.products_total_quantity);
                    console.log(data.products);
                    $('.cart-items ul').html("");
                    $.each(data.products, function(k, v){
                        $('.cart-items ul').append('<li>'+v.name+', '+v.quantity+' шт. по '+v.price_per_item+' грн  '+
                	    //'<a href="" class="delete-item"> <i class="flaticon-cancel-1"> </a>'+
                        '</li>');
                    })
                 }

             },
             error: function(){
                console.log("error")
             }
        })

	});

    function showingCart(){
        $('.cart-items').toggleClass('d-none');
    };

//	$('.cart-container').on('click', function(e){
//	    e.preventDefault();
//	    showingCart();
//	});

	$('.cart-container').mouseover(function(){
	    showingCart();
	});

	$('.cart-container').mouseout(function(){
	    showingCart();
	});

	$(document).on('click', '.delete-item', function(e){
	    e.preventDefault();
	    $(this).closest('li').remove();
	});
//
//	function calculatingCartAmount(){
//	var total_order_amount = 0
//	    $('.product-total-price').each(function(){
//	        total_order_amount += parseInt($(this).text());
//	    });
//	    $('#total_order_amount').text(total_order_amount);
//	};
//
//	$(document).on('change', ".quantity-input", function(){
//	    var current_quantity = parseInt($(this).val());
//	    console.log(current_quantity)
//
//	    var current_div = $(this).closest('span');
//	    var current_price = parseInt(current_div.find('.product-price-per-item').text());
//	    console.log(current_price)
//	    var total_amount = current_quantity*current_price;
//	    console.log(total_amount)
//	    current_div.find('.product-total-price').text(total_amount);
//
//	    calculatingCartAmount();
//	})
//
//	calculatingCartAmount();
})


