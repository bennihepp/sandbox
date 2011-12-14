$(document).ready(function() {
    $("a").click(function(event) {
        alert("Thanks for visiting!");
        event.preventDefault();
        $(this).hide("slow");
    })
    $("a").addClass("test");
});
