$(document).ready(function() {
    $("a").click(function() {
        //alert("error!");
    })
});

 $(document).ready(function(){
   $("a.stuff").toggle(function(){
     $(".stuff").animate({ height: 'hide', opacity: 'hide' }, 'slow');
     $(".stuff2").animate({ height: 'show', opacity: 'show' }, 'slow');
   },function(){
     $(".stuff").animate({ height: 'show', opacity: 'show' }, 'slow');
     $(".stuff2").animate({ height: 'hide', opacity: 'hide' }, 'slow');
   });
 });
