var current_fs, next_fs, previous_fs; //fieldsets
var left, opacity, scale; //fieldset properties which we will animate
var animating; //flag to prevent quick multi-click glitches

$(".next").click(function(){
	if(animating) return false;
	animating = true;

	
	current_fs = $(this).parent();
	next_fs = $(this).parent().next();
	next_fss = $(next_fs).parent().next();
	
	//activate next step on progressbar using the index of next_fs
	$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
	$("#progressbar li").eq($("fieldset").index(next_fss)).addClass("active");
	
	//show the next fieldset
	next_fs.show(); 
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
		step: function(now, mx) {
			//as the opacity of current_fs reduces to 0 - stored in "now"
			//1. scale current_fs down to 80%
			scale = 1 - (1 - now) * 0.2;
			//2. bring next_fs from the right(50%)
			left = (now * 50)+"%";
			//3. increase opacity of next_fs to 1 as it moves in
			opacity = 1 - now;
			current_fs.css({'transform': 'scale('+scale+')'});
			next_fs.css({'left': left, 'opacity': opacity});
		}, 
		duration: 800, 
		complete: function(){
			current_fs.hide();
			animating = false;
		}, 
		//this comes from the custom easing plugin
		easing: 'easeInOutBack'
	});
});

$(".previous").click(function(){
	if(animating) return false;
	animating = true;
	
	current_fs = $(this).parent();
	previous_fs = $(this).parent().prev();
	previous_fss = $(previous_fs).parent().prev();
	
	//de-activate current step on progressbar
	$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
	
	
	//show the previous fieldset
	previous_fs.show(); 
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
		step: function(now, mx) {
			//as the opacity of current_fs reduces to 0 - stored in "now"
			//1. scale previous_fs from 80% to 100%
			scale = 0.8 + (1 - now) * 0.2;
			//2. take current_fs to the right(50%) - from 0%
			left = ((1-now) * 50)+"%";
			//3. increase opacity of previous_fs to 1 as it moves in
			opacity = 1 - now;
			current_fs.css({'left': left});
			previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity});
		}, 
		duration: 800, 
		complete: function(){
			current_fs.hide();
			animating = false;
		}, 
		//this comes from the custom easing plugin
		easing: 'easeInOutBack'
	});
});

$(".submit").click(function(){
	if($('#username').val()=='')
		$('#errorusername').html('enter username!');
	else{
		$('#errorusername').html('');
		$('#errorusername').parent().parent().addClass('form-group has-error has-feedback');
	}

	if($('#email').val()==''){
		$('#erroremail').html('enter your email!');
	}
	else{
		$('#erroremail').html('');
	}
	var re = /\S+@\S+\.\S+/;
    if($('#email').val().match(re)){
    	$('#erroremail').html('');	

    }else{
		$('#erroremail').html('enter valid email!');
	}


	if($('#email').val()==''){
		$('#erroremail').html('enter your email!');
	}
	else{
		$('#erroremail').html('');
	}

	
	if($('#password').val()=='')
		$('#errorpass').html('fill passwords');
	else{
		$('#errorpass').html('');
	}
	if($('#cpassword').val()=='')
		$('#errorpass').html('confirm password');
	else{
		$('#errorpass').html('');
	}
	if($('#password').val() !== $('#cpassword').val())
		$('#errorpass').html('passwords do not match');
	else{
		$('#errorpass').html('');	
	}
	if($('#fname').val()=='')
		$('#errorfname').html('enter firstname!');
	else{
		$('#errorfname').html('');
	}
	if($('#lname').val()=='')
		$('#errorlname').html('enter lastname!');
	else{
		$('#errorlname').html('');
	}

	return false;

})