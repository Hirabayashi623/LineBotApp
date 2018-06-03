$(function(){
	$('.triger').on({
		'click': function(){
			$(this).next('.target').slideToggle(250);
			$(this).toggleClass('active');
		}
	});
});