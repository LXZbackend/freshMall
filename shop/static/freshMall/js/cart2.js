$(function(){

// 全选按钮
// var allBtn = $(".all input")
var allBtn=document.querySelector(".all input");
// alert(allBtn)
// 每一行选中宝贝的按钮，同时也是判断有几行
// var pitchs = $('.cart_list_td .col01 input')
var pitchs =document.querySelectorAll(".cart_list_td .col01 input");


// var pitchs = $('#checked') 
// alert(pitchs.length)
// 宝贝数量加按钮
var num_up = document.querySelectorAll('.cart_list_td .add');

// alert(num_up.length)
// 宝贝数量减少按钮
var num_down = document.querySelectorAll('.cart_list_td .minus');
// 宝贝的数量
var num  = document.querySelectorAll('.cart_list_td .col06 input');

// 宝贝小计
var total = document.querySelectorAll('.cart_list_td .col07>span');
// alert(total[0].innerHTML);

// 删除按钮
var remove = document.querySelectorAll('.cart_list_td #remove');
// alert(remove.length)
// 单价
// var price = $('.cart_list_td .col05')
// 
var price = document.querySelectorAll('.cart_list_td .col05');
// alert(price[0])
// 全选按钮状态开关
var allBtn_on = true;

// 增加按钮的数量记录
var addNum = 0;


// 减少按钮的数量记录
var minNum = 0;

// 总价
var priceAll = document.querySelector('.settlements #total_pic');
// alert('总价'+priceAll);
var allPrice = 0
// 行数
var tr = document.querySelectorAll('.cart_list_td');
// alert(tr.length)
//已选中宝贝的数量
var picths_num = document.querySelector('.settlements #total_num');
// alert(picths_num)
// 宝贝数量的长度
var length = pitchs.length;
// alert(length)
var number = $('.total_count em').text()

$('.total_count em').text(length)




for(var i =0;i<length;i++){
	pitchs[i].index=i;
	num_up[i].index = i;
	num_down[i].index = i;
	remove[i].index = i;


	pitchs[i].onclick = function(){

		if(this.checked){
			// 这是显示已经选中宝贝的总数量。当选中后选中的宝贝数量加1
			picths_num.innerHTML = ++picths_num.innerHTML;
			// 拿出这你点击这一行的价钱
			allPrice += Number(total[this.index].innerHTML);
			// 写到总价中  这里注意需要对总价进行 处理 不然会 会有小数
			priceAll.innerHTML = Math.round(allPrice*100)/100;
		}else{
			picths_num.innerHTML = --picths_num.innerHTML;
			allPrice -= Number(total[this.index].innerHTML);
			priceAll.innerHTML = Math.round(allPrice*100)/100;
		}

	}

// 点击加号
	num_up[i].onclick = function(){
		addNum = 0;
		allPrice = 0;
		var shuliang = num[this.index].value;
		shuliang++;
		// alert(shuliang)
		num[this.index].value = shuliang;
		// total[this.index].innerHTML = shuliang * (price[this.index].innerHTML);
		// 这里在计算小计的时候 值需要进行保留计算，不然会出现很长的小数位 先乘以100  在除以100  你要是保留三位 就乘以1000
		total[this.index].innerHTML = Math.round(shuliang * (price[this.index].innerHTML)*100)/100
		if(!pitchs[this.index].checked){
			// 这里是当你点击增加数量和，这个复选框默认选上
			pitchs[this.index].checked =true		

		}
		for(var i =0;i<pitchs.length;i++){ 
			if(pitchs[i].checked){
				addNum++;
				allPrice += Number(total[i].innerHTML)
			
			}
		}

		// 把数量和总价写道里面
		picths_num.innerHTML = addNum;
		priceAll.innerHTML = Math.round(allPrice*100)/100;

	}


// 点击减号
	num_down[i].onclick=function(){
		  addNum = 0;
			allPrice = 0;
			var shuliang = num[this.index].innerHTML;
			shuliang++;
			num[this.index].innerHTML = shuliang;
			// total[this.index].innerHTML = shuliang * (price[this.index].innerHTML);
			 total[this.index].innerHTML = Math.round(shuliang * (price[this.index].innerHTML)*100)/100
			if (!pitchs[this.index].checked) {
				// 这里是当你点击增加数量和 这个复选框自己选择上
				pitchs[this.index].checked = true;
			}
			for (var i = 0; i < pitchs.length; i++) {
				// 因为上面复选框已经选择了  这时候下面的价钱应该也变动  所以遍历复选框 看谁选上为了，把价钱加到总价上
				if (pitchs[i].checked) {
					addNum++;
					allPrice += Number(total[i].innerHTML);
				}

			}
			// 把数量和总价插入到里面
			picths_num.innerHTML = addNum;
			priceAll.innerHTML = allPrice;
		}
		num_down[i].onclick = function() {
			addNum = 0;
			allPrice = 0;
			var shuliang = num[this.index].value;
			shuliang--;
			// 当数量小于0的时候做下面的操作
			if (shuliang < 1) {
				// 执行删除操作@
				allPrice = 0;
				// 在这样里为啥要改变这三个信息，第一 类是查看谁被删了  false 是为了遍历时看谁被选中了，你删了其他网页中源码还在，你如果不加
				// 等他判断谁被选中时就把 这个删除的也加上了  就不正确了 所以 这里要提醒他说 这个没有被选中
				// 这个给他增加一个不存在的类名 方便下面使用
				tr[this.index].className = "hanmy";
				pitchs[this.index].checked = false;
				// 当执行到这的时候 那条信息就隐藏了
				tr[this.index].style.display = "none";
				// 计数
				number--;
				$('.total_count em').text(number);

				// 同样是删除数据库
					shopId = $(this).prev().attr('name')
				 	// post 请求 用于传传输删除的商品id
				 	$.post('/delCartShop/',{'shopId':shopId})
				  console.log(shopId)





					// 如果有这个类命名的数量 不等于tr 长度 就执行下面的  就代表
				if (document.querySelectorAll(".hanmy").length != tr.length) {
					for (var i = 0; i < tr.length; i++) {
						// 如果tr 没有被class并且并选中了  就执行下面的操作
						if ( tr[i].className!="hanmy" && pitchs[i].checked) {
							removeNum++;
							picths_num.innerHTML = removeNum;
							allPrice += Number(total[i].innerHTML);
						}
					}

				} else {
					// 这时候是 tr 表空了 就把选择的数量和价格重置为0
					console.log("1");
					removeNum = 0;
					allPrice = 0;
					picths_num.innerHTML = removeNum;
				 
				}

				priceAll.innerHTML = allPrice;
			} else {  //这个是当数量不小于1 时 做的该做的操作，计算数量 计算总价啥的
				num[this.index].value = shuliang;
				// console.log(num[this.index].value)
				// total[this.index].innerHTML = shuliang * (price[this.index].innerHTML);

				total[this.index].innerHTML = Math.round(shuliang * (price[this.index].innerHTML)*100)/100

				if (!pitchs[this.index].checked) {
					pitchs[this.index].checked = true;
				}
				for (var i = 0; i < pitchs.length; i++) {
					if (pitchs[i].checked) {
						addNum++;
						// console.log(Number(total[i].innerHTML))
						allPrice += Number(total[i].innerHTML);
					}

				}
				picths_num.innerHTML = addNum;
				priceAll.innerHTML = Math.round(allPrice*100)/100;
			}

	}
	// 这是删除操作 
	var removeNum = 0;
	remove[i].onclick =function(){
		allPrice=0;
		tr[this.index].className = "hanmy";
		pitchs[this.index].checked = false
		tr[this.index].style.display = 'none'
		// 件数减少
				number--;
				$('.total_count em').text(number);
		// console.log(document.querySelectorAll(".hanmy").length)

		// 这是告诉服务器 删除一个操作购物车 通过找到id 传到服务器,并删除
	
	  // console.log($(this).prev().prev().find('.num_show').attr('name'))
	 	shopId = $(this).parent().prev().prev().find('input').attr('name')
	 	// post 请求 用于传传输删除的商品id
	 	$.post('/delCartShop/',{'shopId':shopId})
	  console.log(shopId)














	if (document.querySelectorAll(".hanmy").length != tr.length) {
	
		for (var i = 0; i < tr.length; i++) {
			

			// $('div').hasClass('redColor')
			 // if (!tr[i].className && pitchs[i].checked) 本来是这个方式 !tr[i] .classNmae  判断是否有这个class样式。例子中 他那个标签是空的。我这里面有 所以这个样式一直都不对。 这里改成他样式 是不是那个  如果是就执行
			if (tr[i].className!="hanmy" && pitchs[i].checked){//这个判断是找 那个
			
				removeNum++;
				picths_num.innerHTML = removeNum;
				allPrice += Number(total[i].innerHTML);
			 }
		}
	}else {
		// console.log('1');
		removeNum=0;
		allPrice = 0;
		picths_num.innerHTML = removeNum;

	}
	priceAll.innerHTML = allPrice;

	}//点击函数结束

// 循环的 结束
}
allBtn.onclick = function(){
	for (var i=0;i<pitchs.length;i++){
		pitchs[i].checked = this.checked;
	}
	if(allBtn_on){
		// 把选中宝贝的数量复制给下面的总的数量
		picths_num.innerHTML = pitchs.length;

		for(var j=0;j<total.length;j++){
			allPrice += Number(total[j].innerHTML);	
		}

		priceAll.innerHTML =  Math.round(allPrice*100)/100;
		// 这里为啥要把状态改变  为了方便下次点击 时候就把价格啥的清空
		allBtn_on = false

	}
	else{
		picths_num.innerHTML = 0;
		allPrice = 0;
		priceAll.innerHTML = 0;
		allBtn_on = true;
	}
}//全选按钮结束

// ××××××××××××××××××× 
$jiesuan = $('.settlements .col04 a')

$jiesuan.click(function(){
		var gID = []
		var gNum = []


		for (var i = 0; i < tr.length; i++)
	 {

		if (pitchs[i].checked)
		 {
			// 通过查询器 找到ul对应的ul 下面的input 在input 中取到商品的id 和数量
			$shoptext=$('.cart_list_td').eq(i).find('.num_show')
			goodId = 	$shoptext.attr('name')
			gID.push(goodId)
			goodnum = $shoptext.val()
			gNum.push(goodnum)


			}
		}
		console.log(gID)
		console.log(gNum)
		// 这是组合成json  通过JSON.stringfy(序列话穿过去),并且在服务端反序列化
			var data = {
						gId:gID,
						gNum:gNum,
					}

				$.post('/cartHandle/',JSON.stringify(data),

				  function(data){
				  	// 并没用
				  	if(data.result){
				  		// 当服务器处理完 通过jq重定向 这样就不会产生数据不同步
				  		window.location= '/place_order/'
				  	}

				  	console.log(data.result)


			});








});//这是点击结束







// 这是加载函数的结束
});
