
	let i=1;

	
	jQuery(document).ready(function(){
		var radius = 200;
		var fields = jQuery('.itemDot');
		var container = jQuery('.dotCircle');
		var width = container.width();
		var loopid = jQuery('.circle_id').attr('id');
		var loop_id = parseInt(loopid) - 1;
		
 		radius = width/2.5;
 
		 var height = container.height();
		var angle = 0, step = (2*Math.PI) / fields.length;
		fields.each(function() {
			var x = Math.round(width/2 + radius * Math.cos(angle) - jQuery(this).width()/2);
			var y = Math.round(height/2 + radius * Math.sin(angle) - jQuery(this).height()/2);
			
			
			jQuery(this).css({
				left: x + 'px',
				top: y + 'px'
			});
			angle += step;
		});
		
		
		jQuery('.itemDot').click(function(){
			
			var dataTab= jQuery(this).data("tab");
			jQuery('.itemDot').removeClass('active');
			jQuery(this).addClass('active');
			jQuery('.CirItem').removeClass('active');
			jQuery( '.CirItem'+ dataTab).addClass('active');
			i=dataTab;
			
			jQuery('.dotCircle').css({
				"transform":"rotate("+(360-(i-1)*36)+"deg)",
				"transition":"2s"
			});
			jQuery('.itemDot').css({
				"transform":"rotate("+((i-1)*36)+"deg)",
				"transition":"1s"
			});
			
			
		});
		
		setInterval(function(){
			var dataTab= jQuery('.itemDot.active').data("tab");

			if(dataTab>loop_id||i>loop_id){
			dataTab=0;
			i=0;
			}
			jQuery('.itemDot').removeClass('active');
			jQuery('[data-tab="'+i+'"]').addClass('active');
			jQuery('.CirItem').removeClass('active');
			jQuery( '.CirItem'+i).addClass('active');
			i++;
			
			
			jQuery('.dotCircle').css({
				"transform":"rotate("+(360-(i-2)*36)+"deg)",
				"transition":"2s"
			});
			jQuery('.itemDot').css({
				"transform":"rotate("+((i-2)*36)+"deg)",
				"transition":"1s"
			});
			
			}, 5000);
		
	});



