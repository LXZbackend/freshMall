$(function(){

var $add = $(".add")
var $minus = $('.minus')
var pic = $('.show_pirze em').text()
// alert(pic)
var $total = $('.total em')
var num = $('.num_show').val()


// 初始化价钱
$total.text(pic)
// alert(num)
// 增加点击事件
$add.click(function(){

$('.num_show').val(++num);
// Math.round(allPrice*100)/100;s
total = num *pic
// alert(total)
total = Math.round(total*100)/100
$total.text(total)

});//增加点击事件结束

// 减少点击时间开始
$minus.click(function(){


	if (num>0){$('.num_show').val(--num)}
	else {
		$('.num_show').val(0)
	}
	total = num *pic
	total = Math.round(total*100)/100
	$total.text(total)
	
});

// 加入购物车点击事件开始
$('.add_cart').click(function(){
	$input = $('.num_show')
	goodID = $input.attr("name")
	num = $input.val()
	total = $total.text()
	console.log(goodID)
	console.log(num)
	console.log(total)
	//准备post 像后台传送数据
	$.post('/addCart/',{'goodID':goodID,'num':num,'total':total},
	       function(data){
	       $('.goods_count').text(data.shopNum)
	       // alert(data.shopNum)
	       			location.reload()
	       }

	       ); 

});//购买点击
$('.buy_btn').click(function(){
	$input = $('.num_show')
	goodID = $input.attr("name")
	num = $input.val()
	total = $total.text()
	console.log(goodID)
	console.log(num)
	console.log(total)
	//准备post 像后台传送数据
	$.post('/immediateBuy/',{'goodID':goodID,'num':num,'total':total},
	       function(data){

       			if(data.result){
			  		// 当服务器处理完 通过jq重定向 这样就不会产生数据不同步
			  		window.location= '/place_order/'
			  	}

	}); 
});


// $('.goods_detail_list .num_show').change(function(){

// })









});//加载函数结束