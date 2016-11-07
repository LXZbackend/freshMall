// 这是商品列表的js 实现点击加入购物车,实现商品加入购物车
$(function(){

	$('.add_goods').click(function(){
		goodID = $(this).prev().prev().attr('name')
		num = 1
		total= $(this).prev().attr('name')

		$.post('/addCart/',{'goodID':goodID,'num':num,'total':total},
	       function(data){
	       $('.goods_count').text(data.shopNum)
	       // alert(data.shopNum)
	       			location.reload()
	       }

	       ); 

	})

});