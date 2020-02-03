$(document).ready(function () {
    new WOW().init();

    $(".navbar-collapse").on("click", function () {
        $(".navbar-collapse").collapse("hide");
        $a = $($(this).attr("href"));
        $("html,body").animate({
            scrollTop: $a.offset().top - 50
        }, 500);
        return false;
    });

    // Show modal in case of errors
    if (
        $("#user_name").hasClass("is-invalid") ||
        $("#user_phone").hasClass("is-invalid")
    ) {
        $("#exampleModal").modal("show");
    }
});