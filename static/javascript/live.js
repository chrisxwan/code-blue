$(document).ready(function(){

	if ( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) ) {
    	$("head").append('<link href="/static/css/live-mobile.css" rel="stylesheet">');
	}
	$("#logo-home").click(function(){
		document.location.href="/";
	});

	$(window).load(function(){
		$(".loaded").animate({
			"opacity" : 1
		}, "slow");
	});

	$(".api-title").click(function(){
		$(this).parent().children(".api-explanation.show").animate({
			opacity: 0,
			height: 0,
			'margin-bottom': 0
		}, function(){
			$(this).removeClass("show").addClass("hidden").hide();
		});

		$(this).parent().children(".api-explanation.hidden").show().animate({
			opacity: 1,
			height: '100%',
			'margin-bottom': '20px'
		}, function(){
			$(this).removeClass("hidden").addClass("show");
		});
	})
})