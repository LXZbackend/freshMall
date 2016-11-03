$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;


	$('#user_name').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});


	function check_user_name(){
		var len = $('#user_name').val().length;
		$uername = $('#user_name')
// $.post('/testform/',{'name':$('#user_name').val()},function(data){	
// 			// if (data.name==false){
// 			// 	$uername.next('span').text('这个用户名可以使用')
// 			// }
		if(len>5&&len<20)
		{
			// 这是验证用户是否存在
		$.post('/testform/',{'name':$('#user_name').val()},function(data){

		if (data.name==false){
				$uername.next('span').text('这个用户名可以使用')
				error_name = false;
				// $uername.next('span').css('color','green')
		}
		else {
			$uername.next('span').text('这个用户名已经被占用了')
				error_name = true;
		}

		});

			$('#user_name').next().show();
		
		}


		else
		{	$('#user_name').next().html('请输入5-20个字符的用户名')
			// $('#user_name').next().hide();
			error_name = true;
		}


	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}


	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致')
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确')
			$('#email').next().show();
			error_check_password = true;
		}

	}


	$('#reg_form').submit(function() {
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
		{
			alert("shuru头无")
			return true;
		}
		else
		{	alert("shuru头无")
			return false;
		}

	});
// 这是购物车操作

//加的效果
// $(".add").click(function(){
// var n=$(this).prev().val();
// var num=parseInt(n)+1;
// if(num==0){ return;}
// $(this).prev().val(num);
// });
// //减的效果
// $(".jian").click(function(){
// var n=$(this).next().val();
// var num=parseInt(n)-1;
// if(num==0){ return}
// $(this).next().val(num);
// });
// })
// 执行相加的效果








})