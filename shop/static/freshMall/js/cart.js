$(function(){


// 这是减少
$('.minus').click(function(){
		var n =$(this).prev().val()
		// alert(n)

		var num  = parseInt(n)-1;
		if (num>=0){
		$(this).prev().val(num)

		}
		else{
		$(this).prev().val(0)
		}

		// alert($(this).parent().parent().prev().text())

		// 找到商品的单价
		var onePic = $(this).parent().parent().prev().text()
		// var pic = parseInt(onePic)
		// 得到这个商品的总价

		var total = num*onePic
		// 保留两位小数
		total=total.toFixed(2)
		
	
		if (total>=0){
				 total = '￥'+total
				$(this).parent().parent().next().text(total)
		}



});


$('.add').click(function(){
		var n =$(this).next().val()
		// alert(n)
		var num  = parseInt(n)+1;
		if (num>=0){
	$(this).next().val(num)
		}
	// alert($(this).parent().parent().prev().text())

		// 找到商品的单价
		var onePic = $(this).parent().parent().prev().text()
		// var pic = parseInt(onePic)
		// 得到这个商品的总价

		var total = num*onePic
		// js保留两位小数
			total=total.toFixed(2)

		if (total>=0){
				total = '￥'+total
					 $(this).parent().parent().next().text(total)
		}	

});




});

