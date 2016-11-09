function BCSlideshow(obj)
{
	var oDiv=document.getElementById(obj);	
	var oUl=oDiv.children[0];
	var aLi=oUl.children;
	var pic_num = aLi.length;
	var pic_wid = aLi[0].offsetWidth;
	var pic_hei = aLi[0].offsetHeight;		
	var width=pic_num*pic_wid;

	if(pic_num>1)
	{
		var oOl = document.getElementById('points');	

		for(var i=0;i<pic_num;i++)
		{
			var li = document.createElement('li');
			if(i==0)
			{
				li.className = 'active';
			}
			oOl.appendChild(li);
		}

		var oBtnPrev=document.getElementById('prev');
		var oBtnNext=document.getElementById('next');		

		var aBtn = oOl.children;

		oUl.innerHTML+=oUl.innerHTML;
		oUl.style.width=aLi.length*pic_wid+'px';
		
	
		var now=0;
		for(var j=0;j<aBtn.length;j++)
		{
			(function (index){
				aBtn[j].onclick=function ()
				{
					now = now+(index-now%pic_num);				
					tab();
				};
			})(j);
		}
	
		function tab()
		{
			for(var i=0;i<aBtn.length;i++)
			{
				aBtn[i].className='';
			}
			
			if(now>0)
			{
				aBtn[now%aBtn.length].className='active';
			}
			else
			{
				aBtn[(now%aBtn.length+aBtn.length)%aBtn.length].className='active';
			}
			startMove(oUl, -now*aLi[0].offsetWidth);
		}	
	
		oBtnPrev.onclick=function ()
		{
			now--;
			tab();
		};	
		oBtnNext.onclick=function ()
		{
			now++;		
			tab();
		};	
		function autoplay()
		{
			now++;		
			tab();
		}

		oDiv.timer = setInterval(autoplay,4000);
	
		oDiv.onmouseover=function()
		{
		    clearInterval(oDiv.timer);  
		};

		oDiv.onmouseout = function()
		{
			oDiv.timer = setInterval(autoplay,4000);
		};

	}

	var left=0;
	function startMove(obj, iTarget)
	{
		clearInterval(obj.timer);
		obj.timer=setInterval(function (){
			var speed=(iTarget-left)/8;
			speed=speed>0?Math.ceil(speed):Math.floor(speed);
			
			if(left==iTarget)
			{
				clearInterval(obj.timer);
			}
			else
			{
				left+=speed;
								
				if(iTarget<0)
				{
					obj.style.left=left%width+'px';
				}
				else
				{
					obj.style.left=(left%width-width)%width+'px';
				}
			}
		}, 30);
	}
}