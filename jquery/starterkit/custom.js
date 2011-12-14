$(function() {
	$("#orderedlist").addClass("red");
	$("#orderedlist li:nth(1)").hover(
		function() { $(this).addClass("blue"); },
		function() { $(this).removeClass("blue"); }
	);
	$("#orderedlist").click(function() {
		$("#orderedlist").find("li").each(function(i) {
			$(this).append( " BAM! " + i );
		})
	});
	$(document).ready(function() {
		$('#faq').find('dd').hide().end().find('dt').click(function() {
			$(this).next().slideToggle();
		});
	});

   $("a").hover(function(){
     $(this).parents("p").addClass("highlight");
   },function(){
     $(this).parents("p").removeClass("highlight");
   });

});
