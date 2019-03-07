
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
	})
})


